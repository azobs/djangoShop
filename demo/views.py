from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def helloword(request):
    #return HttpResponse("HELLO WORLD")
    #return render(request, 'index.htm')
    name = None
    return render(request, 'index.htm', {'name_key': name})
    #return render(request, 'index.htm')
