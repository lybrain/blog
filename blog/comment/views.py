from django.shortcuts import render
from django.shortcuts import redirect
from comment.forms import CommentForm

from django.contrib.auth.decorators import login_required

@login_required
def create_comment(request, article_id):
    if request.method == "POST":
        data = request.POST.copy()
        data['article'] = article_id
        comment = CommentForm(data)
        if comment.is_valid():
            comment.save()
        return redirect("article_get", id=article_id)
