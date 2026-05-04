from django import forms
from .models import Post, Tag

MAX_COMPRESSED_IMAGE_SIZE = 5 * 1024 * 1024

class MultipleFieldInput(forms.ClearableFileInput):
    '''
        Віджет поля файлів, який дозволяє вібрати кілька зображень одночасно
    '''
    # За замовчуванням Django FileInput очікує одне зображення
    # Цей прапорець дозволяє HTML input приймати декілька файлів одночасно в одному полі 
    allow_multiple_selection = True
    
class MultipleFileField(forms.FileField):
    '''
        Поле форми, яке буде очищати і валідувати список отриманих файлів
    '''
    def clean(self, data, initial = None):
        '''
            перевіряє один файл або список файлів стандарною логікою Django
        '''
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(file, initial) for file in data]

        return single_file_clean(data, initial)
        
    
class PostCreationForm(forms.Form):
    
    tags = forms.ModelMultipleChoiceField(
        requried = False,
        queryset= Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )
    
    image = MultipleFileField(
        required= False,
        widget= MultipleFieldInput(attrs= {'multiple': True, 'accept': 'image/'})
    )
    
    class Meta:
        model = Post
        fields = ('title', 'topic', 'content')