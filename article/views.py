from django.http.response import Http404
from django.shortcuts import redirect, render
from article.forms import ArticleCreateForm
from article.models import Article
from user.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

# custom add permissions example 
# user.user_permissions.set([permission_list])
# user.user_permissions.add(permission, permission, ...)
# user.user_permissions.remove(permission, permission, ...)
# user.user_permissions.clear()

@login_required
def article_get(request,id):
    if not request.user.has_perm('article.view_article'):
        raise PermissionDenied
    article = Article.objects.get(id=id)
    if article:
        article.views = article.views + 1
        article.save()
        return render(request,"article.html", {"article": article})
    else:
        raise Http404

@login_required
@permission_required('article.add_article', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        article_form = ArticleCreateForm(request.POST,request.FILES)
        if article_form.is_valid():
            obj = article_form.save(commit=False)
            obj.user =  User.objects.get(id=request.user.id)
            obj.save()
        else:
            return render(request, "article-create.html", {"form": article_form, "errors": article_form.errors})

    form = ArticleCreateForm()
    return render(request, "article-create.html", {"form": form})


@login_required
@permission_required('article.change_article', raise_exception=True)
def article_edit(request,id):
    article = Article.objects.get(id=id)
    if request.method == 'GET':   
        if article:
            article_form = ArticleCreateForm(instance=article)
            return render(request, "article-create.html", {"form": article_form})
        else:
            raise Http404
    elif request.method == 'POST':
        article_form = ArticleCreateForm(data=request.POST , files=request.FILES, instance=article)
        article_form.save()
        return render(request,"article.html", {"article": article})

@login_required
@permission_required('article.delete_article', raise_exception=True)
def article_delete(request,id):
    article = Article.objects.get(id=id)
    if article:
        article.delete()
        return redirect('index')
    else:
        raise Http404

