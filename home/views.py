
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
from home.forms import SearchForm
from home.models import Setting, ContactFormu, ContactFormMessage
from job.models import Job, Category, Images, Comment


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


def job_detail(request,id,slug):
    category = Category.objects.all()
    job = Job.objects.get(pk=id)
    images = Images.objects.filter(job_id=id)
    comments = Comment.objects.filter(job_id=id, status='True')
    context={'job': job,
             'category':category,
             'images': images,
             'comments': comments,
              }
    return render(request,'job_detail.html',context)


def job_search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            jobs = Job.objects.filter(title__icontains=query)
            category = Category.objects.all()
            context = {'jobs': jobs,
                       'category': category }
            return render(request, 'search_jobs.html', context)

    return HttpResponseRedirect('/')
