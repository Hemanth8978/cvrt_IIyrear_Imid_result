from django.shortcuts import render
from. models import Result

# Create your views here
def index(request):
    return render(request,'index.html',{})
def submit(request):
    ob=""
    ob=request.POST['text']
    data=Result.objects.filter(htn=ob)
    return render(request,'submit.html',{'data':data})