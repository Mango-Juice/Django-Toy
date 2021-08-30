from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from core.models import Suggestion, Answer
from .forms import PostForm


@csrf_exempt
def get_post(request):
    context = {}

    if request.method == 'GET':
        num = request.GET['id']
        tmp = list(Suggestion.objects.filter(id=num).values())

        if len(tmp) == 0:
            return redirect('unknown')

        context = {
            "id": num,
            "title": tmp[0]["title"],
          }

    return render(request, 'result/invited.html', context)


@csrf_exempt
def test(request):
    context = {
        'form': PostForm()
    }
    return render(request, 'result/inviting.html', context)


@csrf_exempt
def pc(request):
    return render(request, 'errors/pc.html')


@csrf_exempt
def unknown(request):
    return render(request, 'errors/unknown.html')


@csrf_exempt
def result(request):
    context = {}

    if request.method == 'GET':
        num = request.GET['id']
        suggestion = Suggestion.objects.filter(id=num)[0]
        tmp = list(Answer.objects.filter(suggestion=suggestion).values())
        days = ["월", "화", "수", "목", "금", "토", "일"]
        result = [True] * 168
        content = ''
        last = False
        edit = False

        for i in tmp:
            for j, char in enumerate(i['data']):
                if char == 'F':
                    result[j] = False

        for idx, val in enumerate(result):
            if val and not last:
                content += '👉 {}요일 {}시 ~'.format(days[idx // 24], idx % 24)
                edit = True
            elif last and not val:
                content += ' {}요일 {}시\n'.format(days[idx // 24], idx % 24 + 1)
                edit = False
            last = val

        if edit:
            content += ' {}요일 {}시'.format(days[6], 24)

        context = {
            "title": suggestion.title,
            "content": content,
            "count": len(tmp)
          }

    return render(request, 'result/result.html', context)


@csrf_exempt
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.save()
            return render(request, 'result/link.html', {'id': str(data.id)})
    return redirect('unknown')


@csrf_exempt
def submit(request):
    if request.method == "POST":
        num = request.POST.get('id')

        status = ['T'] * 168
        content = dict(request.POST)
        dow = list(map(int, content['dow']))
        start = list(map(int, content['start']))
        fin = list(map(int, content['fin']))

        for i in range(len(dow)):
            day = dow[i] * 24

            if fin[i] <= start[i]:
                continue

            for j in range(day + start[i] - 1, day + fin[i]):
                if 0 <= j < 168:
                    status[j] = 'F'

        Answer.objects.create(suggestion=Suggestion.objects.filter(id=num)[0], data=''.join(status))
        return redirect('https://pytoy-cxkwi.run.goorm.io/core/result/?id='+str(num))
    return redirect('unknown')
