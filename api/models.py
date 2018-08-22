from django.db import models
# Create your models here.

class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    experience = models.TextField()
    extra_notes = models.TextField()
    display_picture = models.ImageField(upload_to='api/pictures')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
    


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    students_name = models.CharField("Student's Name", max_length=100)
    mail = models.EmailField("e-mail", max_length=100)
    fathers_name = models.CharField("Father's Name", max_length=100)
    mothers_name = models.CharField("Mother's Name", max_length=100)
    address = models.TextField("Address")
    phone_number = models.CharField("Phone Number", max_length=13)
    guardian_phone_number = models.CharField("Guardian's Phone Number", max_length=13)
