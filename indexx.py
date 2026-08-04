from tracker import GradeTracker


tracker = GradeTracker()

tracker.add_homework(
    "Programming",
    "Python Classes",
    18,
    20,
    "2026-08-05"
)

tracker.add_exam(
    "Mathematics",
    "Midterm Exam",
    75,
    100,
    "2026-08-10"
)

for assignment in tracker.list_assignments():
    print("------------------------------")
    print(assignment.display_details()) 