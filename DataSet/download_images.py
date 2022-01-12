from imutils import paths
import numpy as np
import argparse
import requests
import os
import cv2

# Defining main function
def main():
    print("Executing Main Function")
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-u", "--urls", required=True,
                    help="path to file containing image URLs")
    ap.add_argument("-o", "--output", required=True,
                    help="path to output directory of images")
    
    ap.add_argument("-d", "--dataset", required=True,
                    help="path to input dataset")
    ap.add_argument("-r", "--remove", type=int, default=-1,
                    help="whether or not duplicates should be removed (i.e., dry run)")

    args = vars(ap.parse_args())
    # grab the list of URLs from the input file, then initialize the
    # total number of images downloaded thus far
    rows = open(args["urls"]).read().strip().split("\n")
    total = 0

    # loop the URLs
    for url in rows:
        try:
            # try to download the image
            r = requests.get(url, timeout=60)
            # save the image to disk
            p = os.path.sep.join([args["output"], "{}.jpg".format(
                str(total).zfill(8))])
            f = open(p, "wb")
            f.write(r.content)
            f.close()
            # update the counter
            print("[INFO] downloaded: {}".format(p))
            total += 1
        # handle if any exceptions are thrown during the download process
        except:
            print("[INFO] error downloading {}...skipping".format(p))
        
    for imagePath in paths.list_images(args["output"]):
        # initialize if the image should be deleted or not
        delete = False
        # try to load the image
        try:
            image = cv2.imread(imagePath)
            # if the image is `None` then we could not properly load it
            # from disk, so delete it
            if image is None:
                delete = True
        # if OpenCV cannot load the image then the image is likely
        # corrupt so we should delete it
        except:
            print("Except")
            delete = True
        # check to see if the image should be deleted
        if delete:
            print("[INFO] deleting {}".format(imagePath))
            os.remove(imagePath)

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
    main()
# Execute the code using "python3 download_images.py --urls urls.txt --output images"
# where urls.txt is the file containing the URLs and images is the output directory of the images
