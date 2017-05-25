from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm


def index(request):
    context = RequestContext(request=request)

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}

    for category in category_list:
        category.url = category.name.replace(' ', '_')

    for page in page_list:
        page.url = page.title.replace(' ', '_')

    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request=request)

    return render_to_response('rango/about.html', context)


def category(reqeust, category_name_url):
    context = RequestContext(reqeust)

    category_name = decode_url(category_name_url)

    context_dict = {'category_name': category_name, 'category_name_url': category_name_url}

    try:
        category = Category.objects.get(name=category_name)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['error'] = 'category deos not exists'

    return render_to_response('rango/category.html', context_dict, context)


def decode_url(category_name_url):
    return category_name_url.replace('_', ' ')


def encode_url(category_name):
    return category_name.replace(' ', '_')


def add_category(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors

    else:
        form = CategoryForm()

    return render_to_response('rango/add_category.html', {'form': form}, context)


def add_page(request, category_name_url):
    context = RequestContext(request)

    category_name = decode_url(category_name_url)
    context_dict = {}

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)

            cat = Category.objects.get(name=category_name)
            page.category = cat

            page.views = 0

            page.save()

            return category(request, category_name_url)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict['category_name_url'] = category_name_url
    context_dict['category_name'] = category_name
    context_dict['form'] = form

    return render_to_response('rango/add_page.html',
                              {'category_name_url': category_name_url, 'category_name': category_name, 'form': form},
                              context)
