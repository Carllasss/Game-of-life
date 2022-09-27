from django.urls import path
from .views import update


urlpatterns = [
    path('', update, name='update'),
]
