from django.urls import path
from . import views

app_name = 'teaCardApp'

urlpatterns = [
        path('tea_card_view/', views.tea_card_view, name = 'tea'),
        path('dataentry/',views.data_entry, name = 'entry'),
        path('user_login/', views.user_login, name = 'user_login'),
]
