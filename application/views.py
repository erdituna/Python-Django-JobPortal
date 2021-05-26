from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from application.models import AppForm, Application
from home.models import UserProfile
from job.models import Job, Category


def index(request):
    return HttpResponse ("Application Page")


def App(request,id):
    category = Category.objects.all()
    current_user = request.user
    job = Job.objects.get(pk=id)


    if request.method == 'POST':
        form = AppForm(request.POST)

        if form.is_valid():

            data = Application()
            data.user_id = current_user.id
            data.job_id = id
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.salary = form.cleaned_data['salary']
            data.company = form.cleaned_data['company']
            data.title =form.cleaned_data['title']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Application Added ")




    form= AppForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'job': job,
               'category': category,
               'form': form,
               'profile': profile,
               }
    return render(request, 'Application_Form.html', context)



