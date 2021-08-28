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
        tmp = list(Suggestion.objects.filter(id=num).values())

        if len(tmp) == 0:
            return redirect('unknown')

        context = {
            "id": num,
            "title": tmp[0]["title"],
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

            for j in range(day + start[i], day + fin[i]):
                status[j] = 'F'
        Answer.objects.create(suggestion=Suggestion.objects.filter(id=num)[0], data=status)
        return render(request, 'result/result.html', {'id': num})
    return redirect('unknown')
