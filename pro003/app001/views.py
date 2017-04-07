from django.template import loader,Context,Template
from django.http import HttpResponse
from app001.models import news,content,urls
from django.shortcuts import  render_to_response,render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    posts=news.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'html001.html', {'post_list': post_list,
                                            })
    #return render_to_response('html001.html',{'emps':emps})
def con(req,my_args):
    #return HttpResponse("You're looking at my_args %s." % my_args)
    cons=content.objects.all()[int(my_args)]
    link = urls.objects.all()[int(my_args)]
    #str=("%s%s"%(cons.title,cons.content))
    #return HttpResponse(str)
    return render_to_response('html2.html',{'title':cons.title,
                                            'content':cons.content,
                                            'link':link})
#def url(req,my_args):
 #   link=urls.object.all()[int(my_args)]
 #   return render_to_response('html2.html',{'link':link})