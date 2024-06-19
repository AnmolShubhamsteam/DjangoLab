from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=122)
    student_usn = models.CharField(max_length=122)

    def __str__(self) -> str:
        return f"{self.student_name} ({self.student_usn})"

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ptopic = models.CharField(max_length=122)
    planguage = models.CharField(max_length=122)
    pduration = models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.ptopic
