from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date', 'author']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату публикации', 'type': 'datetime-local'}),
            'author': Select(attrs={'class': 'form-control'}),
        }