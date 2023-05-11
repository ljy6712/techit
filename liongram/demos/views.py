from django.shortcuts import render
import random

# Create your views here.

def lotto(request):
    return render(request, 'lotto.html')

def lotto_result(request):
    lottos = list()
    game = request.GET.get('game', 1)
    pull_number = [index for index in range(1,46)]

    for _ in range(int(game)):
        lottos.append(random.sample(pull_number, 6))

    return render(request, 'lotto_result.html', {'lottos':lottos, 'game':game})