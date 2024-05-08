from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='login_view')
def writer_dashboard(request):
    return render(request, 'writer/writer-dashboard.html')

@login_required(login_url='login_view')
def create_article(request):

    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return HttpResponse('Article created successfully')
    
    context = {'CreateArticleForm': form}
    return render(request, 'writer/create-article.html', context)