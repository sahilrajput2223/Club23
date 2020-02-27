from django.shortcuts import render

# Create your views here.
def Home(request):
    temp ="index.html"
    return render(request, temp)