from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	def __str__(self):
		return self.question_text
		
class Choices(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=255)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text