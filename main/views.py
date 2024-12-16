from django.shortcuts import render
def index(request):
    return render(request, 'main/index.html')
def polit(request):
    return render(request, 'main/polit.html')
def sogl(request):
    return render(request, 'main/sogl.html')