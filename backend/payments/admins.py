from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "collect", "amount", "payment_date")
    search_fields = ("user__username", "collect__title", "amount")
    list_filter = ("payment_date",)
    date_hierarchy = "payment_date"
    ordering = ("-payment_date",)
    readonly_fields = ("payment_date",)

    fieldsets = (
        (None, {"fields": ("user", "collect", "amount", "description")}),
        (
            "Дата платежа",
            {
                "fields": ("payment_date",),
            },
        ),
    )
