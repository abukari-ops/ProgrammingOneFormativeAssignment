from assignment import Homework, Exam


class GradeTracker:
    """Manages homework and exam assignments."""

    def __init__(self):
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