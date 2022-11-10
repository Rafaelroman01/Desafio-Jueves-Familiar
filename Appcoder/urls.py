from django.urls import path
from Appcoder.views import mostrar_Familiares

urlpatterns = [
    path("familiares/", mostrar_Familiares)
    
]
 