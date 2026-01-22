time_logs = []

def log_time():
    activity = input("Enter activity name: ")
    hours = float(input("Enter hours spent: "))
    time_logs.append({"activity": activity, "hours": hours})
    print("Time logged successfully")

def view_logs():
    if not time_logs:
        print("No time logs available")
    else:
        for log in time_logs:
            print("Activity:", log["activity"], "| Hours:", log["hours"])

def main():
    while True:
        print("1. Log Time")
        print("2. View Logs")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            log_time()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
