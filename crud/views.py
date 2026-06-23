from .models import Point, GradeTen
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


class HaluView(ListView):
    model= Point
    template_name= "points_grade.html"


class Detail(DetailView):
    model=Point
    template_name="detail_grade.html"

class HaluCreateView(LoginRequiredMixin, CreateView):
    model= Point
    template_name= "pointscreateview_grade.html"
    fields=["author","name","math","biology","chemistry","physics"]

class HaluUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model= Point
    template_name= "updateview_grade.html"
    fields=["name","math","biology","chemistry","physics"]

    def test_func(self):
        obj=self.get_object()
        return obj.author == self.request.user
        
class HaluDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model=Point
    template_name= "deleteview_grade.html"
    success_url=reverse_lazy("points")

    def test_func(self):
        obj= self.get_object()
        return obj.author ==  self.request.user
######################################## grade 10#########################################

class Detail_ten(DetailView):
    model= GradeTen
    template_name="detail_ten_grade.html"

class Grade_ten_list_view(ListView):
    model= GradeTen
    template_name= "list_ten_grade.html"

class Grade_ten_create_view(LoginRequiredMixin, CreateView):
    model= GradeTen
    template_name= "ten_create_grade.html"
    fields=["author","name","math","biology","chemistry","physics"]

class TenUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model= GradeTen
    template_name= "updateview_ten.html"
    fields=["name","math","biology","chemistry","physics"]

    def test_func(self):
        obj=self.get_object()
        return obj.author == self.request.user
        
class TenDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model= GradeTen
    template_name= "deleteview_ten.html"
    success_url=reverse_lazy("list_ten")

    def test_func(self):
        obj= self.get_object()
        return obj.author ==  self.request.user
# Create your views here.
