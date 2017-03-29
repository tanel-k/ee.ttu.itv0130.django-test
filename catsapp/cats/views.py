from django.shortcuts import render, redirect
from datetime import datetime

from .models import Cat

def index(request):
    cat_list = Cat.objects.all()
    context = {
        'cat_list': cat_list
    }
    return render(request, 'cats/index.html', context)

def new_cat(request):
    context = {}

    form = {
        'name': '',
        'year_of_birth': '',
        'errors': {}
    }

    context['form'] = form

    if request.method == 'POST':
        form['name'] = request.POST['name']
        form['year_of_birth'] = request.POST['year_of_birth']

        validate_cat(form)

        if not form['errors']:
            c = Cat(
                name=form['name'],
                year_of_birth=form['year_of_birth']
            )
            c.save()
            return redirect(to='cats:index')

    return render(request, 'cats/new_cat.html', context)

def validate_cat(form):
    if not form['name']:
        form['errors']['name'] = 'This field is required'

    if not form['year_of_birth']:
        form['errors']['year_of_birth'] = 'This field is required'

    try:
        form['year_of_birth'] = int(form['year_of_birth'])

        if form['year_of_birth'] < 1900 or form['year_of_birth'] > datetime.now().year:
            form['errors']['year_of_birth'] = 'You must enter a valid year'
    except ValueError:
        form['errors']['year_of_birth'] = 'You must enter a number'


