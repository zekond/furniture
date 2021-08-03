from django.template import RequestContext
from django.shortcuts import render_to_response
from Seg.apps.main.models import Mattress, Youth, Diningroom, Bedroom, Livingroom, Category

def index_view(request):

    template = "home.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def contact_view(request):

    template = "contact.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def bedroom_view(request):
    bedroom = Bedroom.objects.all()
    template = "bedroom.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def bedroom2_view(request, num):
    youth_art = Bedroom.objects.filter(id=num)

    template = "youth_art.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def diningroom_view(request):
    diningroom = Diningroom.objects.all()
    template = "diningroom.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def diningroom2_view(request, num):
    youth_art = Diningroom.objects.filter(id=num)

    template = "youth_art.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def livingroom_view(request):
    livingroom = Livingroom.objects.all()
    template = "Livingroom.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def livingroom2_view(request, num):
    youth_art = Livingroom.objects.filter(id=num)

    template = "youth_art.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def mattress_view(request):
    mattres = Mattress.objects.all()
    template = "mattress.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def mattress2_view(request, num):
    youth_art = Mattress.objects.filter(id=num)

    template = "youth_art.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def youth_view(request):

    youth = Category.objects.all()
    template = "youth.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def youthc_view(request, num):
    youthc = Youth.objects.filter(youth_id=num)

    template = "youthc.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))

def youth_art_view(request, num):
    youth_art = Youth.objects.filter(id=num)

    template = "youth_art.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))
