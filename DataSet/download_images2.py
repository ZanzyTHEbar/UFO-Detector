from imutils import paths
import argparse
import requests
import cv2
import os
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
                help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
                help="path to output directory of images")
ap.add_argument("-s", "--start", required=False,
                help="First number to start at",
                default=0)
ap.add_argument("-v", "--verbose", required=False,
                help="Print information as we go",
                action="store_true", default=False)

ap.add_argument("-d", "--dataset", required=True,
                    help="path to input dataset")
ap.add_argument("-r", "--remove", type=int, default=-1,
                    help="whether or not duplicates should be removed (i.e., dry run)")


# grab the list of URLs from the input file, then initialize the
def read_url_list(filename):
    return open(filename).read().strip().split("\n")


# generator to read URLs and return data
def read_urls(urls, is_verbose=False):
    for url in urls:
        try:
            # try to download the image
            if is_verbose:
                print("Downloading {}".format(url))
            r = requests.get(url, timeout=60)
            yield ((url, r.content))
        except requests.exceptions.RequestException as e:
            print("Error downloading {} : {}".format(url, e))


# test if files are image data that OpenCV can read
def return_images(file_contents, is_verbose=False):
    for url, data in file_contents:
        try:
            # convert to numpy array that OpenCV can read
            nparr = np.fromstring(data, np.uint8)
            # attempt to decode data as image
            img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if img_cv is None:
                if is_verbose:
                    print("Skipping {} - not an image".format(url))
            else:
                # return the image
                yield ((url, img_cv))
        except Exception as err:
            if is_verbose:
                print("Error parsing {} : {}".format(url, err))


def write_images(images, output_dir, start=0, is_verbose=False):
    file_num = start
    for url, image in images:
        p = os.path.sep.join([output_dir, "{}.jpg".format(str(file_num).zfill(8))])
        cv2.imwrite(p, image)
        file_num += 1
        if is_verbose:
            print("{} <- {}".format(p, url))

def delete_duplicates():
    # grab the paths to all images in our input dataset directory and
    # then initialize our hashes dictionary
    print("[INFO] computing image hashes...")
    imagePaths = list(paths.list_images(args["dataset"]))
    hashes = {}
    # loop over our image paths
    for imagePath in imagePaths:
        # load the input image and compute the hash
        image = cv2.imread(imagePath)
        h = dhash(image)
        # grab all image paths with that hash, add the current image
        # path to it, and store the list back in the hashes dictionary
        p = hashes.get(h, [])
        p.append(imagePath)
        hashes[h] = p

def dhash(image, hashSize=8):
    # convert the image to grayscale and resize the grayscale image,
    # adding a single column (width) so we can compute the horizontal
    # gradient
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    # compute the (relative) horizontal gradient between adjacent
    # column pixels
    diff = resized[:, 1:] > resized[:, :-1]
    # convert the difference image to a hash and return it
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

if __name__ == "__main__":
    args = vars(ap.parse_args())
    output_dir = args["output"]
    is_verbose = args["verbose"]
    start = int(args["start"])

    urls = read_url_list(args["urls"])
    url_data = read_urls(urls, is_verbose)
    images = return_images(url_data, is_verbose)
    write_images(images, output_dir, start, is_verbose)
    delete_duplicates()