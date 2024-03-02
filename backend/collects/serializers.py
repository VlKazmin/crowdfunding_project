from django.db.models import Sum
from django.utils import timezone

from rest_framework import serializers

from .models import Collect


class CollectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = [
            "title",
            "occasion",
            "description",
            "planned_amount",
            "cover_image",
            "end_datetime",
        ]

    def validate_planned_amount(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError(
                "Планируемая сумма должна быть положительным числом."
            )
        return value

    def validate_end_datetime(self, value):
        if value is not None and value <= timezone.now():
            raise serializers.ValidationError(
                "Дата и время окончания " "должны быть в будущем."
            )
        return value


class CollectSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField()
    contributors_count = serializers.SerializerMethodField()
    left_to_collect = serializers.SerializerMethodField()

    class Meta:
        model = Collect
        fields = [
            "id",
            "author",
            "title",
            "occasion",
            "description",
            "planned_amount",
            "collected_amount",
            "left_to_collect",
            "contributors",
            "contributors_count",
            "cover_image",
            "end_datetime",
            "slug",
            "status",
        ]

    def get_left_to_collect(self, obj):
        return obj.left_to_collect()

    def get_contributors(self, obj):
        contributors_data = []
        contributors = obj.contributors.all().distinct()

        for contributor in contributors:
            total_amount = obj.collects.filter(user=contributor).aggregate(
                Sum("amount")
            )["amount__sum"]
            total_amount = total_amount if total_amount is not None else 0

            contributors_data.append(
                {
                    "id": contributor.id,
                    "username": contributor.username,
                    "email": contributor.email,
                    "total_amount": total_amount,
                }
            )

        return contributors_data

    def get_contributors_count(self, obj):
        return obj.contributors.all().count()
