from ipware.ip import get_ip
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ajax_views.decorators import ajax_view
from .models import RatingVote


@csrf_exempt
@require_POST
@ajax_view('rating.vote')
def voting(request, *args, **kwargs):
    client_ip = get_ip(request)

    try:
        value = int(request.POST.get('rating', 5))
    except (TypeError, ValueError):
        value = 5

    # проверка границ
    if value < 1 or value > 5:
        value = 5

    try:
        vote, created = RatingVote.objects.get_or_create(
            ip=client_ip,
            defaults={
                'rating': value
            }
        )
    except RatingVote.MultipleObjectsReturned:
        vote = RatingVote.objects.filter(ip=client_ip).first()

    return JsonResponse({
        'rating': vote.rating
    })
