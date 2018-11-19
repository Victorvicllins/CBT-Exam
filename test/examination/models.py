import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class SubjectCategories(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class TermSession(models.Model):
	name = models.CharField(max_length=50)
	term_start = models.DateField(default=datetime.date.today)
	term_end = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=100, unique=True)
	code = models.CharField(max_length=20, unique=True)
	subject_term = models.ForeignKey(TermSession, on_delete=models.CASCADE)
	category_id = models.ForeignKey(SubjectCategories, on_delete=models.CASCADE)
	subject_question = models.ManyToManyField(TermSession, through='Question', related_name='subjectquestion')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Question(models.Model):
	term_question = models.ForeignKey(TermSession, on_delete=models.CASCADE)
	subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
	category_id = models.ForeignKey(SubjectCategories, on_delete=models.CASCADE)
	question = models.TextField()
	option_a = models.CharField(max_length=255)
	option_b = models.CharField(max_length=255)
	option_c = models.CharField(max_length=255)
	option_d = models.CharField(max_length=255)
	correct_ans = models.CharField(max_length=255)
	published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
 		return self.question

	def get_absolute_url(self):
		url = reverse('exam-home', kwargs={'id':self.id})
		return url

class ExamRecord(models.Model):
	exam_subject = models.CharField(max_length=10)
	user_key = models.CharField(max_length=255)
	attempt = models.CharField(max_length=255)
	score = models.CharField(max_length=225)
	remark = models.CharField(max_length=225)

	def __str__(self):
		return self.user_key
	
