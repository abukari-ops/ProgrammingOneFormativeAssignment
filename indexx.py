from tracker import GradeTracker


def display_menu():
    # Display the main Grade Tracker menu.
    print("\n=================================")
    print("          GRADE TRACKER")
    print("=================================")
    print("1. Add Homework")
    print("2. Add Exam")
    print("3. List Assignments")
    print("4. Filter Assignments")
    print("5. Show Summary")
    print("0. Exit")
    print("=================================")
def get_assignment_details():
    # Collect common assignment information from the user.
    subject = input("Enter subject: ").strip()
    title = input("Enter assignment title: ").strip()
    while True:
        try:
            score = float(input("Enter score: "))
            max_score = float(input("Enter maximum score: "))

            if score < 0:
                print("Score cannot be negative.")
            elif max_score <= 0:
                print("Maximum score must be greater than zero.")
            elif score > max_score:
                print("Score cannot be greater than the maximum score.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter numbers for the scores.")

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    return subject, title, score, max_score, due_date
def add_homework(tracker):
    # Collect and add a homework assignment.
    print("\n--- Add Homework ---")
    subject, title, score, max_score, due_date = get_assignment_details()
    tracker.add_homework(
        subject,
        title,
        score,
        max_score,
        due_date
    )

    print("Homework added successfully.")

def add_exam(tracker):
    # Collect and add an exam assignment.
    print("\n--- Add Exam ---")

    subject, title, score, max_score, due_date = get_assignment_details()

    tracker.add_exam(
        subject,
        title,
        score,
        max_score,
        due_date
    )

    print("Exam added successfully.")

def show_assignments(tracker):
    # Display all assignments in the tracker.
    assignments = tracker.list_assignments()

    if len(assignments) == 0:
        print("\nNo assignments have been added yet.")
        return

    print("\n--- All Assignments ---")

    for number, assignment in enumerate(assignments, start=1):
        print("\n------------------------------")
        print(f"Assignment {number}")
        print("------------------------------")
        print(assignment.display_details())

def main():
    # Run the Grade Tracker program.
    tracker = GradeTracker()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_homework(tracker)

        elif choice == "2":
            add_exam(tracker)

        elif choice == "3":
            show_assignments(tracker)

        elif choice == "4":
            print("\nThe filter feature will be added next.")

        elif choice == "5":
            print("\nThe summary feature will be added later.")

        elif choice == "0":
            print("\nThank you for using Grade Tracker.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select an option from 0 to 5.")


if __name__ == "__main__":
    main()