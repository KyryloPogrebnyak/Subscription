from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from writer.models import Article
from .models import Subscription


@login_required(login_url="login_view")
def client_dashboard(request):
    try:
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
        subscription_plan = subDetails.subscription_plan
    except Subscription.DoesNotExist:
        subscription_plan = "No Subscription"

    context = {"SubPlan": subscription_plan}
    return render(request, "client/client-dashboard.html", context)


@login_required(login_url="login_view")
def browse_articles(request):
    try:
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
    except Subscription.DoesNotExist:
        return render(request, "client/subscription-locked.html")

    current_subscription_plan = subDetails.subscription_plan

    if current_subscription_plan == "Standard":
        articles = Article.objects.all().filter(is_premium=False)
    elif current_subscription_plan == "Premium":
        articles = Article.objects.all()

    context = {"AllClientArticles": articles}
    return render(request, "client/browse-articles.html", context)


@login_required(login_url="login_view")
def subscription_locked(request):
    try:
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
        subscription_plan = subDetails.subscription_plan
    except Subscription.DoesNotExist:
        subscription_plan = "No Subscription"

    context = {"SubPlan": subscription_plan}
    return render(request, "client/subscription-locked.html", context)
