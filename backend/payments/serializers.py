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


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
