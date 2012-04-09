from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import auth


def login(request):
    '''
    '''
    assert request.method == 'POST'
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        auth.login(request, user)
        return redirect("/Hooray!")
    return redirect('/invalid_login')
