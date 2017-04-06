from django.template import loader,Context,Template
from django.http import HttpResponse
from app001.models import news,content
from django.shortcuts import  render_to_response

def index(req):
    emps=news.objects.all()
    return render_to_response('html001.html',{'emps':emps})
def con(req,my_args):
    #return HttpResponse("You're looking at my_args %s." % my_args)
    cons=content.objects.all()[int(my_args)]
    str=("%s%s"%(cons.title,cons.content))
    return HttpResponse(str)
    #return render_to_response('html2.html',{'cons':cons})
