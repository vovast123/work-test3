from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)



@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','description',)



@register(CategoryLegal)
class CategoryLegalTranslationOptions(TranslationOptions):
    fields = ('title',)



@register(SubCategoryLegal)
class SubCategoryLegalTranslationOptions(TranslationOptions):
    fields = ('title',)



@register(LegalProduct)
class LegalProductTranslationOptions(TranslationOptions):
    fields = ('title','description','description_add',)

