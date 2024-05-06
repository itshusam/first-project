To-Do List Application Documentation :

Overview:

The To-Do List Application is a simple command-line program that allows users to manage their tasks by adding, viewing, marking as complete, 
and deleting tasks. It provides a basic interface for users to interact with their to-do list.

Main Features:

1-Add a Task: Users can add a new task to their to-do list.
2-View Tasks: Users can view all tasks currently in their to-do list.
3-Mark Task as Complete: Users can mark a task as complete, changing its status from "Incomplete" to "Complete".
4-Delete a Task: Users can delete a task from their to-do list.
5-Quit Application: Users can quit the application and exit the program.


Usage Instructions:

Adding a Task:
Select option 1 from the menu.
Enter the title of the task you want to add when prompted.
Viewing Tasks:
Select option 2 from the menu.
The application will display all tasks currently in the to-do list, including their titles and statuses.
Marking a Task as Complete:
Select option 3 from the menu.
Enter the title of the task you want to mark as complete when prompted.
The application will update the status of the specified task to "Complete".
Deleting a Task:
Select option 4 from the menu.
Enter the title of the task you want to delete when prompted.
The application will remove the specified task from the to-do list.
Quitting the Application:
Select option 5 from the menu.
The application will exit, terminating the program.


Error Handling:
If a user enters an invalid option or input, the application will display an appropriate error message.
If a user attempts to mark or delete a task that does not exist in the to-do list, the application will notify the user with an error message.


Notes:

The application uses a simple loop structure to present the menu options to the user and handle user input.
Each function in the application is responsible for a specific task (e.g., adding, viewing, marking as complete, deleting), ensuring modularity and maintainability.
