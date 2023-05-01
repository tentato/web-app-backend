from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.template import loader
from .models import Tab
from .models import Post
from .forms import ContactForm
from django.conf import settings

def tabs(request):
  mytabs = Tab.objects.all().values()
  template = loader.get_template('all_tabs.html')
  context = {
    'mytabs': mytabs,
  }
  return HttpResponse(template.render(context, request))

def tab_details(request, id):
    mytab = Tab.objects.get(id=id)
    template = loader.get_template('tab_details.html')
    context = {
    'mytab': mytab,
    }
    return HttpResponse(template.render(context, request))

def posts(request):
    myposts = Post.objects.all().values()
    template = loader.get_template('all_posts.html')
    context = {
    'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def post_details(request, id):
    mypost = Post.objects.get(id=id)
    template = loader.get_template('post_details.html')
    context = {
    'mypost': mypost,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL, from_email])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("main")
    return render(request, "email.html", {"form": form})


def testing(request):
  template = loader.get_template('test_template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))