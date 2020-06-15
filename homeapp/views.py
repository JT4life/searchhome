from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Property, SendMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    propertys = Property.objects.all().order_by('-created')[:10]
    paginator = Paginator(propertys, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'propertys': propertys,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'index.html', context)

def detail(request,name):
    post_list = Property.objects.filter(name=name)
    context = { 'post_list': post_list}
    return render(request, 'details.html', context)

def search(request):
    #queryset = Restaurant.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = Property.objects.filter(
            Q(name__icontains=query) |
            Q(details__icontains=query) |
            Q(purpose__icontains=query) |
            Q(housing__icontains=query)
        ).distinct()
    context = {
        'queryset':queryset
    }
    return render(request, 'search_results.html', context)

def sendMessage(request):
    if request.method=="POST":
        Email=request.POST['email']
        Message=request.POST['message']
        appinfo=SendMessage(email=Email,message=Message)
        appinfo.save()
        return render(request,'message_sent.html')

def mail(request):
    subject = "Greetings"
    msg = "Congratulations for your success"
    to = "joshua4lyfe@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)