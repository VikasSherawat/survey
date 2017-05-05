from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Section', {'fields': ['question']}),
    ]

    inlines = [ChoiceInLine]
    list_display = ('question','created','q_num')
    ordering = ['id']

admin.site.register(Question, QuestionAdmin)
