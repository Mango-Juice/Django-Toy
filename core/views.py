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
            return render(request, 'index.html')

        context = {
            "id": num,
            "title": tmp[0]["title"],
            "describe": tmp[0]["describe"],
          }

    return render(request, 'invited.html', context)


@csrf_exempt
def test(request):
    return render(request, 'inviting.html')
