# CODE SNIPPETS

```python
# create a new window to see possible AI model predictions
                layout = [
                    [sg.Text('Please enter a base64 encoded image')],
                    [sg.InputText('')],
                    [sg.Button('Ok'), sg.Button('Cancel')]
                ]
                window = sg.Window('Predict', layout)
                event, values = window.read()
                print(event, values)
                # if user presses the Ok button
                if event == 'Ok':
                    # create a new window notifying the user that the prediction was successful
                    layout = [
                        [sg.Text('Prediction successful!')],
                        [sg.Button('Ok')]
                    ]
                    window = sg.Window('Prediction Successful', layout)
                    event, values = window.read()
                    print(event, values)
                    window.close()
                # if user presses the Cancel button
                elif event == 'Cancel':
                    # create a new window notifying the user that the prediction was unsuccessful
                    layout = [
                        [sg.Text('Prediction unsuccessful!')],
                        [sg.Button('Ok')]
                    ]
                    window = sg.Window('Prediction Unsuccessful', layout)
                    event, values = window.read()
                    print(event, values)
                    window.close()
```

example of mermaid diagram with Font Awesome icons:

```mermaid
    graph LR
        fa:fa-check-->fa:fa-coffee
```

```markdown

    ```mermaid
    graph LR
        fa:fa-check-->fa:fa-coffee
    ```
```

## USEFUL LINKS

1. [Python PythonSimpleGUI](https://www.youtube.com/watch?v=IWDC9vcBIFQ)
2. [Python PythonSimpleGUI](https://www.youtube.com/watch?v=Htc-eWCafGs)
3. [Python PythonSimpleGUI](https://www.youtube.com/watch?v=e1TR9Wq0QRs)
4. [Machine Learning](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0265185)
