from django.urls import path
from . import views
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('onama', views.o_nama,),

    path('adminpanel/', views.admin_panel),
    path('adminpanel/OdobravanjeApartmana', views.odobravanje_apartmana,),
    
    path('apartmani/', ApartmanList.as_view()),
    path('apartmani/MojiApartmani', views.moji_apartmani),
    path('apartmani/DodavanjeApartmana', views.dodavanje_apartmana),
    path('apartmani/<int:pk>', views.pojedini_apartman, name='id'),
    path('apartmani/<int:pk>/Uredi', views.uredivanje_apartmana),
    path('apartmani/<int:pk>/Obrisi', views.brisanje_apartmana),
    path('apartmani/<int:pk>/NapisiRecenziju', views.pisanje_recenzije),
    path('apartmani/<int:pk>/OdobravanjeOdredjenogApartmana', views.odobravanje_odredjenog_apartmana),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)