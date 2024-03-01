from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
    OpenApiResponse,
)
from .serializers import CollectSerializer, CollectCreateSerializer


def collect_schema_view():
    return extend_schema_view(
        list=list_collects(),
        retrieve=retrieve_collect(),
        create=create_collect(),
        update=update_collect(),
        partial_update=partial_update_collect(),
        destroy=delete_collect(),
    )


def list_collects():
    return extend_schema(
        summary="Список сборов",
        description="Возвращает список всех сборов.",
        responses={200: CollectSerializer(many=True)},
        examples=[
            OpenApiExample(
                "Пример успешного получения списка сборов",
                summary="Успешное получение списка сборов",
                value=[
                    {
                        "id": 12,
                        "author": 1,
                        "title": "test",
                        "occasion": "birthday",
                        "description": "test",
                        "planned_amount": "124.00",
                        "collected_amount": "122.00",
                        "left_to_collect": 2.0,
                        "contributors": [
                            {
                                "id": 1,
                                "username": "test_user",
                                "email": "a@a.ru",
                            }
                        ],
                        "contributors_count": 1,
                        "cover_image": "Null",
                        "end_datetime": "2024-04-07T08:29:00+03:00",
                        "slug": "asdads",
                        "status": "active",
                    },
                ],
            ),
        ],
    )


def retrieve_collect():
    return extend_schema(
        summary="Получение информации о сборе",
        description="Возвращает информацию о конкретном сборе.",
        responses={200: CollectSerializer()},
        examples=[
            OpenApiExample(
                "Пример успешного получения информации о сборе",
                summary="Успешное получение информации о сборе",
                value={
                    "id": 13,
                    "author": 1,
                    "title": "Test",
                    "occasion": "birthday",
                    "description": "test",
                    "planned_amount": "123.00",
                    "collected_amount": "0.00",
                    "left_to_collect": 123.0,
                    "contributors": [
                        {
                            "id": 1,
                            "username": "admin",
                            "email": "a@a.ru",
                            "total_amount": 1.0,
                        }
                    ],
                    "contributors_count": 0,
                    "cover_image": "null",
                    "end_datetime": "2024-03-31T11:34:00+03:00",
                    "slug": "asd-2",
                    "status": "active",
                },
            ),
            OpenApiExample(
                "Пример ошибки с несуществующим сбором",
                summary="Ошибка - сбор не найден",
                response_only=True,
                value={"detail": "Сбор не найден."},
            ),
        ],
    )


def create_collect():
    return extend_schema(
        summary="Создание сбора",
        description="Создает новый сбор с указанными данными.",
        request=CollectCreateSerializer,
        responses={201: CollectCreateSerializer()},
        examples=[
            OpenApiExample(
                "Пример запроса дял создания сбора",
                summary="Создание сбора",
                value={
                    "title": "Свадьба",
                    "occasion": "wedding",
                    "description" "описание" "planned_amount": 1000.00,
                    "cover_image": "null",
                    "end_datetime": "2024-03-01T12:00:00Z",
                },
                request_only=True,
            ),
            OpenApiExample(
                "Пример успешного создания сбора",
                summary="Успешное создание сбора",
                value={
                    "title": "Свадьба",
                    "occasion": "wedding",
                    "description" "описание" "planned_amount": 1000.00,
                    "cover_image": "null",
                    "end_datetime": "2024-03-01T12:00:00Z",
                },
                response_only=True,
            ),
        ],
    )


def delete_collect():
    return extend_schema(
        summary="Удаление сбора",
        description="Удаляет указанный сбор.",
        responses={204: "No Content"},
        examples=[
            OpenApiExample(
                "Пример успешного удаления сбора",
                summary="Успешное удаление сбора",
                response_only=True,
                value=None,
            ),
            OpenApiExample(
                "Пример ошибки с несуществующим сбором",
                summary="Ошибка - сбор не найден",
                response_only=True,
                value={"detail": "Сбор не найден."},
            ),
        ],
    )


def update_collect():
    return extend_schema(
        summary="Обновление сбора",
        description="Обновляет данные о сборе с указанным идентификатором.",
        request=CollectCreateSerializer,
        responses={
            200: CollectSerializer(),
            404: OpenApiResponse(
                description="Сбор не найден.",
                examples=[
                    OpenApiExample(
                        "Пример ошибки с несуществующим сбором",
                        summary="Ошибка - сбор не найден",
                        value={"detail": "Сбор не найден."},
                        request_only=True,
                    ),
                ],
            ),
        },
        examples=[
            OpenApiExample(
                "Пример успешного обновления сбора",
                summary="Успешное обновление сбора",
                value={
                    "title": "Свадьба",
                    "occasion": "wedding",
                    "description": "test",
                    "planned_amount": "124.00",
                    "cover_image": "null",
                    "end_datetime": "2024-03-31T11:34:00+03:00",
                },
            ),
        ],
    )


def partial_update_collect():
    return extend_schema(
        summary="Частичное обновление сбора",
        description=("Обновляет часть данных о сборе с указанным id."),
        request=CollectCreateSerializer,
        responses={200: CollectSerializer()},
        examples=[
            OpenApiExample(
                "Пример успешного частичного обновления сбора",
                summary="Успешное частичное обновление сбора",
                value={
                    "title": "Свадьба_2",
                },
                request_only=True,
            ),
        ],
    )
