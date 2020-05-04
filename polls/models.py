from django.db import models
from django.utils import timezone
import datetime


# models.Model을 상속받은 파생 클래스로 작성
class Question(models.Model):  # 질문 데이터
    question_text = models.CharField('질문 문구', max_length=200)
    pub_date = models.DateTimeField('게시 일자')  # 사람이 읽기 쉬운 형태를 지정

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'   # 최근 게시글순으로 정렬
    was_published_recently.boolean = True                   # 아이콘으로 출력
    was_published_recently.short_description = '최근 게시?'   # 표시되는 글 변경


class Choice(models.Model):  # 내용 데이터(선택할 값)
    # 외래키 지정, 속성에 부모가 누군지 지정(Question), 부모가 삭제되면 같이 삭제되라
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
