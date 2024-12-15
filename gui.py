import functions
import FreeSimpleGUI as Fsg
import time

Fsg.theme("DarkBlue16")

clock = Fsg.Text("", key='clock_key')
label = Fsg.Text("Type in a to-do")
input_box = Fsg.InputText(tooltip="Enter todo", key='todo_iText')
add_button = Fsg.Button("Add")
list_box = Fsg.Listbox(values=functions.get_todos(), key='todo_list',
                       enable_events=True, size=(45, 10))
edit_button = Fsg.Button("Edit")
complete_button = Fsg.Button("Complete")
exit_button = Fsg.Button("Exit")


window = Fsg.Window('My To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock_key"].update(time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            latest_todo = values['todo_iText'] + "\n"
            todos.append(latest_todo)
            functions.write_todos(todos)
            window['todo_list'].update(values=todos)
        case "Edit":
            try:
                selected_index_to_edit = window['todo_list'].Widget.curselection()
                latest_todo = values['todo_iText'] + "\n"

                todos = functions.get_todos()
                index = selected_index_to_edit[0]
                todos[index] = latest_todo

                functions.write_todos(todos)
                window['todo_list'].update(values=todos)
            except IndexError:
                Fsg.Popup("Select Item from list before you Edit.", font=("Helvetica", 20))
        case "todo_list":
                window["todo_iText"].update(value=values['todo_list'][0])
        case "Complete":
            try:
                todo_to_complete = values['todo_list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo_list'].update(values=todos)
                window["todo_iText"].update(value="")
            except IndexError:
                Fsg.Popup("Select Item from list before you Complete.", font=("Helvetica", 20))
        case Fsg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
