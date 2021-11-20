from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from article.models import Article


def set_to_zero_views(model_admin, request, queryset):
     queryset.update(views=0)

# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/


class ArticleAdmin(admin.ModelAdmin):
     fieldsets = (
        ("Article", { # name is a string representing the title of the fieldset (blue line)
            'fields': ('title', 'short_description','image','description','user')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('views',),
        }),
    )
    #  list_display_links = ('id','short_description')
     list_display = ('id','title','views','user')
     list_editable = ('title','user')
     list_filter = ('views','user__is_staff')
     list_select_related = ('user',) #  This can save you a bunch of database queries. 
     search_fields = ('title',)
     actions = (set_to_zero_views,)

admin.site.register(Article,ArticleAdmin)
