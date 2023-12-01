from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import InventoryPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import InventoryPost
from django.views.generic import DetailView
from django.views.generic import DeleteView


class IndexView(ListView):
    template_name = 'index.html'
    queryset = InventoryPost.objects.order_by('-posted_at')
    paginate_by = 9
    
    
  
      
# Create your views here.

@method_decorator(login_required, name='dispatch')
class CreateInventoryView(CreateView):
    form_class = InventoryPostForm
    template_name = "post_inventory.html"
    success_url = reverse_lazy('inventory:post_done')
    

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = InventoryPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories

class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = InventoryPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name = 'detail.html'
    model = InventoryPost

class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = InventoryPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset
    
class InventoryDeleteView(DeleteView):
    model = InventoryPost
    template_name = 'inventory_delete.html'
    success_url = reverse_lazy('inventory:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)