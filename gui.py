import functions
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to-do")
input_box = Fsg.InputText(tooltip="Enter todo", key='todo-iText')
add_button = Fsg.Button("Add")
list_box = Fsg.Listbox(values=functions.get_todos(), key='todo_list',
                       enable_events=True, size=[45, 10])
edit_button = Fsg.Button("Edit")


window = Fsg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todo_list"])
    match event:
        case "Add":
            todos = functions.get_todos()
            latest_todo = values['todo-iText'] + "\n"
            todos.append(latest_todo)
            functions.write_todos(todos)
        case "Edit":
            try:
                selected_index_to_edit = window['todo_list'].Widget.curselection()
                latest_todo = values['todo-iText'] + "\n"

                todos = functions.get_todos()
                index = selected_index_to_edit[0]
                todos[index] = latest_todo

                functions.write_todos(todos)
                window['todo_list'].update(values=todos)
            except IndexError:
                Fsg.Popup("Select Item from list before you Edit.")

        case Fsg.WIN_CLOSED:
            break

window.close()
