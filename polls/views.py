from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import loader  # 템플릿 가져오기 위해
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]  # 최근 데이터를 0~4까지 5개의 객체 가져와라
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')  # 템플릿 파일 가져옴 loader.get_template()
#     context = {  # 최근 문항 데이터를 사전 형식으로 저장
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


# def index(request):  # 인덱스 페이지
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)  # render(), loader 사용할 필요 없음


class IndexView(generic.ListView):
    template_name = 'polls/index.html'  # 생략하면 question_list.html이 디폴트(앱이름/모델이름_liat.html)
    context_object_name = 'latest_question_list'  # 기본 이름 재정의, 생략하면

    def get_queryset(self):  # 함수 재정의
        """최근 게시된 투표 5개 반환"""
        return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#     return HttpResponse("%s번 투표 상세 보기" % question_id)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)  # 한 행만 가져올 때는 get 가능, 다수일 때는 filter
#     except Question.DoesNotExist:
#         raise Http404("진행 중인 투표가 없습니다.")  # 404오류 일으키기, 사용자가 에러메시지를 수정할 수 있음 -> get_object_or_404로 대체
#     return render(request, 'polls/detail.html', {'question': question})


# def detail(request, question_id):  # 상세보기
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question  # 모델 지정
    template_name = 'polls/detail.html'  # 생략하면 question_detail.html이 디폴트(앱이름/모델이름_detail.html)


def vote(request, question_id):  # 투표하기
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=int(request.POST['choice']))
        # post 형식으로 접근, 'choice'로 전달되어오는 데이터(value가 choice.id인 int값 - int() 함수 적용)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "투표 항목을 선택하지 않았습니다."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터 처리가 성공하면, 항상 HttpRedirect를 반환하라
        # 이렇게 해야, 사용자가 돌아가기 버튼을 클릭해도 두번 게시되는 현상을 방지할 수 있음
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def results(request, question_id):
#     response = "%s번 투표 결과 보기"
#     return HttpResponse(response % question_id)


# def results(request, question_id):  # 결과보기
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
