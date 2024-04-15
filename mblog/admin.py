
from django.contrib import admin
from .models import Post, Comment, ProfileImage, ContactInfo









class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

#admin.site.register(Post, PostAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'birth_day','email', 'description')
    search_fields = ['firstname', 'description']


admin.site.register(ContactInfo, ContactInfoAdmin)


admin.site.register(ProfileImage)



