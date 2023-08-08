from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
    path("seating",views.seating, name="seating"),
    path("tt_1",views.tt_1, name="tt_1"),
    path("tt_2",views.tt_2, name="tt_2")
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)