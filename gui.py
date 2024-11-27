import functions
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to-do")
input_box = Fsg.InputText(tooltip="Enter todo", key='todo-iText')
add_button = Fsg.Button("Add")

window = Fsg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            latest_todo = values['todo-iText'] + "\n"
            todos.append(latest_todo)
            functions.write_todos(todos)
        case Fsg.WIN_CLOSED:
            break

window.close()
