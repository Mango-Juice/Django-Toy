from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from core.models import Suggestion


@csrf_exempt
def get_post(request):
    context = {}

    if request.method == 'GET':
        num = request.GET['id']
        tmp = list(Suggestion.objects.filter(id=num).values())

        if len(tmp) == 0:
            return render(request, 'errors/unknown.html')

        context = {
            "id": num,
            "title": tmp[0]["title"],
            "describe": tmp[0]["describe"],
          }

    return render(request, 'result/invited.html', context)


@csrf_exempt
def test(request):
    return render(request, 'result/inviting.html')


@csrf_exempt
def error(request):
    return render(request, 'errors/pc.html')

@csrf_exempt
def result(request):
    return render(request, 'result/result.html')