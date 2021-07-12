from django.shortcuts import render, redirect
from .models import Yongloc

# Create your views here.


def home(request):
    message = request.GET.get('message')
    jinsung = request.GET.get('jinsung')

    if message:
        md = Yongloc.objects.filter(model__icontains=message)
        nomd = ''
        search = ''
        if int(bool(md)) == 0:
            nomd = '일치하는 모델명이 없습니다.'
            search = '검색어 : '
        else:
            search = '검색어 : '
        return render(request, 'home.html', {'md': md, 'nm': nomd, 'message': message, 'search': search})

    if jinsung == 'jinsung3':
        return redirect('jinsung3')
    elif jinsung == 'DAJL':
        return redirect('동아장왼쪽')
    elif jinsung == 'DAJR':
        return redirect('동아장오른쪽')

    return render(request, 'home.html')


def dongajangL(request):
    message = request.GET.get('message')
    jinsung = request.GET.get('jinsung')

    dajl = Yongloc.objects.filter(loc0='동아장왼쪽')
    dajlB6 = dajl.get(loc1='B6')
    dajlK6 = dajl.get(loc1='K6')
    dajlK7 = dajl.get(loc1='K7')
    dajlK8 = dajl.get(loc1='K8')
    dajlK9 = dajl.get(loc1='K9')
    dajlK10 = dajl.get(loc1='K10')
    dajlK11 = dajl.get(loc1='K11')
    dajlK12 = dajl.get(loc1='K12')
    dajlK13 = dajl.get(loc1='K13')
    dajlK14 = dajl.get(loc1='K14')
    dajlK15 = dajl.get(loc1='K15')

    if message:
        md = Yongloc.objects.filter(model__icontains=message)
        nomd = ''
        search = ''

        if int(bool(md)) == 0:
            nomd = '일치하는 모델명이 없습니다.'
            search = '검색어 : '
        else:
            search = '검색어 : '
        return render(request, 'dongajangL.html', {'md': md, 'nm': nomd, 'message': message, 'search': search, 'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15})

    if jinsung == 'jinsung3':
        return redirect('jinsung3')
    elif jinsung == 'DAJL':
        return redirect('동아장왼쪽')
    elif jinsung == 'DAJR':
        return redirect('동아장오른쪽')
    return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15})


def dongajangR(request):
    message = request.GET.get('message')
    jinsung = request.GET.get('jinsung')

    dajr = Yongloc.objects.filter(loc0='동아장오른쪽')
    dajrL6 = dajr.get(loc1='L6')
    dajrL7 = dajr.get(loc1='L7')
    dajrL8 = dajr.get(loc1='L8')
    dajrL9 = dajr.get(loc1='L9')
    dajrL10 = dajr.get(loc1='L10')
    dajrL11 = dajr.get(loc1='L11')
    dajrL12 = dajr.get(loc1='L12')
    dajrL13 = dajr.get(loc1='L13')
    dajrL14 = dajr.get(loc1='L14')
    dajrL15 = dajr.get(loc1='L15')
    dajrU6 = dajr.get(loc1='U6')
    dajrU7 = dajr.get(loc1='U7')
    dajrU8 = dajr.get(loc1='U8')
    dajrU9 = dajr.get(loc1='U9')
    dajrU10 = dajr.get(loc1='U10')
    dajrU11 = dajr.get(loc1='U11')
    dajrU12 = dajr.get(loc1='U12')
    dajrU13 = dajr.get(loc1='U13')
    dajrU14 = dajr.get(loc1='U14')
    if message:
        md = Yongloc.objects.filter(model__icontains=message)
        nomd = ''
        search = ''

        if int(bool(md)) == 0:
            nomd = '일치하는 모델명이 없습니다.'
            search = '검색어 : '
        else:
            search = '검색어 : '
        return render(request, 'dongajangR.html', {'md': md, 'nm': nomd, 'message': message, 'search': search, 'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14})

    if jinsung == 'jinsung3':
        return redirect('jinsung3')
    elif jinsung == 'DAJL':
        return redirect('동아장왼쪽')
    elif jinsung == 'DAJR':
        return redirect('동아장오른쪽')
    return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14})


def dongajangLclick(request, mdname):
    message = request.GET.get('message')
    jinsung = request.GET.get('jinsung')

    dajl = Yongloc.objects.filter(loc0='동아장왼쪽')
    dajlB6 = dajl.get(loc1='B6')
    dajlK6 = dajl.get(loc1='K6')
    dajlK7 = dajl.get(loc1='K7')
    dajlK8 = dajl.get(loc1='K8')
    dajlK9 = dajl.get(loc1='K9')
    dajlK10 = dajl.get(loc1='K10')
    dajlK11 = dajl.get(loc1='K11')
    dajlK12 = dajl.get(loc1='K12')
    dajlK13 = dajl.get(loc1='K13')
    dajlK14 = dajl.get(loc1='K14')
    dajlK15 = dajl.get(loc1='K15')
    find = ''

    if mdname == dajlB6.model:
        findB6 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findB6': findB6})
    if mdname == dajlK6.model:
        findK6 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK6': findK6})
    if mdname == dajlK7.model:
        findK7 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK7': findK7})
    if mdname == dajlK8.model:
        findK8 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK8': findK8})
    if mdname == dajlK9.model:
        findK9 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK9': findK9})
    if mdname == dajlK10.model:
        findK10 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK10': findK10})
    if mdname == dajlK11.model:
        findK11 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK11': findK11})
    if mdname == dajlK12.model:
        findK12 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK12': findK12})
    if mdname == dajlK13.model:
        findK13 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK13': findK13})
    if mdname == dajlK14.model:
        findK14 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK14': findK14})
    if mdname == dajlK15.model:
        findK15 = 'background-color: lightpink;'
        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'findK15': findK15})

    if message:
        md = Yongloc.objects.filter(model__icontains=message)
        nomd = ''
        search = ''

        if int(bool(md)) == 0:
            nomd = '일치하는 모델명이 없습니다.'
            search = '검색어 : '
        else:
            search = '검색어 : '
        return render(request, 'dongajangL.html', {'md': md, 'nm': nomd, 'message': message, 'search': search, 'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15})

    if jinsung == 'jinsung3':
        return redirect('jinsung3')
    elif jinsung == 'DAJL':
        return redirect('동아장왼쪽')
    elif jinsung == 'DAJR':
        return redirect('동아장오른쪽')
    return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15})


def dongajangRclick(request, mdname):
    message = request.GET.get('message')
    jinsung = request.GET.get('jinsung')

    dajr = Yongloc.objects.filter(loc0='동아장오른쪽')
    dajrL6 = dajr.get(loc1='L6')
    dajrL7 = dajr.get(loc1='L7')
    dajrL8 = dajr.get(loc1='L8')
    dajrL9 = dajr.get(loc1='L9')
    dajrL10 = dajr.get(loc1='L10')
    dajrL11 = dajr.get(loc1='L11')
    dajrL12 = dajr.get(loc1='L12')
    dajrL13 = dajr.get(loc1='L13')
    dajrL14 = dajr.get(loc1='L14')
    dajrL15 = dajr.get(loc1='L15')
    dajrU6 = dajr.get(loc1='U6')
    dajrU7 = dajr.get(loc1='U7')
    dajrU8 = dajr.get(loc1='U8')
    dajrU9 = dajr.get(loc1='U9')
    dajrU10 = dajr.get(loc1='U10')
    dajrU11 = dajr.get(loc1='U11')
    dajrU12 = dajr.get(loc1='U12')
    dajrU13 = dajr.get(loc1='U13')
    dajrU14 = dajr.get(loc1='U14')
    find = ''

    if mdname == dajrL6.model:
        findL6 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL6': findL6})
    if mdname == dajrL6.model:
        findL6 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL6': findL6})
    if mdname == dajrL7.model:
        findL7 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL7': findL7})
    if mdname == dajrL8.model:
        findL8 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL8': findL8})
    if mdname == dajrL9.model:
        findL9 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL9': findL9})
    if mdname == dajrL10.model:
        findL10 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL10': findL10})
    if mdname == dajrL11.model:
        findL11 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL11': findL11})
    if mdname == dajrL12.model:
        findL12 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL12': findL12})
    if mdname == dajrL13.model:
        findL13 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL13': findL13})
    if mdname == dajrL14.model:
        findL14 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL14': findL14})
    if mdname == dajrL15.model:
        findL15 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findL15': findL15})
    if mdname == dajrU6.model:
        findU6 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU6': findU6})
    if mdname == dajrU7.model:
        findU7 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU7': findU7})
    if mdname == dajrU8.model:
        findU8 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU8': findU8})
    if mdname == dajrU9.model:
        findU9 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU9': findU9})
    if mdname == dajrU10.model:
        findU10 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU10': findU10})
    if mdname == dajrU11.model:
        findU11 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU11': findU11})
    if mdname == dajrU12.model:
        findU12 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU12': findU12})
    if mdname == dajrU13.model:
        findU13 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU13': findU13})
    if mdname == dajrU14.model:
        findU14 = 'background-color: lightpink;'
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'findU14': findU14})

    if message:
        md = Yongloc.objects.filter(model__icontains=message)
        nomd = ''
        search = ''

        if int(bool(md)) == 0:
            nomd = '일치하는 모델명이 없습니다.'
            search = '검색어 : '
        else:
            search = '검색어 : '
        return render(request, 'dongajangR.html', {'md': md, 'nm': nomd, 'message': message, 'search': search, 'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14})

    if jinsung == 'jinsung3':
        return redirect('jinsung3')
    elif jinsung == 'DAJL':
        return redirect('동아장왼쪽')
    elif jinsung == 'DAJR':
        return redirect('동아장오른쪽')
    return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14})


