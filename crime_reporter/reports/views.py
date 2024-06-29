# reports/views.py

from rest_framework import generics
from .models import CrimeReport
from .serializers import CrimeReportSerializer

class CrimeReportCreate(generics.CreateAPIView):
    queryset = CrimeReport.objects.all()
    serializer_class = CrimeReportSerializer

class CrimeReportList(generics.ListAPIView):
    queryset = CrimeReport.objects.all()
    serializer_class = CrimeReportSerializer

    def get_queryset(self):
        queryset = CrimeReport.objects.all()
        # Add filtering logic here
        return queryset
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'reports/register.html', {'form': form})
