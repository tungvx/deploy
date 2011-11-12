# -*- coding: utf-8 -*-
from django import forms
from mysite.settings import FILE_UPlOAD_PATH
from appengine_django.models import BaseModel
from google.appengine.ext import db

class Upload(BaseModel):                             #Upload files table in databases
    filename    = db.StringProperty()
    upload_time = db.DateTimeProperty('time uploaded')
    description = db.StringProperty()
    def __unicode__(self):
        return self.description


class upload_file_form(forms.Form):                     # Define a simple form for uploading excels file
    description   = forms.CharField(max_length=30,required=True)
    file    = forms.FileField(required=True)

def handle_uploaded_file(f):                            #Save file upload content to uploaded folder
    fd = open('%s/%s' % (FILE_UPlOAD_PATH, f.name), 'wb')     #Create new file for write
    for chunk in f.chunks():
        fd.write(chunk)                                 #Write file data
    fd.close()                                          #Close the file
