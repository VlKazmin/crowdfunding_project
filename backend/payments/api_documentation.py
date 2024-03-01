from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
)

from .serializers import PaymentDetailSerializer, PaymentCreateSerializer


def payment_schema_view():
    return extend_schema_view(
        list=list_payments(),
        retrieve=retrieve_payment(),
        create=create_payment(),
        destroy=delete_payment(),
    )


def list_payments():
    return extend_schema(
        summary="Список платежей",
        description="Возвращает список всех платежей.",
        responses={200: PaymentDetailSerializer(many=True)},
        examples=[
            OpenApiExample(
                "Пример успешного получения списка платежей",
                summary="Успешное получение списка платежей",
                value=[
                    {
                        "id": 1,
                        "user": 1,
                        "collect": 1,
                        "amount": 100.00,
                        "timestamp": "2024-03-01T12:00:00Z",
                    },
                ],
                request_only=True,
            ),
        ],
    )


def retrieve_payment():
    return extend_schema(
        summary="Получение информации о платеже",
        description="Возвращает информацию о конкретном платеже.",
        responses={200: PaymentDetailSerializer},
        examples=[
            OpenApiExample(
                "Пример успешного получения информации о платеже",
                summary="Успешное получение информации о платеже",
                value={
                    "id": 1,
                    "user": 1,
                    "collect": 1,
                    "amount": 100.00,
                    "timestamp": "2024-03-01T12:00:00Z",
                },
            ),
            OpenApiExample(
                "Пример ошибки с несуществующим платежом",
                summary="Ошибка - платеж не найден",
                response_only=True,
                value={"detail": "Страница не найдена."},
            ),
        ],
    )


def create_payment():
    return extend_schema(
        summary="Создание платежа",
        description="Создает новый платеж для указанного сбора.",
        request=PaymentCreateSerializer,
        responses={
            201: PaymentDetailSerializer,
        },
        examples=[
            OpenApiExample(
                "Пример успешного создания платежа",
                summary="Успешное создание платежа",
                value={
                    "id": 1,
                    "user": 1,
                    "collect": 1,
                    "amount": 100.00,
                    "timestamp": "2024-03-01T12:00:00Z",
                },
                request_only=True,
            ),
        ],
    )


def delete_payment():
    return extend_schema(
        summary="Удаление платежа",
        description="Удаляет указанный платеж.",
        responses={204: "No Content"},
        examples=[
            OpenApiExample(
                "Пример успешного удаления платежа",
                summary="Успешное удаление платежа",
                response_only=True,
                value=None,
            ),
            OpenApiExample(
                "Пример ошибки с несуществующим платежом",
                summary="Ошибка - платеж не найден",
                response_only=True,
                value={"detail": "Страница не найдена."},
            ),
        ],
    )
