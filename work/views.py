from django.shortcuts import render
from django.views.generic import DetailView
from .models import Work

# Create your views here.
class WorkDetailView(DetailView):
    template_name = "work/work_detail.html"
    model = Work
    context_object_name = "work"



