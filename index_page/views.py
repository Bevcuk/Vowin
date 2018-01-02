import datetime
import json as simplejson
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import context
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from blog.models import Post
from index_page.models import Image, TypeImage


def contact(request):
    return render(request, 'index_page/contact.html')


def about(request):
    return render(request, 'index_page/fotyou.html')


class GalleryView(TemplateView):
    context_object_name = 'home_list'
    template_name = 'index_page/gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        #context['gallery'] = Image.objects.filter(type_image=3)
        return context


def show_image(request, element_id):
    gallery = Image.objects.filter(type_image=element_id)
    return render(request, 'index_page/gallery.html', {'gallery': gallery})


class RoletuView(TemplateView):
    context_object_name = 'home_list'
    template_name = 'index_page/roletu.html'

    def get_context_data(self, **kwargs):
        context = super(RoletuView, self).get_context_data(**kwargs)
        return context


class DoorView(TemplateView):
    context_object_name = 'home_list'
    template_name = 'index_page/door.html'

    def get_context_data(self, **kwargs):
        context = super(DoorView, self).get_context_data(**kwargs)
        return context


class VorotaView(TemplateView):
    context_object_name = 'home_list'
    template_name = 'index_page/vorota.html'

    def get_context_data(self, **kwargs):
        context = super(VorotaView, self).get_context_data(**kwargs)
        return context


class IndexView(TemplateView):
    context_object_name = 'home_list'
    template_name = 'index_page/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()[:3]
        return context


def change_profil(request, element_id):
    if element_id == '0':
        html = render_to_string('profil_change.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '1':
        html = render_to_string('profil_change_rechau.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    return HttpResponse(json, content_type='application/json')


def change(request, element_id):
    if element_id == '1':
        html = render_to_string('change1.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '2':
        html = render_to_string('change2.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '3':
        html = render_to_string('change3.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '4':
        html = render_to_string('change4.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '5':
        html = render_to_string('change5.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '6':
        html = render_to_string('change7.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '7':
        html = render_to_string('change8.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '8':
        html = render_to_string('change9.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    if element_id == '10':
        html = render_to_string('change10.html')
        results = {'html': html}
        json = simplejson.dumps(results)
    return HttpResponse(json, content_type='application/json')


def send(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        text = request.POST['text']
        email_subject = 'Зворотній зв\'язок'
        email_body = "call me%s description: %s" % (phone, text)
        send_mail(email_subject, email_body, 'myemail@example.com', ['vowin.window@gmail.com'], fail_silently=False)
    else:
        return render_to_response('index_page/success.html')
    return render_to_response('index_page/success.html')
