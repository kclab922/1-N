from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    
    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()

    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


def comment_create(request, article_id):
    # 여기에는 컨텐츠만 저장된 상태
    form = CommentForm(request.POST)

    if form.is_valid():
        # form을 저장 => 추가로 넣어야 하는 데이터를 넣기 위해 잠시 저장 멈춰! 
        # 파이썬 코드로는 만들어놓고, db에는 아직 넣지 마.
        comment = form.save(commit=False)

        # # 첫번째 방법(객체를 저장하는 방법)
        # # article_id를 기준으로 article obj 가져오기 (Read와 같음)
        # article = Article.objects.get(id=article_id)
        # # article 컬럼에 추가
        # 이 방법은 DB를 조회함
        # comment.article = article
        # comment.save()

        # 두번째 방법(integer를 저장하는 방법)
        # 이 방법은 DB를 호출하지 않으므로, 속도가 더 빠름
        comment.article_id = article_id
        comment.save()

        return redirect('articles:detail', id=article_id)

    # else:
    #     context = {
    #         'form': form
    #     }
    #     return render(request, )
