from django.contrib import admin
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):  # 둘 다 가능한 방법
class ChoiceInline(admin.TabularInline):
    model = Choice  # 사용할 모델 지정
    extra = 3       # 선택 항목은 기본적으로 3개 준비


class QuestionAdmin(admin.ModelAdmin):          # 'ModelAdmin'을 상속받는 클래스 생성
    fieldsets = [                               # 필드 순서 변경
        (None, {'fields': ['question_text']}),
        ('날짜 정보', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 추가
    inlines = [ChoiceInline]
    list_filter = ['pub_date']           # 게시일자로 필터링
    search_fields = ['question_text']    # 질문 내용으로 검색


admin.site.register(Question, QuestionAdmin)  # 둘째 인자로 전달
# admin.site.register(Choice)  # 제거 !!

