from http.client import HTTPResponse
# from audioop import reverse
from curses.ascii import isdigit
from xml.dom import ValidationErr
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView
from core.forms import EmailForm, PostCreateForm, PostEditForm
from core.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




class IsPostOwner:
    def get_queryset(self):
        return self.request.user.post_sat.all()




# Create your views here.
def home_view(request: HttpRequest)-> HttpResponse:
    return render (request,'home.html', context = {
        'posts':Post.objects.all(),
        'custom_form': EmailForm()
        })



# pk aris igive id (primary key)
def post_detail_view (request:HttpRequest, pk: int)-> HttpResponse:
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('requesterd post does not exist')
    return render(request, 'post_detail.html', {'post': post, })



@login_required

def post_delete_view(request: HttpRequest,)-> HttpResponse:
    if request.method == 'Get':
        return redirect('core:home')
    
    pk: str = request.POST.get('pk', '')

    if pk.isdigit():
        pk: int = int(pk)

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('Requested Post does not exists')

    post.delete()

    return redirect ('core:home')

@login_required
def post_create_view(request: HttpRequest)-> HttpResponse:
    template: str = 'post_create.html'
    if request.method =='GET':
        return render(request, template, context={'form': PostCreateForm()})

    form = PostCreateForm(data=request.POST)

    if not form.is_valid():
        return render(request,template,{'form':form})

    form.save()
    return redirect('core:home')



class PostCreateView(IsPostOwner, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('core:home')
    template_name = 'post_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PostEditView(IsPostOwner, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post_create.html'
    # def get_queryset(self) -> models.query.QuerySet[Any]:
    #     return self.request.

    def get_success_url(self) -> str:
        return reverse('core:post-detail', kwargs={'pk':self.object.pk})





@login_required

def post_edit_view(request: HttpRequest, pk: int)-> HttpResponse:
    template: str = 'post_create.html'
    
    
    post = get_object_or_404(Post, pk=pk)


    form = PostEditForm(data=request.POST or None, instance=post)
    
    if request.method =='GET':
        return render(request, template, context={'form': form})

    form = PostEditForm(data=request.POST)

    if not form.is_valid():
        return render(request,template,{'form':form})


    form.save()
    # post.title = form.cleaned_data['title']
    # post.text = form.cleaned_data['text']
    # post.save()
    return redirect('core:home')

