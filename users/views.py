from rest_framework.generics import ListCreateAPIView, get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from cars.serializers import CarSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class CarCreate(ListCreateAPIView):
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=user_id)
        serializer.save(user=user)
