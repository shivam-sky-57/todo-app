
# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
text = """
Principles of productivity:
Managing your inflow.
Systemizing everything that repeats.
"""
print(text)

while True:
    user_action = input("Type add or show, complete, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid.")
        # case _:
        #     print("Hey, you entered an unknown command")
print("Bye!")
