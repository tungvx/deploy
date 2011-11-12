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
   print 'tung'






