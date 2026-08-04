class Assignment:
    """Parent class for all assignments."""

    def __init__(
        self,
        subject,
        title,
        score,
        max_score,
        due_date,
        assignment_type
    ):
        self.subject = subject.strip().title()
        self.title = title.strip().title()
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date.strip()
        self.type = assignment_type

    def calculate_percentage(self):
        """Calculate the assignment percentage."""
        return (self.score / self.max_score) * 100

    def display_details(self):
        """Return the assignment details in a readable format."""
        percentage = self.calculate_percentage()

        return (
            f"Subject: {self.subject}\n"
            f"Title: {self.title}\n"
            f"Type: {self.type}\n"
            f"Score: {self.score}/{self.max_score}\n"
            f"Percentage: {percentage:.2f}%\n"
            f"Due Date: {self.due_date}"
        )


class Homework(Assignment):
    """Represents a homework assignment."""

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(
            subject,
            title,
            score,
            max_score,
            due_date,
            "Homework"
        )


class Exam(Assignment):
    """Represents an exam assignment."""

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(
            subject,
            title,
            score,
            max_score,
            due_date,
            "Exam"
        )