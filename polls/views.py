from django.shortcuts import render
from .models import Question,Choices
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
# Create your views here.
def index(request):
	
	return render(request,"index.html" ,{})
	
def polls(request):
	polled = Question.objects.order_by("id")
	return render(request,"polls.html" , {"poller":polled})
	

def details(request , question_id):
	polled = get_object_or_404(Question , pk=question_id)
	choiceed = get_list_or_404(Choices, question=polled)	
	content_dict = {"poller":polled,"choice":choiceed}
	return render(request , "details.html" , context=content_dict)
	
def result(request,question_id):
	polled = get_object_or_404(Question , pk=question_id)
	choiceed = get_list_or_404(Choices, question=polled)	
	content_dict = {"poller":polled,"choice":choiceed}

	return render(request ,"result.html" , context=content_dict)

def vote(request,question_id):
	polled = get_object_or_404(Question , pk=question_id)
	choiceed = get_list_or_404(Choices, question=polled)	
	content_dict = {"poller":polled,"choices":choiceed}
	
	if request.method =="POST":
		selected_choice = Choices.objects.get(pk=request.POST['choice'])
		selected_choice.votes += 1
		selected_choice.save()
   
	return render(request , "vote.html" , context=content_dict)
	
