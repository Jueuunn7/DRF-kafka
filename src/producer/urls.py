from django.urls import path

from producer.views import ProducerView


urlpatterns = [
    path('', ProducerView.as_view(), name='producer'),
]