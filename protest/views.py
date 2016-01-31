from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView
from protest.forms import ProtestForm
from protest.models import Protest, User, Participation

# Create your views here.

def index(request) :
    return render(request, 'protest/index.html')

def protest_list(request) :

    protest_list = Protest.objects.all()
    params = {
    'protest_list' : protest_list,
    }
    return render(request, 'protest/protest_list.html', params)


# def protest_detail(request):
#     protest = Protest.objects.get()
#     return render(request, 'protest/protest_detail.html')


def user_detail(request):
    user = User.objects.get()
    participation = Participation.objects.get(pk = self.kwargs['pk'])
    return render(request, 'protest/user_detail.html')


class ProtestDetailView(DetailView):
    def get_object(self, queryset=None):
        # self.kwargs : year, month, day, pk
        # self.kwargs['year']
        # try:
        #     return Post.objects.get(pk=self.kwargs['pk'])
        # except Post.DoesNotExist:
        #     raise Http404
        return get_object_or_404(Protest, pk=self.kwargs['pk'])

# post_detail = DetailView.as_view(model=Post)
protest_detail = ProtestDetailView.as_view()


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

user_detail = DetailView.as_view(model = User)