#daily_reminder.py

#Prompt user for task information
task = input("Enter your task:")
priority = input("Priority (high/medium/low):") .lower()
time_bound = input("Is it time-bound? (yes/no):") .lower()

#Process and give customized reminder 
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"
    
#Add extra message if task is time-sensitive
if time_bound =="yes":
    reminder +="Task that requires immediate attention today!"
else :
    reminder +="Consider completing when you have free time."

#Print the customized reminder
print("\nReminder:",reminder)
