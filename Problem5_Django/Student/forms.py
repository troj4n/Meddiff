from django import forms

class DataForm(forms.Form):
    name=forms.CharField(label='Name', max_length=100)
    rollno=forms.CharField(label='Roll No', max_length=100)
    age=forms.CharField(label='Age', max_length=100)
    gender=forms.CharField(label='Gender', max_length=100)