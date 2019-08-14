from django.shortcuts import render

from pyladies.models import StoryPoint, Schedule, Publication, Resource, Partner


def base_view(request):
    story_points = StoryPoint.objects.all().order_by('date')
    return render(request, 'about.html', {'story_points': story_points})


def schedule_view(request):
    schedule = Schedule.objects.all().order_by('-date')
    return render(request, 'schedule.html', {'schedule': schedule})


def publication_view(request):
    publications = Publication.objects.all().order_by('-date')
    return render(request, 'publications.html', {'publications': publications})


def resource_view(request):
    resources = Resource.objects.all().order_by('-order_number')
    return render(request, 'resources.html', {'resources': resources})


def partner_view(request):
    partners = Publication.objects.all()
    return render(request, 'partners.html', {'partners': partners})

