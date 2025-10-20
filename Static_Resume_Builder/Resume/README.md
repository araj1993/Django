# Django Resume Web Application

A dynamic resume web application built with Django that displays personal resume information using Python dictionaries and Django templating language.

## Features

- **Dynamic Resume Display**: Resume data passed as Python dictionary from view to template
- **Gender-Specific Content**: Conditional rendering based on gender (male/female/other)
- **Responsive Design**: Mobile-friendly CSS styling
- **Django Templating**: Demonstrates use of Django template tags:
  - `{{ variable }}` for variable display
  - `{% extends %}` for template inheritance
  - `{% if %}` for conditional rendering
  - `{% for %}` for loop rendering
  - `{% static %}` for static file inclusion

## Project Structure

```
Resume/
├── .github/
│   └── copilot-instructions.md
├── .venv/                      # Virtual environment
├── manage.py                   # Django management script
├── resume_project/             # Main project directory
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py
└── resume/                     # Resume app
    ├── migrations/
    ├── static/
    │   └── resume/
    │       └── css/
    │           └── style.css   # Resume styling
    ├── templates/
    │   └── resume/
    │       ├── base.html       # Base template
    │       └── resume.html     # Resume template
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py                 # App URL configuration
    └── views.py                # Resume view function
```

## Key Components Documentation

### 1. URLs Configuration

#### `resume_project/urls.py` (Main Project URLs)
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),  # Routes root URL to resume app
]
```
- **Purpose**: Main URL dispatcher for the Django project
- **Key Feature**: Routes all requests to resume app URLs

#### `resume/urls.py` (App URLs)
```python
from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.resume_view, name='resume'),  # Root path shows resume
]
```
- **Purpose**: App-specific URL routing
- **Key Feature**: Maps root URL to resume_view function

### 2. Views (`resume/views.py`)
```python
def resume_view(request):
    resume_data = {
        'name': 'Anu Prithviraj',
        'skills': [{'name': 'Python', 'rating': 5}, ...],
        # ... more resume data
    }
    # Sort skills by rating (5 stars to lower)
    resume_data['skills'] = sorted(resume_data['skills'], 
                                  key=lambda x: x['rating'], reverse=True)
    return render(request, 'resume/resume.html', {'resume': resume_data})
```
- **Purpose**: Handles resume display logic
- **Key Features**: 
  - Contains structured resume data as Python dictionary
  - Dynamically sorts skills by star rating
  - Passes context to template

### 3. Templates

#### `resume/templates/resume/base.html` (Base Template)
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Resume{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'resume/css/style.css' %}">
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```
- **Purpose**: Base template for inheritance
- **Key Features**: 
  - Loads static files with `{% load static %}`
  - Provides blocks for title and content
  - Links CSS stylesheet

#### `resume/templates/resume/resume.html` (Main Resume Template)
```html
{% extends 'resume/base.html' %}
{% block content %}
<div class="resume-container">
    <!-- Personal Section (Left) -->
    <div class="personal-section">
        <h1>{{ resume.name }}</h1>
        {% if resume.gender == 'female' %}👩‍💻{% endif %}
        
        <!-- Contact Details -->
        {% for skill in resume.skills %}
            <span class="stars">
                {% for i in "12345" %}
                    {% if forloop.counter <= skill.rating %}⭐{% else %}☆{% endif %}
                {% endfor %}
            </span>
        {% endfor %}
    </div>
    
    <!-- Professional Section (Right) -->
    <div class="professional-section">
        <!-- Profile, Education, Experience -->
    </div>
</div>
{% endblock %}
```
- **Purpose**: Main resume display template
- **Key Features**: 
  - Uses `{% extends %}` for inheritance
  - Implements gender-specific emojis with `{% if %}`
  - Loops through skills with `{% for %}`
  - Dynamic star ratings system
  - Two-column layout (personal/professional)

### 4. Styling (`resume/static/resume/css/style.css`)
```css
/* Two-column grid layout */
.resume-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

/* Personal section with gradient */
.personal-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

/* Skills with star ratings */
.personal-section .skill-item {
    background: rgba(255, 255, 255, 0.2);
    border-left: 4px solid #ffffff;
}

/* Professional section */
.professional-section {
    background: white;
    padding: 40px;
}

/* Responsive design */
@media (max-width: 768px) {
    .resume-container { grid-template-columns: 1fr; }
}
```
- **Purpose**: Responsive styling for resume layout
- **Key Features**: 
  - CSS Grid for two-column layout
  - Gradient background for personal section
  - Transparent skills cards with backdrop blur
  - Hover effects and transitions
  - Mobile-responsive design
  - Print-friendly styles

## Installation & Setup

1. **Activate Virtual Environment**:
   ```bash
   .venv\Scripts\activate  # Windows
   ```

2. **Install Dependencies**:
   ```bash
   pip install django
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access Application**:
   Open browser to `http://127.0.0.1:8000`

## VS Code Integration

### Tasks Available
- **Run Django Server**: Use `Ctrl+Shift+P` → "Tasks: Run Task" → "Run Django Server"

### Extensions Installed
- **Python**: Python language support
- **Django**: Django template and syntax highlighting

## Component Integration Flow

```
1. URL Request (/) → resume_project/urls.py
2. Route to App → resume/urls.py  
3. Call View → resume/views.py (resume_view)
4. Process Data → Sort skills, prepare context
5. Render Template → resume.html extends base.html
6. Load Styles → {% static 'resume/css/style.css' %}
7. Display Resume → Two-column responsive layout
```

## Template Features Summary

| Feature | Code Example | Usage |
|---------|-------------|--------|
| **Variable Display** | `{{ resume.name }}` | Show dynamic data |
| **Template Inheritance** | `{% extends 'resume/base.html' %}` | Reuse base structure |
| **Conditional Logic** | `{% if resume.gender == 'female' %}👩‍💻{% endif %}` | Gender-specific content |
| **Loops** | `{% for skill in resume.skills %}` | Iterate over skills |
| **Static Files** | `{% static 'resume/css/style.css' %}` | Load CSS/images |
| **Blocks** | `{% block content %}...{% endblock %}` | Define template sections |

## Customization

To customize the resume data, edit the `resume_data` dictionary in `resume/views.py`:

```python
resume_data = {
    'name': 'Your Name',
    'age': 25,
    'gender': 'male',  # 'male', 'female', or 'other'
    'email': 'your.email@example.com',
    'skills': ['Python', 'Django', 'JavaScript'],
    'education': {
        'degree': 'Your Degree',
        'university': 'Your University',
        'year': '2020'
    },
    # ... more fields
}
```

## Development

- **Python Version**: 3.13.5
- **Django Version**: 5.2.7
- **Environment**: Virtual environment (venv)

## Next Steps

1. Add more resume sections (projects, certifications, etc.)
2. Implement admin interface for editing resume data
3. Add multiple resume templates
4. Implement user authentication for multiple resumes
5. Add export functionality (PDF generation)

---

**Author**: Django Resume Builder  
**Created**: October 2025  
**Framework**: Django 5.2.7