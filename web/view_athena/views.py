from django.shortcuts import render

def index(request):
    return render(request, 'view_athena/index.html', {})
