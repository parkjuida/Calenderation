from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Chronicler
from .forms import ChroniclerRegistrationForm, ChroniclerLoginForm


# Create your views here.
class Registration(View):
    def get(self, request):
        form = ChroniclerRegistrationForm()
        return render(request, 'chroniclerRegistration.html', {'form': form})

    def post(self, request):
        form = ChroniclerRegistrationForm()
        form_data = form(request.POST)
        if form_data.is_valid():
            form_data.save()

        return redirect(request, '/')


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/calender', request)
        else:
            form = ChroniclerLoginForm()
            return render(request, 'login.html', {'form': form})

    def post(self, request):
        print("post")
        username = request.POST['email_address']
        password = request.POST['password']
        if username is None:
            print("user is none")
            return Response(data={'error': 'Username is none'}, status=HTTP_400_BAD_REQUEST,
                        template_name='login.html')
        if password is None:
            print("password is none")
            return Response(data={'error': 'Password is none'}, status=HTTP_400_BAD_REQUEST,
                        template_name='login.html')
        user = authenticate(username=username, password=password)
        if not user:
            print("user invalid")
            return Response(data={'error': 'Invalid user...'}, status=HTTP_400_BAD_REQUEST,
                        template_name='login.html')
        print("all did")
        login(request, user)
        return redirect('/calender', request)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/calender', request)
