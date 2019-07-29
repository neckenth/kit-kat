from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('auth/', include('django.contrib.auth.urls'), name='auth'),
    path('requests/new/', views.new_request, name="new_request")
    # path('<int:req_id>/', views.detail, name='detail'),
    # path('new', views.new, name='new')
]
