from django.shortcuts import render, redirect
from .models import Article, Comment
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

    # comment 목록 조회 방법 3가지

    # 첫번째 방법
    # 코멘트를 기준으로 코멘트를 찾는 것
    # 인스턴스를 직접 찾는 것이므로 article=article로 표기. 이 조건에 부합하는 애들만 필터링해서 찾는 것
    # comments = Comment.objects.filter(article=article)

    # 두번째 방법
    # 게시물을 기준으로 해당 게시물에 있는 코멘트를 찾는 것
    # 여기서 comment_set.() 은 장고 자체적으로 models.py에 클래스들에 자동으로 만들어지는 컬럼
    # 기준점을 article로 잡아서 예를 들어 1번 게시물로 잡고, 
    # 파이썬 세상에서 결과물을 도출하고 그것을 html로 연결
    # comments = article.comment_set.all()

    # 세번째 방법
    # HTML 코드에서 article.comment_set.all을 사용
    # HTML 코드에서 파이썬 코드를 실행

    context = {
        'article': article,
        'form': form,
        # 'comments': comments, (3번째 방법에서는 주석처리)
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


def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('articles:detail', id=article_id)