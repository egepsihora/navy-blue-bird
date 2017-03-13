# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    contacts = {'city': 'г. Харьков',
                'street': 'ул. 23 Августа',
                'phone': '0 800 000 00 00'}

    return render(request, 'library/library.html',
                  {'contacts': contacts})