def editdajL(request):
    mdmdmd = Yongloc.objects.all()
    message = request.GET.get('message')
    jinsung = request.GET.get('jinsung')

    dajl = Yongloc.objects.filter(loc0='동아장왼쪽')
    dajlB6 = dajl.get(loc1='B6')
    dajlK6 = dajl.get(loc1='K6')
    dajlK7 = dajl.get(loc1='K7')
    dajlK8 = dajl.get(loc1='K8')
    dajlK9 = dajl.get(loc1='K9')
    dajlK10 = dajl.get(loc1='K10')
    dajlK11 = dajl.get(loc1='K11')
    dajlK12 = dajl.get(loc1='K12')
    dajlK13 = dajl.get(loc1='K13')
    dajlK14 = dajl.get(loc1='K14')
    dajlK15 = dajl.get(loc1='K15')

    if message:
        md = Yongloc.objects.filter(model__icontains=message)
        nomd = ''
        search = ''

        if int(bool(md)) == 0:
            nomd = '일치하는 모델명이 없습니다.'
            search = '검색어 : '
        else:
            search = '검색어 : '
        return render(request, 'dongajangL.html', {'md': md, 'nm': nomd, 'message': message, 'search': search, 'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15})

    if jinsung == 'jinsung3':
        return redirect('jinsung3')
    elif jinsung == 'DAJL':
        return redirect('동아장왼쪽')
    elif jinsung == 'DAJR':
        return redirect('동아장오른쪽')

    if request.method == 'POST':
        dajlB6.model = request.POST['B6']
        dajlB6.save()
        dajlK6.model = request.POST['K6']
        dajlK6.save()
        dajlK7.model = request.POST['K7']
        dajlK7.save()
        dajlK8.model = request.POST['K8']
        dajlK8.save()
        dajlK9.model = request.POST['K9']
        dajlK9.save()
        dajlK10.model = request.POST['K10']
        dajlK10.save()
        dajlK11.model = request.POST['K11']
        dajlK11.save()
        dajlK12.model = request.POST['K12']
        dajlK12.save()
        dajlK13.model = request.POST['K13']
        dajlK13.save()
        dajlK14.model = request.POST['K14']
        dajlK14.save()
        dajlK15.model = request.POST['K15']
        dajlK15.save()

        return render(request, 'dongajangL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15})
    return render(request, 'editdajL.html', {'B6': dajlB6, 'K6': dajlK6, 'K7': dajlK7, 'K8': dajlK8, 'K9': dajlK9, 'K10': dajlK10, 'K11': dajlK11, 'K12': dajlK12, 'K13': dajlK13, 'K14': dajlK14, 'K15': dajlK15, 'gg': mdmdmd})


def editdajR(request):
    mdmdmd = Yongloc.objects.all()
    message = request.GET.get('message')
    jinsung = request.GET.get('jinsung')

    dajr = Yongloc.objects.filter(loc0='동아장오른쪽')
    dajrL6 = dajr.get(loc1='L6')
    dajrL7 = dajr.get(loc1='L7')
    dajrL8 = dajr.get(loc1='L8')
    dajrL9 = dajr.get(loc1='L9')
    dajrL10 = dajr.get(loc1='L10')
    dajrL11 = dajr.get(loc1='L11')
    dajrL12 = dajr.get(loc1='L12')
    dajrL13 = dajr.get(loc1='L13')
    dajrL14 = dajr.get(loc1='L14')
    dajrL15 = dajr.get(loc1='L15')
    dajrU6 = dajr.get(loc1='U6')
    dajrU7 = dajr.get(loc1='U7')
    dajrU8 = dajr.get(loc1='U8')
    dajrU9 = dajr.get(loc1='U9')
    dajrU10 = dajr.get(loc1='U10')
    dajrU11 = dajr.get(loc1='U11')
    dajrU12 = dajr.get(loc1='U12')
    dajrU13 = dajr.get(loc1='U13')
    dajrU14 = dajr.get(loc1='U14')

    if message:
        md = Yongloc.objects.filter(model__icontains=message)
        nomd = ''
        search = ''

        if int(bool(md)) == 0:
            nomd = '일치하는 모델명이 없습니다.'
            search = '검색어 : '
        else:
            search = '검색어 : '
        return render(request, 'dongajangR.html', {'md': md, 'nm': nomd, 'message': message, 'search': search, 'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14})

    if jinsung == 'jinsung3':
        return redirect('jinsung3')
    elif jinsung == 'DAJL':
        return redirect('동아장왼쪽')
    elif jinsung == 'DAJR':
        return redirect('동아장오른쪽')

    if request.method == 'POST':
        dajr = Yongloc.objects.filter(loc0='동아장오른쪽')
        dajrL6.model = request.POST['L6']
        dajrL6.save()
        dajrL7.model = request.POST['L7']
        dajrL7.save()
        dajrL8.model = request.POST['L8']
        dajrL8.save()
        dajrL9.model = request.POST['L9']
        dajrL9.save()
        dajrL10.model = request.POST['L10']
        dajrL10.save()
        dajrL11.model = request.POST['L11']
        dajrL11.save()
        dajrL12.model = request.POST['L12']
        dajrL12.save()
        dajrL13.model = request.POST['L13']
        dajrL13.save()
        dajrL14.model = request.POST['L14']
        dajrL14.save()
        dajrL15.model = request.POST['L15']
        dajrL15.save()
        dajrU6.model = request.POST['U6']
        dajrU6.save()
        dajrU7.model = request.POST['U7']
        dajrU7.save()
        dajrU8.model = request.POST['U8']
        dajrU8.save()
        dajrU9.model = request.POST['U9']
        dajrU9.save()
        dajrU10.model = request.POST['U10']
        dajrU10.save()
        dajrU11.model = request.POST['U11']
        dajrU11.save()
        dajrU12.model = request.POST['U12']
        dajrU12.save()
        dajrU13.model = request.POST['U13']
        dajrU13.save()
        dajrU14.model = request.POST['U14']
        dajrU14.save()
        return render(request, 'dongajangR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14})
    return render(request, 'editdajR.html', {'L6': dajrL6, 'L7': dajrL7, 'L8': dajrL8, 'L9': dajrL9, 'L10': dajrL10, 'L11': dajrL11, 'L12': dajrL12, 'L13': dajrL13, 'L14': dajrL14, 'L15': dajrL15, 'U6': dajrU6, 'U7': dajrU7, 'U8': dajrU8, 'U9': dajrU9, 'U10': dajrU10, 'U11': dajrU11, 'U12': dajrU12, 'U13': dajrU13, 'U14': dajrU14, 'gg': mdmdmd})


#################################################################################
list_name = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'D0', 'D1', 'E0', 'E1', 'F0', 'F1', 'G0', 'G1', 'H0', 'H1', 'H2', 'H3', 'I0', 'I1',
             'J0', 'J1', 'K0', 'K1', 'L0', 'L1', 'M0', 'M1', 'N0', 'O0', 'P0', 'B1', 'B2', 'ez5', 'ez4', 'ez3', 'ez2', 'ez1', 'ezb1', 'dajl', 'dajr']

A0 = ['DC102P', 'DC103P', '116MLAMP', 'Q3', 'BT203TM', 'BT026TRM', 'BT150CST', '160CC', '405TC', '235TC', '205TC', '4309HDVP-C', 'RS2322P', '415MU3', 'ITVERSC01-001', '4308HDVP', '4000HDP', '1502WU', 'RS232 4P', 'SC01-001', 'S01-001', '4303TX', '4301HDP', '753DCU3', 'DC101P', 'DC204PU', 'G2', '407NEC LP', '122LAMP-WC', 'BT203RM', 'BT029TRM', '435TC', '625U3', 'RS232 2P', '854DCU3',
      '1611SPO', '535TC', 'X1 MINI(W)', 'X1 MINI(B)', '4302HDVP', '116LAMP', '120LAMP', '121LAMP-C', '415M U3', '236CPS(B)', '236CPS(W)']
A1 = ['PEG4806JT', 'E0C001', 'RD232S5', 'EOC204THD', 'EOS201THD', '4508HDP', '4504HDP', '04PRAID', '105NEC', '1617SP-10G', '1614SP-VPD', '1613SP-VP', '1614SP-VPD', '1613SP-VP', '1612SP', '342PL-TC', 'RS232WC', '1609SP', '1606SP-P', '1606SP', 'EOC7001', '1610SP', '1602SP', '1601SP', '10BCR', '504N', 'RS232SC30', 'RS232U30', '322TCC', '1615SP', '340PL', 'US485C01', '341PL-SC',
      '001HDGL', '04P RAID', 'EOC302POE', 'RS232-TC', 'US485C01', '1603SP', '323TCA']
B0 = ['3410RS4', '232RS16', '1405HD4K', '2002UHD4K', '1410HD4K', '2005UHD4K', '1415HD4K', '1403HD4K', '12020HD4K', '28018HD4K', '2005UHD4K', '010UHD4K', '050UHD4K', '2020UHD4K', '020UHD4K', 'SFP1G-LX-SM', '100UHD4K', '1010HDCA', '28018UHD8K', '28015UHD8K', '020UHD4K', '1005HDCA', '1003HDCA', '1002HDCA', '42485LP2 EX', '42485LP4 EX',
      '1420HD4K', 'DVI200', 'DVI015', 'SFP10G-SR', 'SFP1G-CP', '150UHD4K', '12015HD4K', 'EC232485 2P', '2010UHD4K', '015UHD4K', 'SC101', '1011HDCA', '030UHD4K', '28030UHD4K', '1430HD4K', '14015HD4K', '1402HD4K', '952EX OXFORD', 'SFP1GDT-SX-MM', '2003UHD4K', '20015UHD4K', '2001UHD4K', 'DVI030', '954LP EX']
B1 = ['803HVC EX', '334N-AP', 'INTEL25K EX', '201CA', '364DCP EX', '111TCE', '201PL EX', '362DCP EX', 'RGB300', '1200AC', '361DCP EX', '1284PL', '1394VT EX', '1394TI', '551CP-10G', '540CP-10G', '110EA', 'RGB050', 'RGB020',
      '462DCP EX', '542SFP-10G', '220UL', '360DCP EX', '3100K EX', 'RGB100', '351SFP-1G', '1100U3', 'POE2302EX4', 'RGB150', '915V3', '550CP-10G', '210CA', '561SFP-10G', 'RGB200', '1202AC-AP']
C0 = ['2002SFP-10G', 'P0E201EX', 'POE2712MDT', 'POE2610MDT', 'POE2606MDT', 'POE13ST', 'POE19S', '200FSCSW40B', '200FSCSW40A', '2001POE-SFP', '2000GSCS-PW', '633DPT', '468LT', '911FT', '2000GSCSW-A', '2000GSCSW-B', 'POE706EF', '8501POE', 'POE4803JM', 'PSE4809AT', '868LTT', '2000G-SFP', '400PT', 'POE810F-2TP', '478PT',
      '200FSCSW-B', '200FSCSW-A', '858LT', 'POE202EX', '2008SFP-TP', 'POE201EX', '488PDT', 'POE4805JM', 'POE4807J-60W']
C1 = ['POE2002EXW', 'POE2001EXW', '300FSCS-POE', '300FSCM-POE', '3000SFP-POE', '300FSCSWA', '300FSCSWB', '3011SFP', 'POE1528GDT', 'POE524FDT', 'POE3004PD', 'POE3004PD-60', 'POE516FDT-B', 'PO516FDT-A', 'POE514FDT', 'POE2708AU-240', 'POE2812AU', 'POE306EF', 'P0E1524GDT', '3022SFP', 'PE844H', 'HTB515', 'POE1528GDT', 'PE4804J',
      'POE332SFP-TP', 'POE3108UL2-SFP', 'POE505F', 'POE1001EX']
D0 = ['7322HVC-4K', '7324HVC-4K', '7160KVM EX', '142VW', '2202HDM', '4150VE', '1021VFC', 'HD140TX-4K', 'HD141RX-4K', 'HD40SP-4R', 'HD60CAP-4K ', '2405UD-4K', '2404UHDM', '2403UHM', '1023DFC', '1025SFC', '1030VFC-KVM', '1029DFC-KVM', '1028HF-KVM', 'HD50POC-4K60', '7102VM-4K', '7460KVM EX', '7402KVM-DUAL', '2212UHD4K', '4401SLS', '1008SP4K', '1026HFC-KVM', '4244HDM',
      '7104KVM EX', '2403UHDM', '1022HFC', '4248UHDM', 'HD150POC-4K60', '4245HDM', '1027HFC-4K60']
D1 = ['NBS2315', '0301SWC4K', '2508VSP', '104DVI', '102DVl', 'HD100RS-4K', 'HD070IR', '2418VHC', '2417HVC-MR', '2102SDHC', '2218VDHP', '400HDW-R', '2217HDAV', '030IR', '310HST', '60HDC', '2416HVC-MN', '400HDW', '2602HDSC', '1608AHD', '502SK4K', '2101SDHC',
      'HD70RS-4K', 'SDI0102SP', '502SP4K', '512SP4K', '514SP4K', 'SDI0104SP']
E0 = ['QTC14PPS', '312DPVU3', '3222SPW4K', '3512SW4K', 'AV2308', 'AV2306', 'QC623GAN', 'QTC614PPS', '470HDCR', '470HDC', 'MOH360A(W)', 'MOH360A(B)', '112CMDP', '2425VDC', '2424DVC', '170HDCR', '2436BNC', '2245CHPD', '2435DP', '2434UTP', '2433TL', '3403SW4K', '2431ST', '5030TC', '2432USB', '313DPHU3', '2423VHC', '313DPHU3', '2232TCV', '2231TCH', '170HDC', '2252TCHV',
      '2246CHPD', '3405SW4K', '2233TCD', '326TCH-DX', '3412SW4K', '2251TCH', '2421HVC']
E1 = ['UH404LAN', '1102ND-MST', '335TC-PD', '3376TCH-DUAL', 'QTC612P', '1567QTC', 'USB190', '1429CH', '1410WC-C', '32QWC', '5060TG', '495UCG', '9708U3', '1565QMC', 'USB105PW', '707UHP', '35QTC', '331TC-PD', 'USB100', '14AC', '717UH', '414U3',
      '33QWC(B)', '503OTG', '415TC', '703U3NP', '704UH', '1568QLC', 'USB60', '1573LMM', '31WC-B', 'USB404']
F0 = ['008TC-5P', '715TC', '1005GH IGMP', 'DPHV02', '602SP4K60', '104BT', '1535L8', '1546C', 'K380BT', '1407CHG', '1406CHG', '1404CHG', 'QTC601', 'QTC603', '001TC', '006TC-4P', '5000PB(B)', '5000PB(W)', 'QTC601', '007TC-PD', 'K381P', '1008GH IGMP', '04AC-AP', '402SPC4K60', '1408QTC', 'DP102VS', 'DL303U3D PLUS', '204BT', 'HD301SWC4K', 'QTC613', '1403CHG', '10WC-PB(B)', '10WC-PB(W)', '3422BTC', '1413CHG', 'QTC605', '403SWC4K60', '8004FSC', '118WC-PD', '6003HW-PB', '1422BTC', '1545L8',
      '10007QPB', '005TC', '035RHD4K', '5005PBCB', '4202SPC4K', '2422BTC', '4202SPC4K', '5005PBCB', 'DVI202SW', '04AC', 'IDE JENDER', '10006TQPB', '20001QPB', '04AC-4P']
F1 = ['MTV302', '280S3', '412TCV', '8602TU3', '8603TCU3', '416TCH-DX', 'BT23CSM', 'BT20CST', '300N MINI', '501AC', 'MQP-N1(M)', 'MQP-N1(N)', 'MQP-N1(W)', 'TB13CS', 'BT17CS', 'BT18CS', '1302WBTA', 'BT13CS', '416TCH-DX', '820A', '316TCH-PD', '9718U3', '411TCH', '9720TC-OTG', '318TCH-PD', 'M2280C5', '413TCH-DX', '240PSE', 'MTV340-4K', '840A', 'MTV310', '531WBT', 'MTV330-4K', '486TC', '2420HDP', '202N MINI',
      '9716TC-PD', '317TCH', '2244TCH', '9713TCU3', '8601U3', '9714TC', '2244TCH', '120PSE', '9717U2', '830A', '9712TC', '1300WBT', '9715TC-PD', 'BT22CSA', '8600CR', '9721TC', 'MTV320']
G0 = ['515TC', 'TCA05EX', 'TCC05EX', '330TC', '329TC', '328TC', '518SATA', '218SATA', 'M2281C', 'RJ456C', 'M2284NVME', '315UH', 'JUD480', '505UH', 'JUH377', '218SATAIDE NEW', 'RJ45', '518U3 SATAIDE', 'TCA03EX', 'TCC03EX', '505UHP', 'JCA153',
      'JCA366', 'JEE256', 'JVCU100', '510UHP', '614U3', 'M 2281C', 'M2285U3', 'JCD543', 'JCA141', '214UH', 'UH104G', 'JCD381', '616TC', 'JCA379', '615TC']
G1 = ['JUA250', 'JUCX01', 'JDA159', 'JUC500', 'JUA365', 'JUC500', 'JUC100', 'JUA350',
      'JUCX10', 'JCH377', 'JDA112', 'JUE130', 'JUA254', 'JUC501', 'JTCX02', 'JDA134', 'JUC700']
H0 = ['1586U2-MC', '1587U2-MC', '1588U2-MC', '1590U3-MB', '1591U3-MB', '1595U3-M5', '1594U3-AB', '1593U3-AB', '1592U3-MB', '1581U2-AB', '1580U2-AB', '1570HD-MF', '1571HD-MF', '1570HD MF', '1531L', '1532C', '1577USM5', '1530M', '1528LCMD', '2241TCH-WHITE', '2241TCH-BLACK', 'BT50GST', '1525L', '1533CC', '1512TC', '1521',
      'KVMPS2', '115CDP', '1513TC', '1516TC', 'PS2', '120TLC', '1517TC', '2412VHC', '2243TCV', '2411HVC', '1524M']
H1 = ['SFP25G-LR', 'LL305MM-10G', 'LL310MM-10G', '2242TCD', 'LL203SM', 'LS203MM', 'LS201MM', 'LS203SM', 'SS203SM', 'LL203MM',
      '1518OTG-TC', 'LS330MM-10G', '1201AC', 'SS203MM', '1529LCMD', '1003M', 'LL201MM', 'LL201SM', 'LN00-QC3C']
H2 = ['4422BTC', '204UH NEW', 'LL205SM', 'LS210SM', 'LL220SM', 'LS220SM', 'SS230SM', 'LL250MM', 'LL220MM',
      'SS230MM', 'LS230MM', 'SS220MM', 'SPT2015SM', 'LS230SM', 'LL210SM', 'SS205MM', 'SS250SM']
H3 = ['1656DVI-FM', '1656DVI-FM', 'DPAS01D-00', 'SER6437AL-C', 'SER6437A', 'IPC-E2108S-B', 'lPC-E3204S-B', 'DPAS02H-00', 'DPH2001-D5', 'DPH3000-D4', 'DPAS08H-00', 'D2H23HD', 'C2HC3MO', 'C2VC7AO', '1645STC', '1646STC-FF', 'D2H13D', '1649HD-FM', '1643STC-Y', '1642STC-Y', 'IPC-E3204S-B', '1651HDVI-MF', '1655VGA-FF', '1653RJC', 'DPA301D-00(5V1A허)', 'IPC-E2202SL-C', 'DPAS04H-00', 'DPA301D-00', '1652HDVI-FM', '1650HD-FF',
      '1547ST-MF', 'IPC-E2204S-B', '1542ST-MF', '1541ST-MF', '1554ST-MM', 'D2H13MD', 'UPD2018-B', '1543ST-MF', '1648PS2', '1647OTG', '1569-3RC', '1585ST-2RC']
I0 = ['766FP', '1429FAN', '651DCU3HUB''656CCU3', '353C', '412U3', '963DU3H', '962DU3', '10MM', '659CCU3', '35HR', '351TCU3', '110LAMP', '350U3', '05AC', '7004N', '525U3', '651DCU3 HUB',
      '652DCU3', 'QC602', '8004N', '318U3', '418U3', '108LAMP', '650TC', '352U3', '109LAMP']
I1 = ['618DEU3', '203DVDRW-TC', '645U3', '804U3 RAID', '704TC', '852DCU3', '852DCU3', '962DCU3', '215U3', '200DVD-RW', '802U3 RAID', '101DVD-RW', '201DVD-COMBO', '200DVD-RW', '425U3',
      '100DVD-RW', '965TC', '952DCU3', '706M 6G', '702U3 RAID', '963DCU3H', '964DCU3C', '702TC RAID', '954DCU3', '644DU3', '706M6G', '802TC RAID', '110LAMP']
J0 = ['2024GS', 'AX1800MT', 'SFP-40G-DAC03', 'SFP-10G-DAC03', '7122KVM EX', 'USB10U3', '1019GSFP', '1SERIAL EX', 'SFP10G-DAC03', 'SFP10G-DAC01', '405NEC LP', '220V', '1204AC-AP', '2SERIAL EX', '101DVD-COMBO', 'USB05', '9703U3', 'SL602 PCle', '1024GS', '1016GS', 'USB10(B)', '1serial EX', '1026GSFP',
      'RS232U20', 'USB20', 'USB15', 'SL601 PCIE', 'RS232U20', '890AP-10K(+POE2403JM)', '305NEC EX', '1025GS IGMP', '200HCS', '206NEC EX', '212U3']

J1 = ['USB40U3 PW', 'USB05U3 PW', 'USB20U3(B)', '6005GH-IGMP', '8305SH', '675PB PRO', 'UH103AN', '707U3P', '314UH', '707U3', 'USB30PW', 'USB30U3', '408PB-UPS', 'UH303LAN', 'UH103LAN', '2000GSCM', '2016GS', '2000GSCS', '200FSCS', '6008GH', '6008GH-IGMP', '2200GU3', '2200GTC', 'USB05U3NP', '306UHP',
      'USB05 PLUS', 'UH305', 'UH308', '704U3', 'USB10U3PW', 'USB05U3NP', 'UH309PD', '208PB-UPS', '200FSCS', '314UHP', '964DCU3', '2024GS', '6005GH', '200FSCM', '8408SH', '316U3', '319U3', '704UHP']
K0 = ['N300VE', 'N80VE', 'N100VE', 'HD116SP4K', '722HC-KVM 4K', '0102SP4K', '0102SP4K', '3502PST', '1405CHB', '1411CHB', 'QTC604NB', '1402CHB', '7008KVM-4K', '7016KVM-4K', '7216KVM-4K', '7002KVM-4K', '7004KVM-4K', '2516VSP', '0102SPC4K', '7018KVM-KP', '100HDC', '122SDHC', '124HSDC', '2216VHC', '2215HVC', '405SW4K60', 'HD102SP4K', '402SP4K60', '2404VSW',
      '2216VHC', '622HC-KVM', '100HDCR', '7202KVM-4K', '2302VSP', '7014KVM-KP', '100HDCR', 'HD310SW4K', '404SP4K60', '2402VSW', '7012KVM-4K-PK', '0501SW4K', '2502VSP', '2304VSP', '7208KVM']
K1 = ['0104SP4K', '47QTC', '2415HVC', '408SP4K60', '2504VSP', 'HD301SW4K', 'HD501SW4K', 'HD104SP4K', '402SP4K60', '404SP4K60', '7008KVM', '37QTC', '07AC', '3504PST', '7012KVM-KP',
      'HD108SP4K', '7204KVM-4K', '07AC', 'N200VE', '7102KVM-4K',  '0226SP', '632DC-KVM', '612VC-KVM']
L0 = ['237AIR', '330UHD4K', 'POE605F', 'POE608F', 'POE2418LED-PM',
      'POE310F-21P', 'POE4012L2-SFP', '1G POE1005', '340UHD4K60']
L1 = ['POE808FP']
M0 = ['1102ND-MST', '2274TCH-4K']
M1 = ['CAM1080A', '1000K EX', '1000K LP', 'TC343LAN', 'TC313LAN', '1101TC', '1900AC', '2005GH', '7602KVM-K(B)', '7602KVM-K(W)', '3422U3-10G', '1305AC-AT', '1650AC-AT', '8060UHD-4K', '3506PST', '2271TCH-4K', 'M2287TCH', '306PST', 'QTC611', '8100UH-4K', '8120UHD-4K', 'AV2307',
      'AV2303', 'AV2302', 'AV2301', 'QTC607PD', '409LU3', 'SWP3500', 'M2286-COMBO', '2261TCH', '513OTG', '1301DS-PD', '325GEN32', '311TCH', 'POE3304EX4', 'POE3101EX', 'POE3102EX4', '3102D EX', 'POE3201EX4', 'POE3202EX4', 'POE3204EX4', '220TC', '2500K', '2502GTC', '2501GU3']
N0 = []
O0 = ['BT1150T', '2279TCH-PD', '2272TCH-PD',
      'M2289 NVME-G32', 'M2288DCU3', '338TC', '448TC']
P0 = ['4052L3-10G', 'POE528TP-COMBO', '3028GL2-SFP', 'POE320SFP-PD', '3110GL2-SFP', '3029GL2-10G', 'POE3008GFJ1', 'POE328SFP-PD', '3029GL2-10G',
      '2052GL2-10G', '1018GS IGMP', 'POE510-TP', '1018GS IGMP', 'POE4808J-95W', 'POE7006SFP-TP', 'POE327SFP-TP', 'POE324SFP-TP']

JB1 = ['0102SP4K', '0102SPC4K', '0104SP4K', '0301SW4K', '0501SW4K', '05AC', '1000K EX', '1000K LP', '100DVD-RW', '100HDC', '1016GS', '1018GS-IGMP', '1019G-SFP', '101DVD-COMBO', '1024GS', '1026GSFP', '104BT', '1422BTC', '1SERIAL EX', '2016GS', '2024GS', '203DVDRW-TC', '204BT', '208PB-UPS', '215U3', '218SATA NEW', '225SSD', '2402VSW', '2404VSW', '2422BTC', '2SERIAL EX', '304BT', '305NEC EX', '315UH', '316U3', '319U3', '340PL', '3422BTC', '3502PST', '3504PST', '350U3', '35HR', '408PB-UPS', '415MU3', '425U3', '504N', '518U3', '525U3', '6005GH', '6005GH IGMP', '6008GH', '6008GH IGMP', '652DCU3', '675PB', '702U3 RAID', '704U3', '704UHP', '706M6G', '707U3', '8408SH', '852DCU3', '9703U3', 'BT150CST', 'MTV302', 'MTV320', 'MTV330-4K', 'MTV340-4K', 'QC602', 'RS232U20', 'UH305', 'UH308', 'USB05', 'USB05PLUS', 'USB05U3NP', 'USB05U3PW', 'USB10', 'USB10U3', 'USB15', 'USB20',
       ]
JB2 = []

EZ5 = ['125LAMP-WC', '0226SP', '200HCS', '4150VE', '854LP', '915V3', '954LP EX', '958LP EX',
       'EC232485 2P', 'EC232485 4P', 'FC232485 CM', 'FC232485 CS', 'RJ45', 'RJ45C6', 'SC101', ]
EZ4 = ['9721TC', '101PL', '1284PL', '1301DS-PD', '1394VT EX', '1SERIAL LP', '201PL EX', '206NEC EX', '212U3', '2212UHD4K', '2218VDHP', '2420HDP', '2431ST', '2432USB', '2433TL', '2434UTP', '2435DP', '2436BNC', '2SERIAL LP', '3102D EX', '322TCC', '323TCA', '341PL-SC', '342PL-TC', '3506PST', '351SFP-1G', '352SFP-1G', '360DCP EX', '361DCP EX', '362DCP EX', '405NEC LP', '407NEC LP', '462DCP EX', '540CP-10G', '541SFP-10G', '550CP-10G', '561SFP', '562SFP-10G', '612VC-KVM', '622HC-KVM', '632DC-KVM', '722HC-KVM4K', '7322HVC-4K', '7324HVC-4K', '7326HVC-4K',
       '803HVC EX', '805HVC4K EX', '8100UHD-4K', '8120UHD-4K', '8330HVC-4K60', '9708U3', '9712TC', '9713TCU3', '9714TC', '9715TC-PD', '9716TC-PD', '9717U2', '9718U3', '9719TC-OTG', '9720TC-OTG', 'AV2301', 'AV2303', 'AV2304', 'AV2305', 'AV2306', 'AV2307', 'HD60CAP-4K', 'IDE JENDER', 'KVMPS2', 'M2280C5', 'M2281C', 'M2285U3', 'M2286-COMBO', 'M2288DCU3', 'M2289NVME-32', 'POE3204EX4', 'PS2', 'RS201SW', 'RS232 2P', 'RS232 4P', 'RS232 SC', 'RS232 TC', 'RS232 WC', 'RS232S5', 'RS232SC30', 'RS232U30', 'SL601PCIE', 'SL602PCIE', 'TC1701W-PD', 'TC1702W-PD', 'US485C01', ]
EZ3 = ['1100CA', '1100U3', '1101TC', '110EA', '111TCE', '1200AC', '1201AC', '1300WBT', '1302WBTA', '1305AC-AT', '1650AC-AT', '1900AC', '204UH', '210CA', '214UH', '2200GTC', '2200GU3', '220TC', '220UL', '2279TCH-PD', '300N', '306UHP', '312DPVU3', '313DPHU3', '314UH', '314UHP', '316TCH-PD', '325GEN32', '326TCH-DX', '328TC', '329TC', '330TC', '331TC-PD', '334N-AP', '335TC-PD', '3422U3-10G', '406JC', '409LU3', '413TCH-DX', '414U3', '415TC', '468LT', '478PT', '488PDT', '501AC', '503OTG', '505UHP',
       '506OTG', '510UHP', '513OTG', '515TC', '531WBT', '703U3NP', '704UH', '707UHP', '715TC', '717UH', '8501POE', '858LT', '8600CR', '8601POE', '8601U3', '8602TU3', '8603TCU3', '868LTT', '870AP-2K', '890AP-10G', '911FT', 'G2', 'Q3', 'TC313LAN', 'TC343LAN', 'TC414LAN', 'TCA03EX', 'TCA05EX', 'TCC03EX', 'TCC05EX', 'UH103LAN', 'UH104G', 'UH303LAN', 'UH309PD', 'UH404LAN', 'USB105', 'USB105PW', 'USB10P', 'USB15U3', 'USB190', 'USB20U3', 'USB30PW', 'USB30U3', 'USB404', 'USB40U3PW', 'USB60', 'X1', ]
EZ2 = ['644DCU3', '07AC', '04AC-4P', '10006TQPB', '10007QPB', '10WC-PB', '118WC-PD', '1403CHG', '1406CHG', '1407CHG', '1408QTC', '1413CHG', '1429CH', '14AC', '1512TC', '1513TC', '1514TC', '1516TC', '1517TC', '1521TM', '1522KLM', '1523KCM', '1524M', '1525L', '1526C', '1527LM', '1528LCMD', '1530M', '1531L', '1533CC', '1535L8', '1545C8', '1565QMC', '1573LMM', '20001QPB', '205TC', '235TC', '280S3', '32QWC', '338TC', '33QWC', '351TCU3', '352U3', '353C', '35QTC', '37QTC', '405TC', '412U3',
       '418U3', '435TC', '4422BTC', '448TC', '47QTC', '486TC', '5000PB', '5005PBCB', '535TC', '6003HW-PB', '618DEU3', '625U3', '650TC', '651DCU3HUB', '659CCU3', '702TC', '753DCU3', '766FP', '8004FSC', '802TC', '802U3', '804U3', '820A', '840A', '854DCU3', '952DCU3', '954DCU3', '962DCU3', '963DCU3H', '964DCU3C', '965TC', 'BT026TRM', 'BT029TRM', 'BT203RM', 'BT20CST', 'BT22CSA', 'BT50GST', 'K380BT', 'QC623GAN', 'QTC601', 'QTC603', 'QTC604NB', 'QTC605', 'QTC607PD', 'QTC612P', 'QTC613', 'SWP3500', ]
EZ1 = ['2000GSCM', '2000GSCS', '2000GSCS-PW', '2000GSCSW-A', '2000GSCSW-B', '2000G-SFP', '200FSCM', '200FSCS', '200FSCSW-A', '200FSCSW-B', '3024GL2-SFP', '3028GL2-SFP', '3029GL2-10G', '3034GL2-SFP', '3110GL2-SFP', '4000MG', '4008MCS', '57QWC', '7302KVM-DVI', '7304KVM-DVI', 'HTB515', 'MS1303N', 'MS1308M', 'NBS2315', 'PE4804J', 'PE844H', 'PEG4806JT', 'POE1005', 'POE1008', 'POE1616FG', 'POE1620L2-300', 'POE1720L2-250', 'POE19ST', 'POE2067EXW', 'POE2418LED-PM', 'POE2424SFP-380', 'POE2428LED-PM', 'POE2429L2-370', 'POE2430L2-380', 'POE3004PD', 'POE3005GF',
       'POE3008GF', 'POE3010G-2TP', 'POE3018SFP-250', 'POE3020SFP', 'POE3026SFP-400', 'POE3042L2-10G', 'POE3052L2-10G', 'POE308SFP-TP V3', 'POE310F-2TP', 'POE316SFP-TP', 'POE318SFP-TP', 'POE320SFP-PD', 'POE324SFP-TP', 'POE327SFP-TP', 'POE328SFP-PD', 'POE332SFP-TP', 'POE4010L2-140', 'POE4012L2-SFP', 'POE4028L2S-TP', 'POE4128L2S-TP', 'POE4210L2S-TP', 'POE4803JM', 'POE4805JM', 'POE4808J-95W', 'POE505F', 'POE506-TP', 'POE528TP-COMBO', 'POE6005F', 'POE6006GF-60', 'POE6008F', 'POE605F', 'POE606F', 'POE608F', 'POE7006SFP-TP', 'POE808FP', 'PSE4809AT', 'QTC611', 'QTC614PPS', ]
EZ1T = ['1025GS IGMP', '1052SFP-10G', '2001POE-SFP', '2052GL2-10G', '236CPS', '2424DVC', '2425VDC', '2500K EX', '2501GU3', '2502GTC', '3000SFP-POE', '300FSCSWB-POE', '3022SFP', '4052L3-10G', '4301HDP', '4302HDVP', '4308HDVP', '4504HDP', '4508HDP', '4516HDP', '4604VPS-36V', '4608VPS-36V', '4616VPS-36V', '614U3', '615TC', '616TC',
        '7255GH', '7258GH', 'EOC302POE', 'HD150POC-4K60', 'NC02', 'POE1001EX', 'POE101EX', 'POE1524GDT', 'POE1528GDT', 'POE2001EXW', 'POE2002EXW', 'POE201EX', 'POE202EX', 'POE2403JM', 'POE2406AU-240', 'POE2708AU-240', 'POE2712MDT', 'POE2812AU-240', 'POE3108UL2-SFP', 'POE4807J-60W', 'POE515FDT-SCS', 'POE706EF', 'POE810F-2TP', ]
EZB1 = ['001HDGL', '0301SWC4K', '035RHD4K', '1008SP4K', '102DVI', '104DVI', '1102ND-MST', '112CMDP', '113CDP', '115CDP', '120TLC', '122SDHC', '124HSDC', '1608AHD', '170HDC', '170HDCR', '2202HDM', '2215HVC', '2216VHC', '2217HDAV', '2231TCH', '2232TCV', '2233TCD', '2241TCH', '2242TCD', '2243TCV', '2244TCH', '2246CHPD', '2251TCH', '2252TCHV', '2254TCDP', '2261TCH-DUAL', '2271TCH-4K', '2272TCH-PD', '2273TCH-4K', '2274TCH-4K', '2275TC2-4K', '2277TCH-4K', '2302VSP', '2304VSP', '2403UHDM', '2404UHDM', '2405UHD-4K', '2411HVC', '2412VHC', '2415HVC', '2416HVC-MN', '2417HVC-MR', '2418VHC', '2421HVC', '2423VHC', '2502VSP', '2504VSP', '2508VSP', '310HST', '311TCH', '317TCH', '318TCH-PD', '3222SPW4K', '3376TCH-DUAL', '3403SW4K', '3405SW4K', '3412SW4K', '3512SW4K', '400HDW', '400HDWR', '402SP4K60', '402SPC4K60',
        '403SW4K60', '403SWC4K60', '404SP4K60', '405SW4K60', '408SP4K60', '411TCH', '412TCV', '416TCH-DX', '4202SPC4K', '4244HDM', '4245HDM', '4248UHDM', '4288UHDM', '4401SLS', '4404SLS', '4405SMW', '470HDC', '502SP4K', '50HDC', '512SP4K', '514SP4K', '602SP4K60', '7002KVM-4K', '7004KVM-4K', '7008KVM-4K', '7012KVM-KP', '7014KVM-KP', '7016KVM-4K', '7018KVM-4K', '7026KVM-4K', '7102KVM-4K', '7104KVM', '7122KVM EX', '7160KVM EX', '7202KVM-4K', '7204KVM-4K', '7208KVM-4K', '7216KVM-4K', '7402KVM-DUAL', '7460KVM EX', '7502KVM-PIP', '7602KVM-4K', '8060UHD-4K', '902SP4K60', '904SP4K60', 'DL303U3D', 'DP102VS', 'DVI202SW', 'EOC7002', 'HD100RS-4K', 'HD102SP4K', 'HD104SP4K', 'HD108SP4K', 'HD116SP4K', 'HD301SW4K', 'HD301SWC4K', 'HD501SW4K', 'N100VE', 'N200VE', 'N300VE', 'N80VE', 'SDI0102SP', 'SDI0104SP', ]


DAJL = ['122LAMP-WC', '110LAMP', '116MLAMP', '1204AC-AP', '1402CHB', '1405CHB',
        '1410WC-C', '1411CHB', '1419FAN', '1421FAN(KP쏠)', '211LAMP-W', '5004N', '7004N', ]
DAJR = ['108LAMP', '109LAMP', '10BCR', '120LAMP', '121LAMP-C', '1412FAN',
        '1418FAN', '1428FAN-T(KP쏠)', '14GDP', '2005GH', 'BT15C', 'BT30CST', ]


def jinsung3(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultA0 = []
    resultA1 = []
    resultB0 = []
    resultB1 = []
    resultC0 = []
    resultC1 = []
    resultD0 = []
    resultD1 = []
    resultE0 = []
    resultE1 = []
    resultF0 = []
    resultF1 = []
    resultG0 = []
    resultG1 = []
    resultH0 = []
    resultH1 = []
    resultH2 = []
    resultH3 = []
    resultI0 = []
    resultI1 = []
    resultJ0 = []
    resultJ1 = []
    resultK0 = []
    resultK1 = []
    resultL0 = []
    resultL1 = []
    resultM0 = []
    resultM1 = []
    resultN0 = []
    resultO0 = []
    resultP0 = []

    strA0 = ''
    strA1 = ''
    strB0 = ''
    strB1 = ''
    strC0 = ''
    strC1 = ''
    strD0 = ''
    strD1 = ''
    strE0 = ''
    strE1 = ''
    strF0 = ''
    strF1 = ''
    strG0 = ''
    strG1 = ''
    strH0 = ''
    strH1 = ''
    strH2 = ''
    strH3 = ''
    strI0 = ''
    strI1 = ''
    strJ0 = ''
    strJ1 = ''
    strK0 = ''
    strK1 = ''
    strL0 = ''
    strL1 = ''
    strM0 = ''
    strM1 = ''
    strN0 = ''
    strO0 = ''
    strP0 = ''

    objectA0 = []
    objectA1 = []
    objectB0 = []
    objectB1 = []
    objectC0 = []
    objectC1 = []
    objectD0 = []
    objectD1 = []
    objectE0 = []
    objectE1 = []
    objectF0 = []
    objectF1 = []
    objectG0 = []
    objectG1 = []
    objectH0 = []
    objectH1 = []
    objectH2 = []
    objectH3 = []
    objectI0 = []
    objectI1 = []
    objectJ0 = []
    objectJ1 = []
    objectK0 = []
    objectK1 = []
    objectL0 = []
    objectL1 = []
    objectM0 = []
    objectM1 = []
    objectN0 = []
    objectO0 = []
    objectP0 = []

    if message:
        for itemA0 in A0:                   # for문으로 입력어가 포함된 품목 리스트에 담기
            if message.upper() in itemA0:
                resultA0.append(itemA0)
        for itemA1 in A1:
            if message.upper() in itemA1:
                resultA1.append(itemA1)
        for itemB0 in B0:
            if message.upper() in itemB0:
                resultB0.append(itemB0)
        for itemB1 in B1:
            if message.upper() in itemB1:
                resultB1.append(itemB1)
        for itemC0 in C0:
            if message.upper() in itemC0:
                resultC0.append(itemC0)
        for itemC1 in C1:
            if message.upper() in itemC1:
                resultC1.append(itemC1)
        for itemD0 in D0:
            if message.upper() in itemD0:
                resultD0.append(itemD0)
        for itemD1 in D1:
            if message.upper() in itemD1:
                resultD1.append(itemD1)
        for itemE0 in E0:
            if message.upper() in itemE0:
                resultE0.append(itemE0)
        for itemE1 in E1:
            if message.upper() in itemE1:
                resultE1.append(itemE1)
        for itemF0 in F0:
            if message.upper() in itemF0:
                resultF0.append(itemF0)
        for itemF1 in F1:
            if message.upper() in itemF1:
                resultF1.append(itemF1)
        for itemG0 in G0:
            if message.upper() in itemG0:
                resultG0.append(itemG0)
        for itemG1 in G1:
            if message.upper() in itemG1:
                resultG1.append(itemG1)
        for itemH0 in H0:
            if message.upper() in itemH0:
                resultH0.append(itemH0)
        for itemH1 in H1:
            if message.upper() in itemH1:
                resultH1.append(itemH1)
        for itemH2 in H2:
            if message.upper() in itemH2:
                resultH2.append(itemH2)
        for itemH3 in H3:
            if message.upper() in itemH3:
                resultH3.append(itemH3)
        for itemI0 in I0:
            if message.upper() in itemI0:
                resultI0.append(itemI0)
        for itemI1 in I1:
            if message.upper() in itemI1:
                resultI1.append(itemI1)
        for itemJ0 in J0:
            if message.upper() in itemJ0:
                resultJ0.append(itemJ0)
        for itemJ1 in J1:
            if message.upper() in itemJ1:
                resultJ1.append(itemJ1)
        for itemK0 in K0:
            if message.upper() in itemK0:
                resultK0.append(itemK0)
        for itemK1 in K1:
            if message.upper() in itemK1:
                resultK1.append(itemK1)
        for itemL0 in L0:
            if message.upper() in itemL0:
                resultL0.append(itemL0)
        for itemL1 in L1:
            if message.upper() in itemL1:
                resultL1.append(itemL1)
        for itemM0 in M0:
            if message.upper() in itemM0:
                resultM0.append(itemM0)
        for itemM1 in M1:
            if message.upper() in itemM1:
                resultM1.append(itemM1)
        for itemN0 in N0:
            if message.upper() in itemN0:
                resultN0.append(itemN0)
        for itemO0 in O0:
            if message.upper() in itemO0:
                resultO0.append(itemO0)
        for itemP0 in P0:
            if message.upper() in itemP0:
                resultP0.append(itemP0)

        if resultA0:
            strA0 = '♣'
            objectA0.append('A0 : ')
        if resultA1:
            strA1 = '♣'
            objectA1.append('A1 : ')
        if resultB0:
            strB0 = '♣'
            objectB0.append('B0 : ')
        if resultB1:
            strB1 = '♣'
            objectB1.append('B1 : ')
        if resultC0:
            strC0 = '♣'
            objectC0.append('C0 : ')
        if resultC1:
            strC1 = '♣'
            objectC1.append('C1 : ')
        if resultD0:
            strD0 = '♣'
            objectD0.append('D0 : ')
        if resultD1:
            strD1 = '♣'
            objectD1.append('D1 : ')
        if resultE0:
            strE0 = '♣'
            objectE0.append('E0 : ')
        if resultE1:
            strE1 = '♣'
            objectE1.append('E1 : ')
        if resultF0:
            strF0 = '♣'
            objectF0.append('F0 : ')
        if resultF1:
            strF1 = '♣'
            objectF1.append('F1 : ')
        if resultG0:
            strG0 = '♣'
            objectG0.append('G0 : ')
        if resultG1:
            strG1 = '♣'
            objectG1.append('G1 : ')
        if resultH0:
            strH0 = '♣'
            objectH0.append('H0 : ')
        if resultH1:
            strH1 = '♣'
            objectH1.append('H1 : ')
        if resultH2:
            strH2 = '♣'
            objectH2.append('H2 : ')
        if resultH3:
            strH3 = '♣'
            objectH1.append('H3 : ')
        if resultI0:
            strI0 = '♣'
            objectI0.append('I0 : ')
        if resultI1:
            strI1 = '♣'
            objectI1.append('I1 : ')
        if resultJ0:
            strJ0 = '♣'
            objectJ0.append('J0 : ')
        if resultJ1:
            strJ1 = '♣'
            objectJ1.append('J1 : ')
        if resultK0:
            strK0 = '♣'
            objectK0.append('K0 : ')
        if resultK1:
            strK1 = '♣'
            objectK1.append('K1 : ')
        if resultL0:
            strL0 = '♣'
            objectL0.append('L0 : ')
        if resultL1:
            strL1 = '♣'
            objectL1.append('L1 : ')
        if resultM0:
            strM0 = '♣'
            objectM0.append('M0 : ')
        if resultM1:
            strM1 = '♣'
            objectM1.append('M1 : ')
        if resultN0:
            strN0 = '♣'
            objectN0.append('N0 : ')
        if resultO0:
            strO0 = '♣'
            objectO0.append('O0 : ')
        if resultP0:
            strP0 = '♣'
            objectP0.append('P0 : ')

        if int(bool(resultA0))+int(bool(resultA1)) + int(bool(resultB0))+int(bool(resultB1))+int(bool(resultC0))+int(bool(resultC1))+int(bool(resultD0))+int(bool(resultD1))+int(bool(resultE0))+int(bool(resultE1))+int(bool(resultF0))+int(bool(resultF1))+int(bool(resultG0))+int(bool(resultG1))+int(bool(resultH0))+int(bool(resultH1))+int(bool(resultH2))+int(bool(resultH3))+int(bool(resultI0))+int(bool(resultI1))+int(bool(resultJ0))+int(bool(resultJ1))+int(bool(resultK0))+int(bool(resultK1))+int(bool(resultL0))+int(bool(resultL1))+int(bool(resultM0))+int(bool(resultM1))+int(bool(resultN0))+int(bool(resultO0))+int(bool(resultP0)) >= 1:
            return render(request, 'jinsung3.html', {'search': '검색어 : ', 'searchoj': message, 'searchsA0': objectA0, 'searchsA1': objectA1, 'searchsB0': objectB0, 'searchsB1': objectB1, 'searchsC0': objectC0, 'searchsC1': objectC1, 'searchsD0': objectD0, 'searchsD1': objectD1, 'searchsE0': objectE0, 'searchsE1': objectE1, 'searchsF0': objectF0, 'searchsF1': objectF1, 'searchsG0': objectG0, 'searchsG1': objectG1, 'searchsH0': objectH0, 'searchsH1': objectH1, 'searchsH2': objectH2, 'searchsH3': objectH3, 'searchsI0': objectI0, 'searchsI1': objectI1, 'searchsJ0': objectJ0, 'searchsJ1': objectJ1, 'searchsK0': objectK0, 'searchsK1': objectK1, 'searchsL0': objectL0, 'searchsL1': objectL1, 'searchsM0': objectM0, 'searchsM1': objectM1, 'searchsN0': objectN0, 'searchsO0': objectO0, 'searchsP0': objectP0, 'searchojsA0': resultA0, 'searchojsA1': resultA1, 'searchojsB0': resultB0, 'searchojsB1': resultB1, 'searchojsC0': resultC0, 'searchojsC1': resultC1, 'searchojsD0': resultD0, 'searchojsD1': resultD1, 'searchojsE0': resultE0, 'searchojsE1': resultE1, 'searchojsF0': resultF0, 'searchojsF1': resultF1, 'searchojsG0': resultG0, 'searchojsG1': resultG1, 'searchojsH0': resultH0, 'searchojsH1': resultH1, 'searchojsH2': resultH2, 'searchojsH3': resultH3, 'searchojsI0': resultI0, 'searchojsI1': resultI1, 'searchojsJ0': resultJ0, 'searchojsJ1': resultJ1, 'searchojsK0': resultK0, 'searchojsK1': resultK1, 'searchojsL0': resultL0, 'searchojsL1': resultL1, 'searchojsM0': resultM0, 'searchojsM1': resultM1, 'searchojsN0': resultN0, 'searchojsO0': resultO0, 'searchojsP0': resultP0, 'A0': strA0, 'A1': strA1, 'B0': strB0, 'B1': strB1, 'C0': strC0, 'C1': strC1, 'D0': strD0, 'D1': strD1, 'E0': strE0, 'E1': strE1, 'F0': strF0, 'F1': strF1, 'G0': strG0, 'G1': strG1, 'H0': strH0, 'H1': strH1, 'H2': strH2, 'H3': strH3, 'I0': strI0, 'I1': strI1, 'J0': strJ0, 'J1': strJ1, 'K0': strK0, 'K1': strK1, 'L0': strL0, 'L1': strL1, 'M0': strM0, 'M1': strM1, 'N0': strN0, 'O0': strO0, 'P0': strP0})
        else:
            return render(request, 'jinsung3.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'A0':
        return render(request, 'jinsung3.html', {'진성A0': '진성A0 : ', 'A0all': A0, 'A0': '♣'})
    elif info == 'A1':
        return render(request, 'jinsung3.html', {'진성A1': '진성A1 : ', 'A1all': A1, 'A1': '♣'})
    elif info == 'B0':
        return render(request, 'jinsung3.html', {'진성B0': '진성B0 : ', 'B0all': B0, 'B0': '♣'})
    elif info == 'B1':
        return render(request, 'jinsung3.html', {'진성B1': '진성B1 : ', 'B1all': B1, 'B1': '♣'})
    elif info == 'C0':
        return render(request, 'jinsung3.html', {'진성C0': '진성C0 : ', 'C0all': C0, 'C0': '♣'})
    elif info == 'C1':
        return render(request, 'jinsung3.html', {'진성C1': '진성C1 : ', 'C1all': C1, 'C1': '♣'})
    elif info == 'D0':
        return render(request, 'jinsung3.html', {'진성D0': '진성D0 : ', 'D0all': D0, 'D0': '♣'})
    elif info == 'D1':
        return render(request, 'jinsung3.html', {'진성D1': '진성D1 : ', 'D1all': D1, 'D1': '♣'})
    elif info == 'E0':
        return render(request, 'jinsung3.html', {'진성E0': '진성E0 : ', 'E0all': E0, 'E0': '♣'})
    elif info == 'E1':
        return render(request, 'jinsung3.html', {'진성E1': '진성E1 : ', 'E1all': E1, 'E1': '♣'})
    elif info == 'F0':
        return render(request, 'jinsung3.html', {'진성F0': '진성F0 : ', 'F0all': F0, 'F0': '♣'})
    elif info == 'F1':
        return render(request, 'jinsung3.html', {'진성F1': '진성F1 : ', 'F1all': F1, 'F1': '♣'})
    elif info == 'G0':
        return render(request, 'jinsung3.html', {'진성G0': '진성G0 : ', 'G0all': G0, 'G0': '♣'})
    elif info == 'G1':
        return render(request, 'jinsung3.html', {'진성G1': '진성G1 : ', 'G1all': G1, 'G1': '♣'})
    elif info == 'H0':
        return render(request, 'jinsung3.html', {'진성H0': '진성H0 : ', 'H0all': H0, 'H0': '♣'})
    elif info == 'H1':
        return render(request, 'jinsung3.html', {'진성H1': '진성H1 : ', 'H1all': H1, 'H1': '♣'})
    elif info == 'H2':
        return render(request, 'jinsung3.html', {'진성H2': '진성H2 : ', 'H2all': H2, 'H2': '♣'})
    elif info == 'H3':
        return render(request, 'jinsung3.html', {'진성H3': '진성H3 : ', 'H3all': H3, 'H3': '♣'})
    elif info == 'I0':
        return render(request, 'jinsung3.html', {'진성I0': '진성I0 : ', 'I0all': I0, 'I0': '♣'})
    elif info == 'I1':
        return render(request, 'jinsung3.html', {'진성I1': '진성I1 : ', 'I1all': I1, 'I1': '♣'})
    elif info == 'J0':
        return render(request, 'jinsung3.html', {'진성J0': '진성J0 : ', 'J0all': J0, 'J0': '♣'})
    elif info == 'J1':
        return render(request, 'jinsung3.html', {'진성J1': '진성J1 : ', 'J1all': J1, 'J1': '♣'})
    elif info == 'K0':
        return render(request, 'jinsung3.html', {'진성K0': '진성K0 : ', 'K0all': K0, 'K0': '♣'})
    elif info == 'K1':
        return render(request, 'jinsung3.html', {'진성K1': '진성K1 : ', 'K1all': K1, 'K1': '♣'})
    elif info == 'L0':
        return render(request, 'jinsung3.html', {'진성L0': '진성L0 : ', 'L0all': L0, 'L0': '♣'})
    elif info == 'L1':
        return render(request, 'jinsung3.html', {'진성L1': '진성L1 : ', 'L1all': L1, 'L1': '♣'})
    elif info == 'M0':
        return render(request, 'jinsung3.html', {'진성M0': '진성M0 : ', 'M0all': M0, 'M0': '♣'})
    elif info == 'M1':
        return render(request, 'jinsung3.html', {'진성M1': '진성M1 : ', 'M1all': M1, 'M1': '♣'})
    elif info == 'N0':
        return render(request, 'jinsung3.html', {'진성N0': '진성N0 : ', 'N0all': N0, 'N0': '♣'})
    elif info == 'O0':
        return render(request, 'jinsung3.html', {'진성O0': '진성O0 : ', 'O0all': O0, 'O0': '♣'})
    elif info == 'P0':
        return render(request, 'jinsung3.html', {'진성P0': '진성P0 : ', 'P0all': P0, 'P0': '♣'})

    return render(request, 'jinsung3.html')
