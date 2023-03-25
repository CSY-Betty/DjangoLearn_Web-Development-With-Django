from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def greeting_view(request):
    user = request.user
    return HttpResponse("Hey!{username}".format(username=user))
