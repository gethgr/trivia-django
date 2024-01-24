from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from trivia.models import Question

# Register your models here.

class QuestionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)