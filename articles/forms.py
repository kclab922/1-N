from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    # 여기는 파이썬 코드를 사용해서 html을 구현하기 위한 공간이므로, 설정값들을 적을 수 없음. 
    # 그래서 메타라는 클래스를 하나 더 만들어서, 거기서 설정값들을 지정하는 것.
    class Meta:
        model = Article
        fields = '__all__'
