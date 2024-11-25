from functions import get_todos, write_todos
import time

now = time.strftime("%d/%m/%Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add / new, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action[:3] or 'new' in user_action[:3]:
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif 'show' in user_action[:4]:
        todos = get_todos()

        new_todos = []
        #Method 1 - using a for loop we strip out all the newline char's, then append the cleaned items to our new list
        #for item in todos:
        #    cleaned_Item = item.strip("\n")
        #    new_todos.append(cleaned_Item)
        #Method 2 - A List comprehension, contains an inline, for loop
        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            #Method 3 - Would be to strip out the new line here on the item variable:
            #item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in user_action[:4]:
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print(f"Your command: {user_action}, is not valid." + '\n' "edit should be used by typing: edit 2, where 2 is the number of the todo you would like to edit.")
            continue # this restarts the loop you are in from the beginning in our case the while loop our program begins with.
        except IndexError:
            print(f"Your command: {user_action}, is not valid. As there is no todo item with that number, type: edit [space] then a number between 1 and {len(todos)}")
            continue

    elif 'complete' in user_action[:8]:
        try:
            number = int(user_action[9:])

            todos = get_todos()

            completedTodo = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            message = f"The todo {completedTodo} was completed."
            print(message)

        except ValueError:
            print(f"Your command: {user_action}, is not valid." + '\n' "complete should be used by typing: complete 5, where 5 is the number of the todo you would like to complete.")
            continue
        except IndexError:
            print(f"Your command: {user_action}, is not valid. As there is no todo item with that number, type: complete [space] then a number between 1 and {len(todos)}")
            continue

    elif 'exit' in user_action[:4]:
        break
    else:
        print('This command is not valid.')