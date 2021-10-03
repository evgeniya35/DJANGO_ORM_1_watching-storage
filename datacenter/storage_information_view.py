from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timedelta

def get_duration(timeVisit):
    return localtime() - timeVisit

def format_duration(durationVisit):
    totalMinute, second = divmod(durationVisit.seconds, 60)
    hour, minute = divmod(totalMinute, 60)
    return (f"{hour}ч {minute:02}мин {second:02}сек")

def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit.entered_at))
        })

#    non_closed_visits = [
#        {
#            'who_entered': 'Richard Shaw',
#            'entered_at': '11-04-2018 25:34',
#            'duration': '25:03',
#        }
#   ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
