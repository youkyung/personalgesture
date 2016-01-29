from django.shortcuts import redirect, render
from protest.forms import ProtestForm

# Create your views here.

def index(request) :
    return render(request, 'templates/index.html')


def protest_new(request):

    if request.method == 'POST' :
        form = ProtestForm (request.POST)
        if form.is_valid():
            protest = form.save ()
            return redirect('protest.views.protest_detail', protest.pk)

    else :
        form = ProtestForm

    return render(request, 'templates/protest_form.html', {
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


def post_list(request) :

    post_list = Protest.objects.all()
    params = {
    'post_list' : post_list,
    }
    return render(request, 'templates/post_list.html', params)

def post_detail(request, pk):

    post = Protest.objects.get(pk=pk)

    params = {
    'post' : post,
    }
    return render(request, 'templates/post_detail.html', params)