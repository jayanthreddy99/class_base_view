from typing import Any, Dict
from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse

class tempdatainsert(TemplateView):
    template_name = 'tempdatainsert.html'
    def get_context_data(self, **kwargs):
        EDO = super().get_context_data(**kwargs)
        SFO = StudentForm()
        EDO ["SFO"] = SFO
        return EDO
    def post(self,request):
        SFD = StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data insert!!!')

class tempformview(FormView):
    template_name = 'tempformview.html'
    form_class = StudentForm
    def form_valid(self, form):
        form.save()
        return HttpResponse('Insert tempformview Done!!!')
