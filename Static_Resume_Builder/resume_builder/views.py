from django.shortcuts import render, HttpResponse

# Create your views here.
def resume_view(request):
    resume_data = {
        'name': 'Alex Johnson',
        'gender': 'male',
        'email': 'alex.johnson@example.com',
        'education': [
            {'degree': 'B.Sc. in Computer Science', 'year': 2020},
            {'degree': 'M.Sc. in AI', 'year': 2022},
        ],
        'skills': ['Python', 'Django', 'Machine Learning'],
        'experience': '2 years at XYZ Company as a backend developer'
    }
    return render(request, 'render_resume.html', resume_data)

def home_view(request):
    return HttpResponse("Welcome to the Resume Builder Home Page!")