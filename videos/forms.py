from django import forms

from .models import Video, Comment

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file', 'thumbnail', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'video_file': forms.FileInput(attrs={'class':'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Leave a Comment!'
                 })
        }

