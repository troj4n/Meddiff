# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import DataForm
from collections import defaultdict
stud_data=defaultdict()
def index(request):
    today = datetime.datetime.now().date()
    if request.method=='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rollno = form.cleaned_data['rollno']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            #pr(name,rollno,age,gender)
            success(request)
    else:
        form=DataForm()
    return render(request, "index.html", {"today":today,"form": form})
def success(request):
    return render(request,"success.html")
