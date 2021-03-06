from django import forms
from .models import Entry, Category, Haiku, Comment, Entry_Status, Entry
from django.contrib.auth.forms import AuthenticationForm


# login form
class AuthForm(AuthenticationForm):

    # accept all the argument
    def __init__(self, *args, **kwargs):
        # Calling the parent class's initializer
        super(AuthForm, self).__init__(*args, **kwargs)

    # custom fields
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password'}))


# submit an entry form
class SubmitEntryForm(forms.ModelForm):
    THEMES = {
        ('', '---------'),
        ('human nature', 'human nature'),
        ('nature and seasons', 'nature and seasons'),
        ('others', 'others'),
    }

    # custom fields
    full_name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 254}))
    haiku_title = forms.CharField(label="", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    author_alias = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    haiku_theme = forms.ChoiceField(choices=sorted(THEMES), label="", initial='',
                                    widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    class Meta:
        model = Entry
        fields = ("full_name", "email", "haiku_title", "author_alias", "haiku_theme")


# haiku entry form
class EntryForm(forms.ModelForm):
    THEMES = {
        ('', '---------'),
        ('human nature', 'human nature'),
        ('nature and seasons', 'nature and seasons'),
        ('others', 'others'),
    }

    # custom fields
    full_name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 254}))
    haiku_title = forms.CharField(label="", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    author_alias = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    haiku_theme = forms.ChoiceField(choices=sorted(THEMES), label="", initial='',
                                    widget=forms.Select(attrs={'class': 'form-select'}), required=True)
    entry_status = forms.ModelChoiceField(queryset=Entry_Status.objects.all(), label="",
                                          widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    class Meta:
        model = Entry
        fields = ("full_name", "email", "haiku_title", "author_alias", "haiku_theme", "entry_status")


class EntryStatusForm(forms.ModelForm):
    class Meta:
        model = Entry_Status
        fields = ("entry_status",)


class CategoryForm(forms.ModelForm):
    # custom fields
    name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 30}))

    class Meta:
        model = Category
        fields = ("name",)


class HaikuForm(forms.ModelForm):
    COMMENT_STATUS_CHOICES = (
        ('', '---------'),
        ('hide', 'hide'),
        ('show', 'show'),
        ('featured', 'featured'),
    )

    # custom fields
    author = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 100}))
    title = forms.CharField(label="", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 50}))
    haiku_status = forms.ChoiceField(choices=sorted(COMMENT_STATUS_CHOICES), label="", initial='',
                                     widget=forms.Select(attrs={'class': 'form-select'}), required=True)
    image = forms.ImageField(label='', required=True, error_messages={'invalid': "Image files only"},
                             widget=forms.FileInput)
    category = forms.ModelChoiceField(queryset=Category.objects.filter(is_deleted=False), label="",
                                      widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    class Meta:
        model = Haiku
        fields = ("author", "title", "haiku_status", "image", "category")


class CommentForm(forms.ModelForm):
    # custom fields
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 150}))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 254}))
    comment = forms.CharField(required=True, label="Comment", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'maxlength': 500}))
    rating = forms.FloatField(required=True, label="Rating", max_value=5, min_value=1,
                              widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = Comment
        fields = ("name", "email", "comment", "rating")


class UserCommentForm(forms.ModelForm):
    COMMENT_STATUS_CHOICES = (
        ('', '---------'),
        ('hide', 'hide'),
        ('show', 'show'),
    )
    # custom fields
    comment_status = forms.ChoiceField(choices=sorted(COMMENT_STATUS_CHOICES), label="", initial='',
                                       widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    class Meta:
        model = Comment
        fields = ("comment_status",)
