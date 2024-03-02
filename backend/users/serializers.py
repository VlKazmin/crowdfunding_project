from djoser.serializers import UserCreateSerializer

from .models import CustomUser


class UserSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        ]

        extra_kwargs = {
            "username": {"required": True},
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {
                "required": True,
                "write_only": True,
            },
        }

    # def to_representation(self, instance):
    #     """
    #     Преобразует объект пользователя в представление JSON.
    #     """
    #     data = super().to_representation(instance)
    #     request = self.context.get("request")

    #     if request.method == "GET":
    #         data.pop("password", None)

    #     return data
