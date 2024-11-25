import functions
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to-do")
input_box = Fsg.InputText(tooltip="Enter todo")
add_button = Fsg.Button("Add")

window = Fsg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
