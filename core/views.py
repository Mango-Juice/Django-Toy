from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from core.models import Suggestion
from .forms import PostForm


@csrf_exempt
def get_post(request):
    context = {}

    if request.method == 'GET':
        num = request.GET['id']
        tmp = list(Suggestion.objects.filter(id=num).values())

        if len(tmp) == 0:
            # return redirect('unknown')
            return render(request, 'result/invited.html')

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
            # return redirect('unknown')
            return render(request, 'result/result.html')

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
