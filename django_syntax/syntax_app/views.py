from django.shortcuts import render

def tem_context(request):
    context = {'name': 'Anu', 'age': 28, 'course': 'Python', 'title': 'Django-Templates' }
    return render(request, 'template.html', context)

def list_of_students(request):
    names = ['Sam', 'Anny', 'Poopy', 'Shark', 'Den']
    return render(request, 'template.html', {'names': names})
