from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(requst):
    return HttpResponse ('Hello,emakasana')
