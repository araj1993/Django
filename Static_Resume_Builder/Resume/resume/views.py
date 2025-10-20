from django.shortcuts import render

def resume_view(request):
    """
    View function to display resume with context data
    """
    resume_data = {
        'name': 'Anu Prithviraj',
        'age': 28,
        'gender': 'female',
        'email': 'anu.prithviraj@gmail.com',
        'phone': '+91 9633*****4',
        'location': 'Trivandrum, Kerala',
        'title': 'Software Test Engineer',
        'summary': 'Passionate STE with 5 years of experience in software testing and quality assurance in various biological domains.',
        'skills': [
            {'name': 'Python', 'rating': 5},
            {'name': 'Django', 'rating':4},
            {'name': 'Git', 'rating': 5},
            {'name': 'JavaScript', 'rating': 3},
            {'name': 'Docker', 'rating': 4},
            {'name': 'PostgreSQL', 'rating': 4},
            {'name': 'Jira', 'rating': 5},
            {'name': 'Bootstrap', 'rating': 4},
            {'name': 'AWS', 'rating': 4},
            {'name': 'JAMA', 'rating': 5}
        ],
        'education': {
            'degree': 'Master of Philosophy in Computational Biology & Bioinformatics',
            'university': 'University of Kerala',
            'year': '2018',
            'gpa': '3.8/4.0'
        },
        'experience': [
            {
                'position': 'Senior Software Test Engineer',
                'company': 'Sequioa Applied Technologies',
                'duration': '2019 - Present',
                'description': 'Lead testing efforts for web applications using Django and React.'
            }
        ]
    }
    
    # Sort skills by rating in descending order (5 stars to lower)
    resume_data['skills'] = sorted(resume_data['skills'], key=lambda x: x['rating'], reverse=True)
    
    return render(request, 'resume/resume.html', {'resume': resume_data})
