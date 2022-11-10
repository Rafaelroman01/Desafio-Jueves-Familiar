from django.urls import path
from Appcoder.views import mostrar_familiares

urlpatterns = [
    path("familiares/", mostrar_familiares)
    
]
 