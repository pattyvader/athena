from django.shortcuts import render

def search(request):
    if request.method == 'GET':
        term = request.GET.get('term_search')

        print term

        return render(request, 'view_athena/index.html', {})
