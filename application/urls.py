from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('app/<int:id>', views.App, name='App'),

    #path('apply/<int:id>', views.apply, name='apply'),




    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    ]
