from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import PlanA, Item_plan
# Create your views here.

class PlanAList(ListView):
    model = PlanA
    
class PlanAView(DetailView):
    model = PlanA
    
class PlanACreate(CreateView):
    model = PlanA
    fields = ['uc', 'evento', 'ch', 'obj', 'docente']
    success_url = reverse_lazy('PlanA_list')
    
class PlanAUpdate(UpdateView):
    model = PlanA
    fields = ['uc', 'evento', 'ch', 'obj', 'docente']
    success_url = reverse_lazy('PlanA_list')

class PlanADelete(DeleteView):
    model = PlanA
    success_url = reverse_lazy('PlanA_list')
    
###### Item_Plano_aula

class Item_planList(ListView):
    model = Item_plan
    
class Item_planView(DetailView):
    model = Item_plan
    
class Item_planCreate(CreateView):
    model = Item_plan
    fields = ['plana', 'content', 'proced', 'recursos']
    success_url = reverse_lazy('Item_plan_list')
    
class Item_planUpdate(UpdateView):
    model = Item_plan
    fields = ['plana', 'content', 'proced', 'recursos']
    success_url = reverse_lazy('Item_plan_list')

class Item_planDelete(DeleteView):
    model = Item_plan
    success_url = reverse_lazy('Item_plan_list')