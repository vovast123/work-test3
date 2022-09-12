from django.contrib import admin
from src.products import models
from modeltranslation.admin import TranslationAdmin




@admin.register(models.Profile)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "for_checking","date_created")
    list_display_links = ("id", "user", )
    list_filter = ( "for_checking",)

@admin.register(models.Message)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user",)
    list_display_links = ("id", "user", )




admin.site.register(models.ProductComment)
admin.site.register(models.ProductCommentLg)





@admin.register(models.LegalProduct)
class ProductAdminLg(admin.ModelAdmin):
    pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'price',
        'owner', 'created_date', 'available'
    )
    list_filter = ('available', 'created_date', 'title')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", )
    prepopulated_fields = {"slug": ("title", )}


@admin.register(models.SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    list_display = ("id", "category", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", "category")
    prepopulated_fields = {"slug": ("title", )}


@admin.register(models.CategoryLegal)
class CategorylgAdmin(TranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", )
    prepopulated_fields = {"slug": ("title", )}

@admin.register(models.SubCategoryLegal)
class SubCategorylgAdmin(TranslationAdmin):
    list_display = ("id", "category", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", "category")
    prepopulated_fields = {"slug": ("title", )}