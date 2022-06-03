from django.urls import path
from mozio_crud.views import ProviderList


urlpatterns = [
    path('providers/', ProviderList.as_view()),
]