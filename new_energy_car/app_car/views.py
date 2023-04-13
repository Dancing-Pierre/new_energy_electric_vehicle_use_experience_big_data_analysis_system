import re
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Avg
from .models import *
from .get_car_data import *


# Create your views here.
def login(request):
    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return render(request, 'login.html')


def do_login(request):
    """登录验证"""
    if request.method == 'POST':
        body = request.POST
        user_account = body.get('user_account')
        password = body.get('password')
        try:
            user = UserAccount.objects.get(user_account=user_account, password=password)
        except Exception as e:
            data = {'login_result': '账号或密码错误'}
            return render(request, 'login.html', data)
        return redirect('/car_list')


# 列表
def car_list(request):
    data = NewEnergyCar.objects.filter()
    return render(request, 'car_list.html', {'data': data})


def get_car_list(request):
    page = read_page()
    json_data = start_requests(page)
    data = parse_data(json_data)
    for rec in data:
        del rec['serie_id']
        del rec['energy_type']
        del rec['min_subsidy_price']
        del rec['max_subsidy_price']
        del rec['max_mix_energy_range']
        del rec['sale_status_sort']
        form1 = NewEnergyCar.objects.create(**rec)
        form1.save()
    data = NewEnergyCar.objects.filter().order_by('-id')
    return render(request, 'car_list.html', {'data': data})


@csrf_exempt
def car_price(request):
    context = {}
    return render(request, 'car_price.html', {'data': context})


def car_price_data(request):
    data = NewEnergyCar.objects.values_list('max_pure_energy_range').annotate(min_price=Avg('min_price'))
    context = {
        'car_data': [o[0] for o in data],
        'price_data': [o[1] for o in data],
    }
    return HttpResponse(json.dumps(context))


@csrf_exempt
def energy_range_min_price(request):
    context = {}
    return render(request, 'energy_range_min_price.html', {'data': context})


def energy_range_min_price_data(request):
    data = NewEnergyCar.objects.filter()
    serie_name = [re.sub('[a-zA-Z0-9]','', o.serie_name).replace(' ','').replace(':','')[:2] for o in data]
    serie_name = list(set(serie_name))
    serie_name = [o for o in serie_name if len(o)>1]
    series_data = []
    for rec in serie_name:
        line_data = [[o.max_pure_energy_range, o.min_price] for o in data if rec in o.serie_name]
        line = {
            'symbolSize': 6,
            'name': rec,
            'data': line_data,
            'type': 'scatter'
        }
        series_data.append(line)
    context = {
        'legend_data': serie_name,
        'series_data': series_data
    }
    print(context)
    return HttpResponse(json.dumps(context))


@csrf_exempt
def energy_range_max_price(request):
    context = {}
    return render(request, 'energy_range_max_price.html', {'data': context})


def energy_range_max_price_data(request):
    data = NewEnergyCar.objects.filter()
    serie_name = [re.sub('[a-zA-Z0-9]', '', o.serie_name).replace(' ', '').replace(':', '')[:2] for o in data]
    serie_name = list(set(serie_name))
    serie_name = [o for o in serie_name if len(o) > 1]
    series_data = []
    for rec in serie_name:
        line_data = [[o.max_pure_energy_range, o.max_price] for o in data if rec in o.serie_name]
        line = {
            'symbolSize': 6,
            'name': rec,
            'data': line_data,
            'type': 'scatter'
        }
        series_data.append(line)
    context = {
        'legend_data': serie_name,
        'series_data': series_data
    }
    print(context)
    return HttpResponse(json.dumps(context))


def car_subsidy(request):
    data = NewEnergyCar.objects.annotate(subsidy_amount=F('max_guide_price') - F('max_price')).filter(has_subsidy=1).order_by('-subsidy_amount')
    return render(request, 'car_subsidy.html', {'data': data})


@csrf_exempt
def car_price_bar(request):
    context = {}
    return render(request, 'car_price_bar.html', {'data': context})


def car_price_bar_data(request):
    labels = []
    series_data = []
    for i in range(5, 50, 5):
        data = NewEnergyCar.objects.filter(max_price__lte=i) & NewEnergyCar.objects.filter(max_price__gte=i-5)
        series_data.append(len(data))
        labels.append('{}-{}万'.format(str(i-5), str(i)))
    data = NewEnergyCar.objects.filter(max_price__gte=50)
    series_data.append(len(data))
    labels.append('50万以上')
    context = {
        'legend_data': labels,
        'series_data': series_data
    }
    return HttpResponse(json.dumps(context))

@csrf_exempt
def car_pure_energy_bar(request):
    context = {}
    return render(request, 'car_pure_energy_bar.html', {'data': context})


def car_pure_energy_bar_data(request):
    labels = []
    series_data = []
    for i in range(100, 600, 100):
        data = NewEnergyCar.objects.filter(max_pure_energy_range__lte=i) & NewEnergyCar.objects.filter(max_pure_energy_range__gte=i-100)
        series_data.append(len(data))
        labels.append('{}-{}公里'.format(str(i-100), str(i)))
    data = NewEnergyCar.objects.filter(max_pure_energy_range__gte=600)
    series_data.append(len(data))
    labels.append('600公里以上')
    context = {
        'legend_data': labels,
        'series_data': series_data
    }
    return HttpResponse(json.dumps(context))
