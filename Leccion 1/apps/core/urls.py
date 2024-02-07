from django.urls import path
from apps.core.views import home
app_name = "security"
urlpatterns = []
# urls de las vistas de menus 
urlpatterns += [
    path('home/',home.HomeTemplateView.as_view(),name="home"),
]