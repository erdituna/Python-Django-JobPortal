from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('applications/', views.applications, name='applications'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),



    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    ]
