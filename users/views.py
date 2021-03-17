from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import UserModel
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status

# create POST
# read GET
# update PUT/PATCH
# delete DELETE

# GENERIC


class ListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = UserModel.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__iexact=name)
        return qs


class ReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


# ===================================================================================================================

# class ListCreateView(APIView):
#
#     def get(self, *args, **kwargs):
# 1 option      qs = UserModel.objects.all()
#         name = self.request.query_params.get('name')
#         if name:
#             qs = qs.filter(name__iexact=name)
#         users = UserSerializer(qs, many=True).data

# 2 option      db_users = UserModel.objects.all()
#         users = UserSerializer(db_users, many=True).data
#         print(users)
#         return Response(users, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = UserSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class ReadUpdateDelete(APIView):
#
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         # user = UserModel.objects.get(pk=pk)
#         user = get_object_or_404(UserModel.objects.all(), pk=pk)  # when you request non-existent id
#         data = UserSerializer(user).data
#         return Response(data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         instance = get_object_or_404(UserModel, pk=pk)
#         serializer = UserSerializer(instance, self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         instance = get_object_or_404(UserModel, pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ===================================================================================================================
# class UserView(APIView):

    # def get(self, *args, **kwargs):
    #     return Response('hello from get')
    #
    # def post(self, *args, **kwargs):
    #     return Response('hello from post')
    #
    # def put(self, *args, **kwargs):
    #     return Response('hello from put')
    #
    # def patch(self, *args, **kwargs):
    #     return Response('hello from patch')
    #
    # def delete(self, *args, **kwargs):
    #     return Response('hello from delete')

