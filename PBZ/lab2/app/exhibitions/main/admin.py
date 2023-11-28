from django.contrib import admin
from main.models import Owner, Artist, ExhibitionHall, Exhibition, Exhibit
from django.db.models import OuterRef, Subquery



@admin.register(Exhibit)
class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'size', 'type', 'artist_name')
    search_fields = ('name',)

    def artist_name(self, obj):
        return obj.artist.name


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'adress', 'phone', 'type')
    search_fields = ('name',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_place', 'birth_date', 'education')
    search_fields = ('name',)


@admin.register(ExhibitionHall)
class ExhibitionHallAdmin(admin.ModelAdmin):
    list_select_related = ('owner',)
    list_display = ('name', 'adress', 'phone', 'space', 'date', 'owner_name')
    search_fields = ('name',)


    def owner_name(self, obj):
        return obj.owner.name
    

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_select_related = ('exhibition_hall',)
    list_display = ('name', 'type', 'start_date', 'end_date', 'exhibition_hall_name')
    search_fields = ('name',)


    def exhibition_hall_name(self, obj):
        return obj.exhibition_hall.name


