from django.db import models

# Create your models here.
class Question(models.Model):
	question_txt = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date Published')
	def __str__(self):
		return self.question_txt

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default =0)
	def __str__(self):
		return self.choice_text