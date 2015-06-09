from django.db import models
from time import time

# Create your models here.
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

class Profile(models.Model):
    full_name = models.CharField(max_length = 50, primary_key= True)
    designation = models.CharField(max_length = 50, blank = True)
    picture = models.FileField(upload_to = get_upload_file_name)

    def __str__(self):
        return self.full_name

TITLE_CHOICES = (
    ('Dr.', 'Dr.'),
    ('Mrs.', 'Mrs.'),
    ('Miss.', 'Miss.'),
    ('Mr.', 'Mr.'),
)

class Book(models.Model):
    title = models.CharField(max_length = 500, blank = True)
    abstract = models.TextField(blank = True)
    publication_year = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    title_first = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    first_author_fname = models.CharField(max_length = 50)
    first_author_lname = models.CharField(max_length = 50)
    title_second = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    second_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    second_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    title_third = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    third_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    third_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    file = models.FileField(upload_to = get_upload_file_name)
    citation = models.TextField(blank = True)

    def __str__(self):
        return self.first_author_fname

class BookChapter(models.Model):
    title_chapter = models.CharField(max_length = 500, blank = True)
    title_book = models.CharField(max_length = 500, blank = True)
    abstract = models.TextField(blank = True)
    publication_year = models.CharField(max_length = 50)
    pages = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 500, blank = True)
    title_first = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    first_author_fname = models.CharField(max_length = 50)
    first_author_lname = models.CharField(max_length = 50)
    title_second = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    second_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    second_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    title_third = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    third_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    third_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    file = models.FileField(upload_to = get_upload_file_name)
    citation = models.TextField(blank = True)

    def __str__(self):
        return self.first_author_fname

class Rpaper(models.Model):
    title = models.CharField(max_length = 500, blank = True)
    abstract = models.TextField(blank = True)
    publication_year = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    title_first = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    first_author_fname = models.CharField(max_length = 50)
    first_author_lname = models.CharField(max_length = 50)
    title_second = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    second_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    second_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    title_third = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    third_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    third_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    file = models.FileField(upload_to = get_upload_file_name)
    citation = models.TextField(blank = True)

    def __str__(self):
        return self.first_author_fname

class Cpaper(models.Model):
    title_paper = models.CharField(max_length = 500, blank = True)
    title_conference = models.CharField(max_length = 500, blank = True)
    abstract = models.TextField(blank = True)
    publication_year = models.CharField(max_length = 50)
    pages = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    publication_place = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 500, blank = True)
    title_first = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    first_author_fname = models.CharField(max_length = 50)
    first_author_lname = models.CharField(max_length = 50)
    title_second = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    second_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    second_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    title_third = models.CharField(max_length = 50, choices=TITLE_CHOICES, default='Mrs')
    third_author_fname = models.CharField(max_length = 50, blank = True, null = True)
    third_author_lname = models.CharField(max_length = 50, blank = True, null = True)
    file = models.FileField(upload_to = get_upload_file_name)
    citation = models.TextField(blank = True)

    def __str__(self):
        return self.first_author_fname





