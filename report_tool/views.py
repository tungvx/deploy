import os.path
import datetime
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext, loader
from django.core.exceptions import *
from django.middleware.csrf import get_token
from django.utils import simplejson
from django.contrib.auth.forms import *

from django.template import Context, loader
from report_tool.models import Upload,upload_file_form,handle_uploaded_file
from django.http import HttpResponse,HttpResponseRedirect
import datetime

UPLOAD = os.path.join('upload.html')

def index(request):
    message=None
    
    t = loader.get_template(os.path.join('index.html'))    
    c = RequestContext(request, { 
                                 'message':message,
                                }
                       )
    return HttpResponse(t.render(c))    
def upload_file(request):
    #This function handle upload action
    print request.POST
    message=None
    if request.method == 'POST':                # If file fo# rm is  submitted
        form = upload_file_form(request.POST, request.FILES)
        if form.is_valid():                     #Cheking form validate
            f = request.FILES['file']
            temp = Upload( filename =f.name,description = request.POST['description'],upload_time=datetime.datetime.now())
            temp.save()                         #Save file information into database
            handle_uploaded_file(f)             #Save file content to uploaded folder
            message="uploaded successfully"
        else:
            message="Error"
            #return HttpResponseRedirect('http://127.0.0.1:8000/admin')
    else:                                   #if file is not submitted that generate the upload form
        form = upload_file_form()

    c = RequestContext(request)
    return render_to_response(UPLOAD, {'form':form, 'message':message},
                              context_instance = c
                              )