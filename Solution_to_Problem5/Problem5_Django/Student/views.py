# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
import re
import sys
import os
import json
from collections import defaultdict
from collections import deque
stud_stack=list()
#student_dict=defaultdict()
counter=1
def get(request):
    try:
        #student_dict['Aman'] = 'Verma'
        return render(request, 'index.html', {'studentdict': student_dict})
    except Exception as e:
        print e
        return render(request, 'index.html', {})

    # return render(request, 'student.html',{} )
def insert(request):
    student_dict={}
    if request.method == 'POST' and request.is_ajax():
        global stud_stack
        name = request.POST.getlist('name[]')
        age = request.POST.getlist('age[]')
        roll = request.POST.getlist('roll[]')
        gender = request.POST.getlist('gender[]')
        student_dict['name']=name
        student_dict['age']=age
        student_dict['roll']=roll
        student_dict['gender']=gender
        stud_stack.append(student_dict)

        print stud_stack
    return HttpResponse(json.dumps(stud_stack), content_type="application/json")

def display(request):
    global stud_stack
    if request.method == 'POST' and request.is_ajax():
        if stud_stack:
            return HttpResponse(json.dumps(stud_stack), content_type="application/json")
        else:
            return HttpResponse(json.dumps("No users added"), content_type="application/json")
def delete(request):
    if request.method == 'POST' and request.is_ajax():
        roll = request.POST.getlist('roll[]')
        global stud_stack
        print "Inside function"
        for i in stud_stack:
            if roll in i.values():
                stud_stack.remove(i)
        print stud_stack
        response="User deleted Successfully"
        return HttpResponse(json.dumps(response), content_type="application/json")
def search(request):
    if request.method == 'POST' and request.is_ajax():
        search_results=[]
        search = request.POST.getlist('search[]')
        global stud_stack
        for i in stud_stack:
            if search in i.values():
                search_results.append(i)
        if search_results:
            return HttpResponse(json.dumps(search_results), content_type="application/json")
        else:
            response="No results found"
            return HttpResponse(json.dumps(response), content_type="application/json")

