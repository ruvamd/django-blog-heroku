from django.contrib import admin
from blogging.models import Post, Category

# todo: create a customized  ModelAdmin  class for the  Post  and  Category  models
class CategoryInline(admin.TabularInline):
    model = Category.posts.through


# class PostInline(admin.TabularInline):
#     model = Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = [CategoryInline,]
    exclude = ("posts",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    # inlines = [PostInline,]


# admin.site.register(Post,PostAdmin)
# admin.site.register(Category,CategoryAdmin)
