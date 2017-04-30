# -*- coding: utf-8 -

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.http.response import HttpResponse
class MoodSwingsView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == '2318934571':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('error, invalid token')
		