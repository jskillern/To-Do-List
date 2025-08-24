from main import to_do_list

def add_task():
    new_task = input("What would you like too add to your To-Do List?")
    to_do_list.append(new_task)
    main()

def complete_task(task_position):
    index = task_position - 1
    to_do_list.pop(index)
    main()
