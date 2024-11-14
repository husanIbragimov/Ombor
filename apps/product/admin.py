from django.contrib import admin

from .models import Product, Category, ProductImage, Rate, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    search_fields = ['name']
    list_filter = ['parent']


admin.site.register(Tag)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_tag']


class RateInline(admin.TabularInline):
    model = Rate
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'discount_price', 'final_price', 'discount_percent', 'amount']
    search_fields = ['name', 'category__name']
    list_select_related = ['category']
    list_filter = ['category']
    inlines = [ProductImageInline, RateInline]
    readonly_fields = ['discount_percent', 'final_price', 'image_tag']
    filter_horizontal = ['tags']
    fieldsets = (
        (None, {
            'fields': (
            'name', 'category', 'price', 'discount_price', 'tags', 'image', 'image_tag', 'description', 'amount')
        }),
    )
