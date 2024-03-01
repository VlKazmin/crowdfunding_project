from django.contrib import admin

from .models import Collect


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "occasion",
        "planned_amount",
        "collected_amount",
        "end_datetime",
        "status",
    )
    search_fields = ("author__username", "title", "occasion", "status")
    list_filter = ("occasion", "status", "end_datetime")
    date_hierarchy = "end_datetime"
    ordering = ("-end_datetime",)

    readonly_fields = ("contributors_count", "left_to_collect")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "author",
                    "title",
                    "occasion",
                    "description",
                    "planned_amount",
                    "collected_amount",
                    "end_datetime",
                    "status",
                )
            },
        ),
        (
            "Участники",
            {
                "fields": ("contributors", "contributors_count"),
            },
        ),
        (
            "Дополнительно",
            {
                "fields": ("cover_image", "slug"),
            },
        ),
    )

    def left_to_collect(self, obj):
        return obj.left_to_collect()

    left_to_collect.short_description = "Осталось собрать"
