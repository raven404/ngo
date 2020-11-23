from django import forms
# from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import Post, Comment


# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    content = forms.CharField(
        widget=TinyMCE(
            attrs={
                'required': False,
                'cols': 30,
                'rows': 20,
            }
        )
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'overview',
            'content',
            'thumbnail',
            'categories',
            'featured',
            'slider',
            'previous_post',
            'next_post'
        )


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }), label="")

    class Meta:
        model = Comment
        fields = ('content', )
