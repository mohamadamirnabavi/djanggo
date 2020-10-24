from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.
def articles_list(request):#قبل از دیت اگر منفی بزاریم برعکس میشه ترتیب
    articles= models.Article.objects.all().order_by('-date')

    args = {'articles':articles}
    return render(request, 'articles/articleslist.html',args )


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)

    return render(request,'articles/articlesdetail.html',{'article':article})
