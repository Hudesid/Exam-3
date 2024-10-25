from django.contrib import admin
from . import models


class ImageInLine(admin.TabularInline):
    model = models.Image
    extra = 1
    raw_id_fields = ('post', 'about')

class CategoriesInLine(admin.TabularInline):
    model = models.Category
    extra = 1
    raw_id_fields = ('post',)

class TagsInLine(admin.TabularInline):
    model = models.Tag
    extra = 1
    raw_id_fields = ('post',)

class MySkillsInLine(admin.TabularInline):
    model = models.MySkill
    extra = 1
    raw_id_fields = ('about',)

class ChangesPolicyInLine(admin.TabularInline):
    model = models.PolicyChanges
    extra = 1
    raw_id_fields = ('policy',)

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'upload_date')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster', 'post_date')
    prepopulated_fields = {
        'slug': ('title',)
    }
    inlines = [ImageInLine, CategoriesInLine, TagsInLine]

@admin.register(models.Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(models.PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('comment',)
    inlines = [ChangesPolicyInLine]

@admin.register(models.PolicyChanges)
class PolicyChangeAdmin(admin.ModelAdmin):
    list_display = ('change',)

@admin.register(models.MySkill)
class MySkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('comment', 'quote_author')
    inlines = [ImageInLine, MySkillsInLine]

@admin.register(models.EmailSite)
class EmailSiteAdmin(admin.ModelAdmin):
    list_display = ('comment', 'title', 'email')