from django.db import models

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.name} at {self.submission_date}"

class AppointmentFormSubmission(models.Model):
    full_name = models.CharField(max_length=50)
    email=models.EmailField()
    phone = models.IntegerField()
    department=models.CharField(max_length=50)
    appointment_date=models.DateField(max_length=15)
    appointment_time=models.TimeField(max_length=15)

    def __str__(self):
     return f"Submission by {self.full_name} at {self.appointment_date} {self.appointment_time}"

    

class Payment(models.Model):
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Payment for {self.phone_number} on {self.timestamp}"
    




# profiles/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.URLField()