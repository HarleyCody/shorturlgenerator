from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import shortURL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwarfs):
        form = SubmitUrlForm()
        context = {
            "title": "ShortURL.com",
            "form": form,
        }
        return render(request, "shortner/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title" : "ShortURL.com",
            "form" : form
        }
        template = "shortner/home.html"
        if form.is_valid():
            print(form.cleaned_data.get("url"))
            url = form.cleaned_data.get("url")
            obj, created = shortURL.objects.get_or_create(url = url)
            context = {
                "object" : obj,
                "created" : created,
            }
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/already-exists.html"


        return render(request, template , context)

class URLRedirectView(View):
    def get(self, request, shorturl=None, *args, **kwargs):
        obj = get_object_or_404(shortURL, shorturl = shorturl)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse()