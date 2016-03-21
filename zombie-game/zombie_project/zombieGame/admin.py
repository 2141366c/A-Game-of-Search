from django.contrib import admin
from zombieGame.models import UserProfile

#class Fill_dictAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('turn',)}

admin.site.register(UserProfile)
#admin.site.register(Fill_dictAdmin)
