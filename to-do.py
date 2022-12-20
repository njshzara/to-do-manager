import os

def add_task(task):
  # Open the to-do list file in append mode
  with open('todo.txt', 'a') as f:
    # Add the task to the file
    f.write(task + '\n')

def view_tasks():
  # Open the to-do list file in read mode
  with open('todo.txt', 'r') as f:
    # Read the tasks from the file
    tasks = f.read().splitlines()

  # Print the tasks
  for i, task in enumerate(tasks):
    print(f'{i + 1}. {task}')

def mark_task_complete(task_index):
  # Open the to-do list file in read mode
  with open('todo.txt', 'r') as f:
    # Read the tasks from the file
    tasks = f.read().splitlines()

  # Mark the task as complete by replacing it with an empty string
  tasks[task_index - 1] = ''

  # Open the to-do list file in write mode
  with open('todo.txt', 'w') as f:
    # Write the updated tasks to the file
    f.write('\n'.join(tasks))

# Print the available actions
print('Actions:')
print('  add <task>')
print('  view')
print('  complete <task index>')

# Get the user's input
action = input('Enter an action: ')

# Split the input into the action and the task
parts = action.split(' ')

if parts[0] == 'add':
  # Add a task
  add_task(' '.join(parts[1:]))
elif parts[0] == 'view':
  # View the tasks
  view_tasks()
elif parts[0] == 'complete':
  # Mark a task as complete
  mark_task_complete(int(parts[1]))
else:
  # Print an error message
  print('Invalid action')
