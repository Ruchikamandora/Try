from django import forms
from pconspectus.models import Profile, Book, BookChapter, Rpaper, Cpaper

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('full_name', 'designation', 'picture')

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'abstract', 'publication_year', 'location', 'title_first', 'first_author_fname', 'first_author_lname', 'title_second', 'second_author_fname', 'second_author_lname', 'title_third', 'third_author_fname', 'third_author_lname', 'file')

class BookChapterForm(forms.ModelForm):

    class Meta:
        model = BookChapter
        fields = ('title_chapter', 'title_book', 'pages', 'abstract', 'publication_year', 'location', 'state', 'publisher', 'title_first', 'first_author_fname', 'first_author_lname', 'title_second', 'second_author_fname', 'second_author_lname', 'title_third', 'third_author_fname', 'third_author_lname', 'file')

class RpaperForm(forms.ModelForm):

    class Meta:
        model = Rpaper
        fields = ('title', 'abstract', 'publication_year', 'location', 'state', 'title_first', 'first_author_fname', 'first_author_lname', 'title_second', 'second_author_fname', 'second_author_lname', 'title_third', 'third_author_fname', 'third_author_lname', 'file')

class CpaperForm(forms.ModelForm):

    class Meta:
        model = Cpaper
        fields = ('title_paper', 'title_conference', 'pages', 'abstract', 'publication_year', 'location', 'publication_place', 'publisher', 'title_first', 'first_author_fname', 'first_author_lname', 'title_second', 'second_author_fname', 'second_author_lname', 'title_third', 'third_author_fname', 'third_author_lname', 'file')
