import PySimpleGUI as sg
from catfacts import get_random_cat_fact

layout = [
    [sg.Text("Dagens random cat fact")],
    [sg.Text('Vad heter du?'), sg.InputText(key="name")],
    [sg.Button("slumpa cat fact", key="get_new")],
    [sg.Text("...", key="fact")]
]

# Create the window
window = sg.Window("Cat Facts", layout)

while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == "get_new":
        cat_fact = get_random_cat_fact()
        name = values['name']
        message = f'Hej {name} visste du att: {cat_fact}'
        window["fact"].update(message)

window.close()



