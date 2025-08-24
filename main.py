#write to a file for long term storage

to_do_list = []

def add_task():
    new_task = input("What would you like too add to your To-Do List?")
    to_do_list.append(new_task)
    main()

def complete_task(task_position):
    index = int(task_position) - 1
    to_do_list.pop(index)
    main()


def main():
    print("----------")
    print("To-Do List")
    print("----------")
    if len(to_do_list) == 0:
        print("You're out of things to do!")
        decision = input("Would you like to (add) a new task or (exit)?").lower()
    
    else:
        for task in to_do_list:
            task_position = (to_do_list.index(task) + 1 )
            print(f"{task_position}. {task}")
        decision = input("""Would you like to (add) or (complete) a task?    (exit)""").lower()
    
    if decision == "add":
        add_task()
    if decision == "complete":
        task_position = input("Which number would you like to complete?")
        print("Task Complete!")
        complete_task(task_position)
    if decision == "exit":
        return


if __name__ == "__main__":
    print(f"""
        --------------------------------
        Welcome back, let's get to work!
        --------------------------------
    """)
    main()