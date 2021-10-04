from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(entered_at, leaved_at):
    if leaved_at is None:
        leaved_at = localtime()
    return leaved_at - entered_at


def format_duration(durationVisit):
    totalMinute, second = divmod(durationVisit.seconds, 60)
    hour, minute = divmod(totalMinute, 60)
    return (f"{hour}:{minute:02}:{second:02}")


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode).get()
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit.entered_at, visit.leaved_at)),
            'is_strange': is_visit_long(visit)
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
