from django.contrib import admin

from src.products import models



@admin.register(models.Profile)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "for_checking")
    list_display_links = ("id", "user", )
    list_filter = ( "for_checking",)

admin.site.register(models.Reviews)
admin.site.register(models.ReviewsLg)

class ProductImageAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.StackedInline):
    model = models.ProductImage
    max_num = 10
    extra = 0


class ProductImageLgInline(admin.StackedInline):
    model = models.ProductImageLg
    max_num = 10
    extra = 0

@admin.register(models.LegalProduct)
class ProductAdminLg(admin.ModelAdmin):
    inlines = [ProductImageLgInline, ]

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'price',
        'owner', 'created_date', 'available'
    )
    list_filter = ('available', 'created_date', 'title')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline, ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", )
    prepopulated_fields = {"slug": ("title", )}


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", "category")
    prepopulated_fields = {"slug": ("title", )}


@admin.register(models.CategoryLegal)
class CategorylgAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", )
    prepopulated_fields = {"slug": ("title", )}

@admin.register(models.SubCategoryLegal)
class SubCategorylgAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "title")
    list_display_links = ("id", "title", )
    list_filter = ("title", "category")
    prepopulated_fields = {"slug": ("title", )}