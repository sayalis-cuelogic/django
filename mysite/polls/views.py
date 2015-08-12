from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.http import Http404
# Create your views here.

#def index(request):
#	return HttpResponse("Hey hii m polls app")

def index(request):
	#assert False, Question.objects.all()
	latest_question_list = Question.objects.order_by('-pub_date')
	#output = ','.join([p.question_txt for p in latest_question_list])
	#template = loader.get_template('polls/index.html')
	context = {'latest_question_list' : latest_question_list}				
	#return HttpResponse(template.render(context))
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request,'polls/index.html',{'question' : question})

def results(request, question_id):
	response = "you are looking at the result of question : %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting for the question %s" % question_id)

