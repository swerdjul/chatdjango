from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import View

from .models import *
from .forms import *


def index(request):
    d_list = Dialog.objects.order_by('id')
    return render(request, 'dialogs/list.html', {'listd': d_list})


def det(request, arg):
    try:
        a = Dialog.objects.get(id=arg)
        d_list = Message.objects.order_by('id')
        last_message = Message.objects.order_by('-id')

    except:
        raise Http404("Диалог не найден")
    return render(request, 'dialogs/det.html', {'dialog': a, 'message': last_message})


def nmess(request, dialog_id):
    try:
        a = Dialog.objects.get(id=dialog_id)
    except:
        raise Http404("Диалог не найден")
    a.message_set.create(author_name=request.POST['name'], message_txt=request.POST['text'])

    # chats = Message.objects.filter(members__in=[request.user.id])
    # return render(request, 'dialogs/list.html', {'user_profile': request.user, 'chats': chats})

    return HttpResponseRedirect(reverse('dialogs:det', args=[a.id]))


def Login(request):
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dialogs/')
                else:
                    return HttpResponse("Авторизация не успешна")
            else:
                messages.error(request, 'Неправильный логин или пароль! Попробуй снова')
    else:
        form = Login_Form()
    return render(
        request,
        'login.html',
        {'login': form}
    )


def Register(request):
    if request.method == 'POST':
        user_form = Registration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/dialogs/')
    else:
        user_form = Registration()
        return render(
            request,
            'registration.html',
            {'user_form': user_form}
        )
