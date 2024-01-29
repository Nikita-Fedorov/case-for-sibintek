from django.urls import path
from api.views import MyselfAPIView

urlpatterns = [
    path('card/', MyselfAPIView.as_view(), name='myself-api'),
]
