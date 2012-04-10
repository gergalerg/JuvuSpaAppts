from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms


class UserSignupForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


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


def signup(request):
    if request.method != 'POST':
        form = UserSignupForm()
    else:
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['email'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
                )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                )
            login(request, user)
            return HttpResponseRedirect('/#step/0')

    return render_to_response(
        'signup.html',
        dict(form=form),
        context_instance=RequestContext(request),
        )


