from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def view_calc(request):
    a = int(request.POST.get('t1',0))
    b = int(request.POST.get('t2',0))
    if request.method == 'GET':
        resp = render(request,'cal/call.html')
        return resp
    elif request.method == 'POST':
        if 'btnsum' in request.POST:
            res = a + b
        elif 'btnsub' in request.POST:
            res = a - b
        elif 'btnmul' in request.POST:
            res = a * b
        elif 'btndiv' in request.POST:
            res = a / b
    d1={"a":a, "b":b, "res":res}
    resp=render(request,'cal/call.html',context=d1)
    return resp        
                    
                    
                
 
