from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User



def trackmyloan(request):
	args = {'user': request.user}
	return render(request, 'trackmyloan.html', args)