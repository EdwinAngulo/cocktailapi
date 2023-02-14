from django.urls import path
from cockapi.views import SearchView

app_name = "cockapi"

urlpatterns = [
    path("", SearchView.as_view()),
]
