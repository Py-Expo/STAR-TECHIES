class FitnessTracker:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity, calories):
        self.activities.append((activity, calories))

    def display_activities(self):
        for idx, (activity, calories) in enumerate(self.activities, 1):
            print(f"{idx}. {activity} - Calories: {calories}")

if __name__ == "__main__":
    tracker = FitnessTracker()

    while True:
        print("\n1. Add activity")
        print("2. Display activities")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            activity = input("Enter your activity: ")
            calories = int(input("Enter calories burned: "))
            tracker.add_activity(activity, calories)
            print("Activity added successfully!")
        elif choice == "2":
            print("\n--- Your Activities ---")
            tracker.display_activities()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
