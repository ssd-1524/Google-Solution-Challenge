from django.urls import path
from .views import table_view


urlpatterns = [
    path('table/', table_view),
]
