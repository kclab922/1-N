from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    # 여기는 파이썬 코드를 사용해서 html을 구현하기 위한 공간이므로, 설정값들을 적을 수 없음. 
    # 그래서 메타라는 클래스를 하나 더 만들어서, 거기서 설정값들을 지정하는 것.
    class Meta:
        model = Article
        # Article이라는 클래스가 갖는 모든 설정값들을 출력해줘
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Comment라는 클래스가 갖는 설정값들 중 content만 출력해줘 
        # 방법1) fields: content만! 
        # 방법2) exclude: article 제외하고!

        # fields = ('content', )
        # 여기서 쉼표를 넣는 이유: 얘는 튜플(혹은 리스트 등과 같이 iterable한 객체)인데, 쉼표가 없으면 그냥 값이라고 인식해버림. 
        exclude = ('article', )