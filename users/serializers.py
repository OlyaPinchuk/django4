from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from cars.serializers import CarSerializer


UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    cars = CarSerializer(many=True, required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_superuser', 'is_staff', 'is_active', 'cars']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        print(validated_data)
        return user

