from typing import Any
from django import forms
from .models import BlogPost, Comment

""" in create view it default provide to form so no need to create if you want your own validation then  override below class and methods"""
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['author','title', 'content']

    def clean(self) -> dict[str, Any]:
        print(self.cleaned_data)
        title=self.cleaned_data['title']
        if len(title)>10:
            return super().clean()
        else:
            raise forms.ValidationError({'title':'title should be grater than 10'})
            # raise ValueError('title  should be graeter than  10')
        # return super().clean()    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
