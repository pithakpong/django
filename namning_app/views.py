from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
def members(request):  
	mymembers = Member.objects.all().values()
	template = loader.get_template('namning_app/home.html')
	context = { 
		'mymembers': mymembers
	}
	return HttpResponse(template.render(context,request))
def details(request):
	template = loader.get_template('namning_app/detail.html')
	return HttpResponse(template.render())


def branch(request,id):
	mymembers = Member.objects.get(id=id)
	template = loader.get_template('namning_app/branch.html')
	context = { 
		'mymembers': mymembers
	}
	return HttpResponse(template.render(context,request))
def test(request):
	template = loader.get_template('namning_app/test.html')
	context = { 
		'fruits': ['Apple', 'Banana', 'Cherry'],
	}
	return HttpResponse(template.render(context,request))