import sys



to_do_list = [] 
choise=" "
task=" "

def add_task(to_do_list, task):
    to_do_list.append({"title": task, "status": "Incomplete"})


def view_tasks(to_do_list):
    if not to_do_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. Title: {task['title']}, Status: {task['status']}")


def mark_as_complete(to_do_list, taskk):
    try:
        found_task = False
        for task in to_do_list:
            if task["title"] == taskk:
                task["status"] = "Complete"
                found_task = True
                break
        if not found_task:
            raise ValueError("Task not found in the list, please try again")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("Task marked as complete successfully.")
    finally:
        print("Marking task as complete operation completed.")


def delete_task(to_do_list, taskk):
    try:
        found_task = False
        for task in to_do_list:
            if task["title"] == taskk:
                to_do_list.remove(task)
                found_task = True
                break
        if not found_task:
            raise ValueError("Task not found in the list, please try again")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("Task deleted successfully.")
    finally:
        print("Deleting task operation completed.")



while True:
    print(
    '''
    choose one of the following:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    '''
    )
    choise=input("")
    if choise=="1":
        task=input(("please enter the task you want to add"))
        add_task(to_do_list, task)
    elif choise=="2":
        view_tasks(to_do_list)
    elif choise=="3":
        task=input("which task you want to mark as complete?")
        mark_as_complete(to_do_list, task)
    elif choise=="4":
        task=input("which task you want to delete?")
        delete_task(to_do_list, task)
    elif choise=="5":
        sys.exit()


