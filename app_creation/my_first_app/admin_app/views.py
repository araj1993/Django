from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect

# Create your views here.
def home(request):
    return HttpResponse("Hello, This is my todo list app")

def redirect_to_home(request):
    return HttpResponseRedirect('/home')  # Redirect to the home view, url path '/home' given

def welcome_html_page(request):
    return render(request, 'welcome.html')  # Render the welcome.html template

def redirect_to_welcome(request):
    return redirect(welcome_html_page)  # Redirect using the name of the URL pattern