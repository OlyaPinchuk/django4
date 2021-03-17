
from django.urls import path
# from users.views import UserView
from users.views import ListCreateView, ReadUpdateDelete

urlpatterns = [
    # path('', UserView.as_view())
    path('', ListCreateView.as_view()),
    path('/<int:pk>', ReadUpdateDelete.as_view())
]