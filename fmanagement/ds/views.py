from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from django.template import Context, Template

# Create your views here.
@csrf_exempt 
def search(request):
    return render_to_response('ds/search.html')

@csrf_exempt 
def bsearch(request):
    if request.POST:
        try:
            num1 = request.POST.get('num1')
            num2 = request.POST.get('num2')
            num3 = request.POST.get('num3')
            num4 = request.POST.get('num4')
            num5 = request.POST.get('num5')
            num6 = request.POST.get('num6')
            nums = request.POST.get('nums')
            return render_to_response('ds/bsearch.html', {'num1' : num1, 'num2' : num2, 'num3' : num3, 'num4': num4, 'num5': num5, 'num6': num6, 'nums' : nums})
        except:
            return HttpResponse("Error")
    return HttpResponse("No post")

def bsearch2(request, num1, num2, num3, num4, num5, num6, nums):
    numlist = [num1, num2, num3, num4, num5, num6]
    low = 1
    high = 6
    mid = []
    i = 1
    while(low < high):
        mid.append((low+high)/2)
        low = low+1
        #a = numlist[mid]
        #if(a == nums):
         #   return HttpResponse(mid)
        #i = i+1
    return HttpResponse(mid)
        
    
        
    
