import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("A basic webapp that allows you to manage a to do list.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    st.checkbox(todo, key="todo" + str(index))

st.text_input(label="Enter an item to do:", placeholder="Add new to do item...",
              on_change=add_todo, key="new_todo")

st.session_state