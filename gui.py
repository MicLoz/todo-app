import functions
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to-do")
input_box = Fsg.InputText(tooltip="Enter todo", key='todo')
add_button = Fsg.Button("Add")

window = Fsg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()


window.close()
