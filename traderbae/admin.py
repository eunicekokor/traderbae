from django.contrib import admin
from traderbae.models import User, Item

class UserAdmin(admin.ModelAdmin):
  list_display = ('name', 'username', 'account_created', 'school', 'email', 'items', 'new_user')

class ItemAdmin(admin.ModelAdmin):
  list_display = ('__str__', 'likes', 'new_item', 'hot_item','owner')

admin.site.register(Item, ItemAdmin)
admin.site.register(User, UserAdmin)
#admin.site.register(ItemAdmin)