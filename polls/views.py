from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index")


def details(request, question_id):
    return HttpResponse("Youre looking at %s." % question_id)


def results(request, question_id):
    response = "Your looking at the voting on questions %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
