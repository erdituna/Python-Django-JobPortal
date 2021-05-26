from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import json



# Create your views here.
from home.forms import SearchForm, RegisterForm
from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile
from job.models import Job, Category, Images, Comment


def index(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    sliderdata = Job.objects.all().order_by('id')[:4]
    jobs_latest = Job.objects.all().order_by('-id')[:4] #last 4 jobs
    randomjobs = Job.objects.all().order_by('?')[:4]   #Random selected 4 jobs
    image = Images.objects.all()

    context = { 'setting' : setting,
                'sliderdata':sliderdata,
                'category': category,
                'image': image,
                'jobs_latest': jobs_latest,
                'randomjobs': randomjobs,
                }

    return render(request,'index.html',context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = { 'setting' : setting,
                'category': category,}

    return render(request,'hakkimizda.html',context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category, }


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
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = { 'setting' : setting,'form':form,'category': category, }

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
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            jobs = Job.objects.filter(title__icontains=query)
            category = Category.objects.all()
            context = {'jobs': jobs,
                       'category': category }
            return render(request, 'search_jobs.html', context)

    return HttpResponseRedirect('/')

def job_search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    job = Job.objects.filter(title__icontains=q)
    results = []
    for rs in job:
      job_json = {}
      job_json = rs.title
      results.append(job_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

            ...
        else:
            messages.warning(request, "Login Hatası! Kullanıcı adı veya şifresi hatalı.")
            return HttpResponseRedirect('/login')

            ...
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login.html', context)


def register_view(request):
    if request.method == 'POST':  # check post
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image ="images/users/users.png"
            data.save()
            return HttpResponseRedirect('/')

    form = RegisterForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'register.html', context)


