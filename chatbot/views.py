from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def homeController(request):
    if request.method=="GET":
        domain = get_current_site(request).domain
        return render(request,"chatbot/home.html",{"domain":domain})
