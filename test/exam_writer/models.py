from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
	# new fields in here
	name = models.CharField(max_length=255)
	email = models.EmailField(unique=True, null=True, blank=True)
	username = models.CharField(max_length=255, unique=True)
	gender = models.CharField(max_length=10)
	private_key = models.CharField(max_length=255)
	public_key = models.CharField(max_length=255)
	active = models.BooleanField(default=False)
	status = models.TextField()
	resume = models.CharField(max_length=255)
	is_student = models.BooleanField(default=False)
	is_instructor = models.BooleanField(default=False)

	def __str__(self):
		return self.email

# class ExamRecorder(models.Model):
# 	user_key = models.CharField(max_length=255)
# 	questions = models.CharField(max_length=255)
# 	choices = models.CharField(max_length=225)

# 	def __str__(self):
# 		return self.user_key

	# def get_absolute_url(self):
	# 	return reverse('url name', kwargs={'id':self.id})

