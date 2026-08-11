from tracker import GradeTracker


def display_menu():
    """Display the main Grade Tracker menu."""
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
    """Collect and validate assignment information."""

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
            print("Invalid input. Please enter numbers for score and maximum score.")

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    return subject, title, score, max_score, due_date


def add_homework(tracker):
    """Add a homework assignment."""

    print("\n--- Add Homework ---")

    subject, title, score, max_score, due_date = get_assignment_details()

    tracker.add_homework(
        subject,
        title,
        score,
        max_score,
        due_date
    )

    print("\nHomework added successfully.")


def add_exam(tracker):
    """Add an exam assignment."""

    print("\n--- Add Exam ---")

    subject, title, score, max_score, due_date = get_assignment_details()

    tracker.add_exam(
        subject,
        title,
        score,
        max_score,
        due_date
    )

    print("\nExam added successfully.")


def show_assignments(tracker):
    """Display all assignments."""

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


def filter_assignments(tracker):
    """Filter assignments by subject, type, or month."""

    assignments = tracker.list_assignments()

    if len(assignments) == 0:
        print("\nNo assignments available to filter.")
        return

    print("\n--- Filter Assignments ---")
    print("1. Filter by Subject")
    print("2. Filter by Type")
    print("3. Filter by Month")

    choice = input("Choose a filter option: ").strip()

    if choice == "1":

        subject = input("Enter subject: ").strip()

        results = tracker.filter_by_subject(subject)

    elif choice == "2":

        assignment_type = input(
            "Enter assignment type (Homework/Exam): "
        ).strip()

        results = tracker.filter_by_type(assignment_type)

    elif choice == "3":

        month = input("Enter month (YYYY-MM): ").strip()

        results = tracker.filter_by_month(month)

    else:
        print("\nInvalid filter option.")
        return

    if len(results) == 0:
        print("\nNo matching assignments found.")
        return

    print("\n--- Filter Results ---")

    for number, assignment in enumerate(results, start=1):

        print("\n------------------------------")
        print(f"Assignment {number}")
        print("------------------------------")

        print(assignment.display_details())


def show_summary(tracker):
    """Display grade summary information."""

    summary = tracker.show_summary()

    if summary is None:
        print("\nNo assignments available for summary.")
        return

    overall_average, subject_averages, highest, lowest = summary

    print("\n=================================")
    print("          GRADE SUMMARY")
    print("=================================")

    print(f"\nOverall Average: {overall_average:.2f}%")

    print("\nSubject Averages:")

    for subject, average in subject_averages.items():
        print(f"{subject}: {average:.2f}%")

    print("\nHighest Scoring Assignment:")
    print(f"Title: {highest.title}")
    print(f"Subject: {highest.subject}")
    print(f"Score: {highest.calculate_percentage():.2f}%")

    print("\nLowest Scoring Assignment:")
    print(f"Title: {lowest.title}")
    print(f"Subject: {lowest.subject}")
    print(f"Score: {lowest.calculate_percentage():.2f}%")

    print("=================================")


def main():
    """Run the Grade Tracker program."""

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
            filter_assignments(tracker)

        elif choice == "5":
            show_summary(tracker)

        elif choice == "0":

            print("\nThank you for using Grade Tracker.")
            print("Goodbye!")

            break

        else:
            print("\nInvalid choice. Please select a number from 0 to 5.")


if __name__ == "__main__":
    main()