from aba_plus_ import *
from django.http import HttpResponse
from django.shortcuts import render

class ExceptionMiddleware(object):
    def process_exception(self, request, exception, *args, **kwargs):
        if isinstance(exception, CyclicPreferenceException) or \
           isinstance(exception, NonFlatException) or \
           isinstance(exception, InvalidPreferenceException):
            return HttpResponse(exception.message)
        elif isinstance(exception, WCPViolationException):
            return render(request, template_name='../templates/aba_plus_django/auto_wcp.html')
        return None