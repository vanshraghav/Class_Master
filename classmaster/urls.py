from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
    path("seating",views.seating, name="seating"),
    path('create_timetable', views.create_timetable, name='create_timetable'),
    path('view_timetable', views.view_timetable, name='view_timetable')
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)