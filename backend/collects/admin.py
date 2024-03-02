from django.contrib import admin

from .models import Collect


class CollectContributorsInline(admin.TabularInline):
    model = Collect.contributors.through
    verbose_name = "Участник"
    verbose_name_plural = "Участники"
    extra = 0


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "occasion",
        "planned_amount",
        "collected_amount",
        "left_to_collect",
        "end_datetime",
        "status",
    )
    search_fields = (
        "author__username",
        "title",
        "occasion",
        "status",
    )
    list_filter = ("occasion", "status", "end_datetime")
    date_hierarchy = "end_datetime"
    ordering = ("-end_datetime",)

    readonly_fields = (
        "collected_amount",
        "left_to_collect",
    )

    fieldsets = (
        (
            "Информация",
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
                    "left_to_collect",
                )
            },
        ),
        (
            "Изображения",
            {
                "fields": ("cover_image",),
            },
        ),
    )
    inlines = [CollectContributorsInline]

    def left_to_collect(self, obj):
        return obj.left_to_collect()

    left_to_collect.short_description = "Осталось собрать"
