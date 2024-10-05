from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, queryset):
    print(model_admin)
    print(dir(request))
    print(queryset)
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    search_fields = ("owner__username",)

    # def total_amenities(self, room):
    #     return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
