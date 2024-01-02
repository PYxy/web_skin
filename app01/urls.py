from django.conf.urls import url
from .views import User

urlpatterns = [
    url(r'create$', User.as_view()),
]