import base64
import requests
import sys
import numpy as np
import cv2


def get_prediction_from_image_url(argv):
    # ex: "/airplanes/00000001.jpg"
    image_to_predict = input(
        "Enter the folder path and image name of the image to predict: ")
    input_values = image_to_predict
    # Save string of image file path below
    string_of_image_file_path = "C:/Users/zacar/Documents/GitHub/UFO-Detector/DataSet/images/" + input_values
    img_filepath = string_of_image_file_path

    # Create base64 encoded string
    with open(img_filepath, "rb") as f:
        image_string = base64.b64encode(f.read()).decode("utf-8")

    # Get response from POST request
    # Update the URL as needed
    response = requests.post(
        url="http://localhost:5000/predict",
        json={"image": image_string},
    )

    data = response.json()
    top_prediction = data["predictions"][0]

    # Print the top predicted label and its confidence
    print("predicted label:\t{}\nconfidence:\t\t{}"
          .format(top_prediction["label"], top_prediction["confidence"]))


def get_prediction_from_video_feed(argv):

    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # encode as base64 jpeg
        result, jpg = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
        encodedimage = base64.b64encode(jpg)

        # Get response from POST request
        # Update the URL as needed
        response = requests.post(
            url="http://localhost:5000/predict",
            json={"image": encodedimage.decode("utf-8")},
        )

        data = response.json()
        top_prediction = data["predictions"][0]

        # Print the top predicted label and its confidence
        print("predicted label:\t{}\nconfidence:\t\t{}"
              .format(top_prediction["label"], top_prediction["confidence"]))

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # sys.exit(get_prediction_from_image_url(sys.argv))
    sys.exit(get_prediction_from_video_feed(sys.argv))
