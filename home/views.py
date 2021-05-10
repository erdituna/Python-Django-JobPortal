from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from job.models import Job, Category


def index(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    sliderdata = Job.objects.all().order_by('id')[:4]
    jobs_latest = Job.objects.all().order_by('-id')[:4] #last 4 products
    randomjobs = Job.objects.all().order_by('?')[:4]   #Random selected 4 products

    context = { 'setting' : setting,
                'sliderdata':sliderdata,
                'category': category,
                'jobs_latest': jobs_latest,
                'randomjobs': randomjobs,}
    category = Category.objects.all()
    return render(request,'index.html',context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = { 'setting' : setting}
    return render(request,'hakkimizda.html',context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = { 'setting' : setting}
    return render(request,'referanslarimiz.html',context)

def category_jobs(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    jobs = Job.objects.filter(category_id=id)
    context={'jobs': jobs,
             'category': category,
             'categorydata': categorydata}
    return render(request,'jobs.html',context)


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