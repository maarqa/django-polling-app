from django.contrib import admin
from .models import Question,Choices
# Register your models here.

class ChoiceAdmin(admin.TabularInline):
	model = Choices
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_text']}),
	('Date Information', { 'fields': ['pub_date'], 'classes': ['collapse']}), ]
	inlines = [ChoiceAdmin]
    
	
admin.site.register(Question,QuestionAdmin)