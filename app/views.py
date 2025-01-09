from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


# @login_required
class ArticleListView(ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_update.html"
    context_object_name = "article"
    success_url = reverse_lazy("home")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "app/article_delete.html"
    context_object_name = "article"
    success_url = reverse_lazy("home")
