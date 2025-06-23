from django.urls import path
from .views import ai_completion, completions_list

urlpatterns = [
    path('complete/', ai_completion, name='ai-complete'),
    path('completions/', completions_list, name='completions-list'),
]
