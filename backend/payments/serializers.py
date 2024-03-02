from django.db import IntegrityError

from rest_framework import serializers

from .models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "amount",
            "collect",
            "description",
        ]

    def validate_amount(self, value):
        if value == 0:
            raise serializers.ValidationError(
                "Значение должно быть больше нуля.",
            )
        if value < 0:
            raise serializers.ValidationError(
                "Значение не может быть отрицательным числом.",
            )

        return value

    def create(self, validated_data):
        user = (
            self.context["request"].user
            if self.context["request"].user.is_authenticated
            else None
        )

        try:
            instance = Payment.objects.create(user=user, **validated_data)
            return instance
        except IntegrityError:
            raise serializers.ValidationError(
                "Неавторизованные пользователи не могут создавать платежи."
            )


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
