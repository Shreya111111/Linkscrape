from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, Http404
import requests
from .models import Link
import datetime
# Create your views here.
 
def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site','')
 
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
     

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address,name=link_text,time=datetime.datetime.now())
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()


    return render(request,'myapp/result.html',{'data':data})
 
def delete_get(request):
    if request.method == 'GET':
        # You might want to retrieve all links and render a page to show available links
        data = Link.objects.all().delete()
        return render(request, 'myapp/result.html', {'data': data})
    else:
        # Handle other HTTP methods, if required
        raise Http404("Page not found")

def clear(request):
    if request.method == 'POST':
        Link.objects.all().delete()
        return HttpResponseRedirect('/')  # Redirect to the homepage after clearing all links
    else:
        return render(request, 'myapp/result.html', {})  # Render an empty result page for GET requests

def faqs(request):
    return render(request,'myapp/faq.html',{})
def about_us(request):
    return render(request,'myapp/about_us.html',{})
    # return HttpResponse('<h1>This is about me!.</h1>')  
    # return HttpResponse('<h1> THis is about me!.</h1>')