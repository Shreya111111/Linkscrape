from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, Http404, HttpResponse
import requests
from .models import Link
import datetime
import csv
import json
import openpyxl
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
    validator=len(data)
    return render(request,'myapp/result.html',{'data':data, 'showexport':validator})
 
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
    
def export(request, format):
    
    links=Link.objects.all()

    if format=='csv':
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="scraped_links.csv"'
        writer=csv.writer(response)
        writer.writerow(['Link Address', 'Link Name', 'Scraped Time'])

        for link in links:
            writer.writerow([link.address, link.name, link.time])
        return response
    
    elif format=='json':
        response=HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="scraped_links.json"'
        data=[{'Link Address': link.address, 'Link Name': link.name, 'Scraped Time': link.time} for link in links]
        json.dump(data, response)
        return response
    
    elif format=='excel':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="scraped_links.xlsx"'
        workbook=openpyxl.Workbook()
        sheet=workbook.active
        sheet.append(['Link Address', 'Link Name', 'Scraped Time'])
        for link in links:
            sheet.append([link.address, link.name, link.time])
        workbook.save(response)
        return response
    else:
        raise Http404("Unsupported File Format")

def faqs(request):
    return render(request,'myapp/faq.html',{})
def about_us(request):
    return render(request,'myapp/about_us.html',{})
    # return HttpResponse('<h1>This is about me!.</h1>')  
    # return HttpResponse('<h1> THis is about me!.</h1>')