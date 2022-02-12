import PySimpleGUI as sg
import base64
import requests
import os.path


def main():
    print("Hello, world!")


def test_gui():
    sg.theme('Dark Blue 3')
    layout = [
        [sg.Text('Hello World!')],
        [sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    window = sg.Window('Window Title', layout)
    event, values = window.read()
    print(event, values)
    window.close()


def Signup():
    sg.theme('Dark Blue 3')
    layout = [
        [sg.Text('Please enter your desired username and password')],
        [sg.InputText(''), sg.InputText('')],
        [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Login')]
    ]
    window = sg.Window('Signup', layout)
    event, values = window.read()
    username, password = values
    print(event, values)
    is_logged_in = False

    while True:
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        # if user presses the Ok button
        if event == 'Ok':
            # create a new window notifying the user that the signup was successful
            layout = [
                [sg.Text('Signup successful!')]
            ]
            window = sg.Window('Signup Successful', layout)
            event, values = window.read()
            print(event, values)
            window.close()
        # if user presses the Cancel button
        elif event == 'Cancel':
            # create a new window notifying the user that the signup was unsuccessful
            layout = [
                [sg.Text('Signup unsuccessful!')],
                [sg.Button('Ok')]
            ]
            window = sg.Window('Signup Unsuccessful', layout)
            event, values = window.read()
            print(event, values)
            window.close()
    return username, password, is_logged_in

class LoginWindow:
    def __init__(self, username, password, is_logged_in):
        self.username = username
        self.password = password
        self.is_logged_in = is_logged_in
        self.user_details = self.UserDetails()

    class UserDetails:
        def __init__(self):
            self.username = self.username
            self.password = self.password
            self.user = [self.username, self.password]
            self.is_logged_in = self.is_logged_in

    def login_window(self):
        self.is_logged_in = False
        layout = [
            [sg.Text('Please enter your username and password')],
            [sg.InputText(''), sg.InputText('')],
            [sg.Button('Login')]
        ]
        self.window = sg.Window('Login', layout)
        self.event, self.values = self.window.read()
        self.username, self.password = self.values
        if self.username == self.user_details.user[0] and self.password == self.user_details.user[1]:
            self.is_logged_in = True
            print(f"{self.username} is logged in")
            print(self.event, self.values)
        else:
            print(f"{self.username} is not logged in")
            print(self.event, self.values)
            self.window.close()

    def Dashboard(self):
        # create a new window that will be the user's dashboard
        layout = [
            [sg.Text('Welcome to your dashboard')],
            [sg.Button('Logout')]
        ]
        self.window = sg.Window('Dashboard', layout)
        self.event, self.values = self.window.read()
        print(self.event, self.values)
        # if user presses the Logout button
        if self.event == 'Logout':
            # close the dashboard window
            self.window.close()
        self.is_logged_in = False
        print(f"{self.username} is logged out")


def CreatePost():
    # Save string of image file path below
    string_of_image_file_path = "C:/Users/zacar/Documents/GitHub/UFO-Detector/DataSet/images/airplanes/00000006.jpg"
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


def UploadImage():
    # create windown layout of two columns
    file_list_column = [
        [
            sg.Text('Please upload an image'),
            sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'),
            sg.FolderBrowse(),
            sg.Button('Upload')
        ],
        [
            sg.Listbox(values=[], enable_events=True,
                       size=(40, 20), key='-FILE LIST-')
        ],
    ]
    image_viewer_column = [
        [sg.Text('Choose an image on the left:')],
        [sg.Text(size=(40, 1), key='-TOUT-')],
        [sg.Image(key='-IMAGE-')],
    ]

    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column)
        ],
    ]
    sg.theme('Dark Blue 3')
    window = sg.Window('Upload Image', layout)
    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            break
        if event == '-FOLDER-':
            folder = values["-FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
                print("Folder does not exist")
            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".png", ".gif"))
            ]
            window['-FILE LIST-'].update(fnames)
        elif event == '-FILE LIST-':
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0])
                window['-TOUT-'].update(filename)
                window['-IMAGE-'].update(filename=filename)
            except:
                print("Folder does not exist")
                pass

    window.close()


if __name__ == "__main__":
    main()
    # test_gui()
    # Signup()
    #username, password, is_logged_in = Signup()
    #LoginWindow(username, password, is_logged_in)
    UploadImage()
