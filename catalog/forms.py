from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'preview', 'published']

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError('Title is required')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if not content:
            raise forms.ValidationError('Content is required')
        return content

    def clean_preview(self):
        preview = self.cleaned_data['preview']
        if not preview:
            raise forms.ValidationError('Preview image is required')
        return preview

    def clean_published(self):
        published = self.cleaned_data['published']
        if not published:
            raise forms.ValidationError('Publication state is required')
        return published
