from django.shortcuts import render, redirect

# Create your views here.
def news(request):
    return render(request, 'news.html', {})
    