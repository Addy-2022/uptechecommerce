from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    dob = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    profile_pix = models.ImageField(upload_to="profile")

    def __str__(self):
        return self.fullname
