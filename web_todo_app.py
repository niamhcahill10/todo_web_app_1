import streamlit as st
import todos_functions as tf

todos = tf.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    tf.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)

st.text_input(label="todo_input", label_visibility="hidden", placeholder="Add a new todo.",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        tf.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
