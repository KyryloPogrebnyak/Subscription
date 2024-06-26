from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, UpdateUserForm
from django.http import HttpResponse
from .models import Article
from account.models import CustomUser

# Create your views here.


@login_required(login_url="login_view")
def writer_dashboard(request):
    return render(request, "writer/writer-dashboard.html")


@login_required(login_url="login_view")
def create_article(request):

    form = ArticleForm()

    if request.method == "POST":

        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("my-articles")

    context = {"CreateArticleForm": form}

    return render(request, "writer/create-article.html", context)


@login_required(login_url="login_view")
def my_articles(request):

    current_user = request.user.id
    article = Article.objects.all().filter(author=current_user)
    context = {"AllArticles": article}

    return render(request, "writer/my-articles.html", context)


@login_required(login_url="login_view")
def update_article(request, pk):

    try:

        article = Article.objects.get(id=pk, author=request.user)

    except:

        return redirect("my-articles")

    form = ArticleForm(instance=article)

    if request.method == "POST":

        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect("my-articles")

    context = {"UpdateArticleForm": form}

    return render(request, "writer/update-article.html", context)


@login_required(login_url="login_view")
def delete_article(request, pk):

    try:

        article = Article.objects.get(id=pk, author=request.user)

    except:

        return redirect("my-articles")

    if request.method == "POST":

        article.delete()

    context = {"Article": article}

    return render(request, "writer/delete-article.html", context)


@login_required(login_url="login_view")
def account_management(request):

    form = UpdateUserForm(instance=request.user)

    if request.method == "POST":

        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("writer-dashboard")

    context = {"UpdateUserForm": form}

    return render(request, "writer/account-management.html", context)

@login_required(login_url="login_view")
def delete_account(request):

    if request.method == "POST":

        deleteUser = CustomUser.objects.get(email=request.user)
        deleteUser.delete()
        return redirect("login_view")

    return render(request, "writer/delete-account.html")