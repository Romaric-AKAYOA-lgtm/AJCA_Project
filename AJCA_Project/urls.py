from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from  .  import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
     # Inclusion des applications
    path('', views. home_view, name='home') , 
     path('Tuteur/', include('tuteur.urls')),
    path('Adherent/', include('Adherent.urls')),
    path('cotisation/', include('cotisation.urls')),
    path('tuteurAdherent/',include('tuteurAdherent.urls') ),
    path('activation/', include('Activation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
