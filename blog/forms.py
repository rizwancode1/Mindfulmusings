from django import forms
from .models import Article, Comment 


class CreateArticalForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ('title' , 'content', 'categories', 'tags')
        fields =('__all__')
        exclude = ['likes', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2 }),  # Make the textarea smaller
        }





