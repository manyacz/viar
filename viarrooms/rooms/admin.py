from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Rooms


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_start', 'date_end', 'price', 'get_photo')
    list_display_links = ('id', 'title', 'price')
    search_fields = ('title', 'content', 'price')
    list_editable = ('date_start', 'date_end', )
    list_filter = ('price', )
    fields = ('title','content', 'date_start', 'date_end', 'price', 'photo' , 'get_photo', 'is_published')
    readonly_fields = ('get_photo',  )
    save_on_top = True
    
    
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75px">')
        # else:
        #     return 'Фото не установлено'
        
    get_photo.short_description = 'Миниатюра'
    

# class ReserveAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date_in', 'date_out')
#     fields = ('title', 'date_in', 'date_out')
    
admin.site.register(Rooms, RoomsAdmin)
# admin.site.register(Reserve, ReserveAdmin)

admin.site.site_title = 'Управление комнатами'
admin.site.site_header = 'Управление комнатами'