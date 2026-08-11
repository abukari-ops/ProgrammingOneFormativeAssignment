from assignment import Homework, Exam


class GradeTracker:
    """Manage homework and exam assignments."""

    def __init__(self):
        """Create an empty list for assignments."""
        self.assignments = []

    def add_homework(self, subject, title, score, max_score, due_date):
        """Create and store a homework assignment."""

        homework = Homework(
            subject,
            title,
            score,
            max_score,
            due_date
        )

        self.assignments.append(homework)

        return homework

    def add_exam(self, subject, title, score, max_score, due_date):
        """Create and store an exam assignment."""

        exam = Exam(
            subject,
            title,
            score,
            max_score,
            due_date
        )

        self.assignments.append(exam)

        return exam

    def list_assignments(self):
        """Return all stored assignments."""

        return self.assignments

    def filter_by_subject(self, subject):
        """Return assignments that match a subject."""

        matching_assignments = []

        for assignment in self.assignments:

            if assignment.subject.lower() == subject.strip().lower():
                matching_assignments.append(assignment)

        return matching_assignments

    def filter_by_type(self, assignment_type):
        """Return assignments that match Homework or Exam."""

        matching_assignments = []

        for assignment in self.assignments:

            if assignment.type.lower() == assignment_type.strip().lower():
                matching_assignments.append(assignment)

        return matching_assignments

    def filter_by_month(self, month):
        """Return assignments that match a month such as 2026-08."""

        matching_assignments = []

        for assignment in self.assignments:

            if assignment.due_date.startswith(month.strip()):
                matching_assignments.append(assignment)

        return matching_assignments

    def show_summary(self):
        """Calculate grade summary information."""

        if len(self.assignments) == 0:
            return None

        percentages = []

        for assignment in self.assignments:
            percentage = assignment.calculate_percentage()
            percentages.append(percentage)

        overall_average = sum(percentages) / len(percentages)

        highest_assignment = max(
            self.assignments,
            key=lambda assignment: assignment.calculate_percentage()
        )

        lowest_assignment = min(
            self.assignments,
            key=lambda assignment: assignment.calculate_percentage()
        )

        subject_totals = {}
        subject_counts = {}

        for assignment in self.assignments:

            subject = assignment.subject
            percentage = assignment.calculate_percentage()

            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0

            subject_totals[subject] += percentage
            subject_counts[subject] += 1

        subject_averages = {}

        for subject in subject_totals:

            subject_averages[subject] = (
                subject_totals[subject] / subject_counts[subject]
            )

        return (
            overall_average,
            subject_averages,
            highest_assignment,
            lowest_assignment
        )