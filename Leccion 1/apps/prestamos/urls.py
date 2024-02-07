from django.urls import path
from apps.prestamos.views import prestamos
app_name = "prestamos"
urlpatterns = []
# urls de las vistas de menus 
urlpatterns += [
    path('list', prestamos.PrestamoListView.as_view(), name="prestamo_list"),
    path('create', prestamos.PrestamoCreateView.as_view(), name="prestamo_create"),
    path('update/<int:pk>/', prestamos.PrestamoUpdateView.as_view(), name="prestamo_update"),
    path('delete/<int:pk>/', prestamos.PrestamoDeleteView.as_view(), name="prestamo_delete"),
]