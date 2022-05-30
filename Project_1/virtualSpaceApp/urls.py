from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='VS-home'),
    path('delete/<str:Task_id>', views.delete, name='delete'),
    path('DeletVrSpace/<str:VrSpace_id>', views.DeletVrSpace, name='DeletVrSpace'),
    path('CreatTask', views.CreatTask, name='CreatTask'),
    path('CreatVrSpace', views.CreatVrSpace, name='CreatVrSpace'),
    path('UpdateTask/<str:Task_id>', views.UpdateTask, name='UpdateTask'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)