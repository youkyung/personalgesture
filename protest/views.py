from django.shortcuts import redirect, render
from protest.forms import ProtestForm
from protest.models import Protest
# Create your views here.

def index(request) :
    return render(request, 'protest/index.html')

def post_list(request) :

    post_list = Protest.objects.all()
    params = {
    'post_list' : post_list,
    }
    return render(request, 'protest/post_list.html', params)


def protest_new(request):

    if request.method == 'POST' :
        form = ProtestForm (request.POST)
        if form.is_valid():
            protest = form.save ()
            return redirect('protest.views.protest_detail', protest.pk)

    else :
        form = ProtestForm

    return render(request, 'protest/protest_form.html', {
        'form' : form,
        })


def protest_edit(request, pk):
    protest = Protest.objects.get(pk= pk)

    if request.method == 'POST':
        form = ProtestForm (request.POST, instance = post)
        if form.is_valid():
            protest = form.save()
            return redirect('blog.views.protest_edit', protest.pk)

    else: form = ProtestForm (instance = protest)
    return render(request, 'templates/protest_form.html', {
        'form' : form,
        })