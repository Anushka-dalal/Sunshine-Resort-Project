from django.urls import path
from .views import *
from .models import *


urlpatterns = [
    path('', home.as_view()),
    path('booking/', booking.as_view()),
    path('display/', display.as_view()),
    path('update/<int:id>', update.as_view()),
    path('delete/<int:id>', delete.as_view()),
    path('gallery/', gallery),

]