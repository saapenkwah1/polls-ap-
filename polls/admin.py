from django.contrib import admin
from .models import Choice, Question
# Register your models here.

#admin.site.register(Question)
#admin.site.register(Choice)
#class ChoiceInline(admin.StackedInline):
    # model = Choice
    # extra = 3
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['callapse']}),]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
