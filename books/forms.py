from django import forms
from .models import CommentModel

class UserCommentFrom(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ["body"]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields["body"].widget.attrs.update(
                {
                    "class": "px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none dark:text-white dark:placeholder-gray-400 dark:bg-gray-800",
                    "placeholder": "Write a comment...",
                    "rows": "6",
                },
                
            )