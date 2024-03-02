from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
)

from users.serializers import UserSerializer


def user_schema_view():
    return extend_schema_view(
        list=list_users(),
        retrieve=retrieve_user(),
        create=create_user(),
        update=update_user(),
        partial_update=partial_update_user(),
        destroy=delete_user(),
        me=me(),
    )


def create_user():
    return extend_schema(
        summary="Создание пользователя",
        request=UserSerializer,
        responses={201: UserSerializer},
        description="Создает нового пользователя",
        examples=[
            OpenApiExample(
                "Запрос",
                summary="Пример запроса для создания пользователя",
                description="Пример JSON-объекта для создания пользователя",
                value={
                    "username": "example_user",
                    "email": "example@example.com",
                    "first_name": "test",
                    "last_name": "test",
                    "password": "test",
                },
                request_only=True,
            ),
            OpenApiExample(
                "Ответ",
                summary="Пример успешного ответа после создания пользователя",
                description="Пример JSON-объекта с информацией о созданном "
                "пользователе",
                value={
                    "username": "example_user",
                    "email": "example@example.com",
                    "first_name": "test",
                    "last_name": "test",
                },
                response_only=True,
            ),
        ],
    )


def update_user():
    return extend_schema(
        summary="Полное обновление пользователя",
        request=UserSerializer,
        responses={200: UserSerializer},
        description="Обновляет пользователя",
        examples=[
            OpenApiExample(
                "Запрос",
                summary="Пример запроса для полного обновления пользователя",
                description="Пример JSON-объекта для полного обновления "
                "пользователя",
                value={
                    "username": "updated_user",
                    "email": "updated@example.com",
                    "first_name": "updated_test",
                    "last_name": "updated_test",
                    "password": "updated_password",
                },
                request_only=True,
            ),
            OpenApiExample(
                "Ответ",
                summary="Пример успешного ответа после полного обновления "
                "пользователя",
                description="Пример JSON-объекта с информацией о обновленном "
                "пользователе",
                value={
                    "username": "updated_user",
                    "email": "updated@example.com",
                    "first_name": "updated_test",
                    "last_name": "updated_test",
                },
                response_only=True,
            ),
        ],
    )


def list_users():
    return extend_schema(
        summary="Список пользователей",
        responses={200: UserSerializer(many=True)},
        description="Возвращает список всех пользователей",
    )


def me():
    return extend_schema(
        summary="Действия с текущим пользователем",
        responses={200: UserSerializer()},
        description="Возвращает информацию о текущем пользователе",
        examples=[
            OpenApiExample(
                "Ответ",
                summary="Пример успешного ответа для текущего пользователя",
                description="Пример JSON-объекта с информацией о текущем "
                "пользователе",
                value={
                    "username": "current_user",
                    "email": "current@example.com",
                    "first_name": "current_test",
                    "last_name": "current_test",
                },
                response_only=True,
            ),
        ],
    )


def retrieve_user():
    return extend_schema(
        summary="Получение профиля одного пользователя",
        responses={200: UserSerializer},
        description="Возвращает информацию о пользователе",
        examples=[
            OpenApiExample(
                "Ответ",
                summary="Пример успешного ответа для профиля пользователя",
                description="Пример JSON-объекта с информацией о пользователе",
                value={
                    "id": "id",
                    "username": "example_user",
                    "email": "example@example.com",
                    "first_name": "test",
                    "last_name": "test",
                },
                response_only=True,
            ),
        ],
    )


def delete_user():
    return extend_schema(
        summary="Удаление пользователя",
        responses={204: None},
        description="Удаляет пользователя",
    )


def partial_update_user():
    return extend_schema(
        summary="Частичное обновление пользователя",
        request=UserSerializer,
        responses={200: UserSerializer},
        description="Частично обновляет пользователя",
        examples=[
            OpenApiExample(
                "Запрос",
                summary="Пример запроса для частичного "
                "обновления пользователя",
                description="Пример JSON-объекта для частичного обновления "
                "пользователя",
                value={"email": "updated@example.com"},
                request_only=True,
            ),
            OpenApiExample(
                "Ответ",
                summary="Пример успешного ответа после частичного обновления "
                "пользователя",
                description="Пример JSON-объекта с информацией о частично "
                "обновленном пользователе",
                value={
                    "username": "example_user",
                    "email": "updated@example.com",
                    "first_name": "test",
                    "last_name": "test",
                },
                response_only=True,
            ),
        ],
    )
