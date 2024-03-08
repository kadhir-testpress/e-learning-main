from django.contrib import admin
from .models import Subject, Course, Module
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline, OrderedInlineModelAdminMixin

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(OrderedTabularInline):
    model = Module
    fields = ('title', 'description', 'move_up_down_links')
    readonly_fields = ('order', 'move_up_down_links')
    ordering = ('order',)
    extra = 1

@admin.register(Course)
class CourseAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline,]