from django.shortcuts import render

# Create your views here.
def homeController(request):
    if request.method=="GET":
        return render(request,"chatbot/home.html")
