from django.db import models

class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    DateOfBirth = models.DateField()
    Course = models.CharField(max_length=100)
    EnrollmentDate = models.DateField()

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
