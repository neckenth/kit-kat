from django.urls import path

from . import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    # path('<int:req_id>/', views.detail, name='detail'),
    # path('new', views.new, name='new')
]
