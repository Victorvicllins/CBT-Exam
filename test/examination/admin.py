from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from exam_writer.forms import CustomUserCreationForm, CustomUserChangeForm
from exam_writer.models import CustomUser
from .models import *

admin.site.site_header = "Harmony CBT Administration"
# Register your models here.
class SubjectCategoriesAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at',)

admin.site.register(SubjectCategories, SubjectCategoriesAdmin)

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['username', 'email', 'is_student', 'is_instructor']

admin.site.register(CustomUser, CustomUserAdmin)

class TermSessionAdmin(admin.ModelAdmin):
	list_display = ['name', 'term_start', 'term_end']

admin.site.register(TermSession, TermSessionAdmin)

class SubjectAdmin(admin.ModelAdmin):
	list_display = ['name', 'category_id', 'code']
	ist_display_links = ('subject_term',)
	list_editable = ['code']

admin.site.register(Subject, SubjectAdmin)

def published(modeladmin, request, queryset):
	queryset.update(published=True)

def unpublished(modeladmin,request,queryset):
	queryset.update(published=False)	

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['term_question', 'subject_id', 'category_id', 'question', 'correct_ans', 'published', 'created_at']
	list_display_links = ['term_question', 'subject_id']
	list_filter = ['term_question', 'subject_id', 'published', 'created_at']
	#list_display_links = ('term_question', 'subject_id')
	list_editable = ['question', 'correct_ans']
	actions = [published, unpublished]

admin.site.register(Question, QuestionAdmin)
