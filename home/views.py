from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from job.models import Job


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Job.objects.all().order_by('id')[:4]
    context = { 'setting' : setting,
                'sliderdata':sliderdata}
    return render(request,'index.html',context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = { 'setting' : setting}
    return render(request,'hakkimizda.html',context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = { 'setting' : setting}
    return render(request,'referanslarimiz.html',context)

def iletisim(request):
    if request.method == 'POST':  # check post
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = { 'setting' : setting,'form':form}

    return render(request,'iletisim.html',context)