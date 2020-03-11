from django.views import View
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import redirect,render,get_object_or_404
from . models import dlogin,Post,post_like,post_comment
from . forms import LoginForm,RegForm,CommentForm
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,RedirectView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin


def dec(a):
    def warp(self,request,*arg, **kwargs):
        if self.request.session.has_key('my_session'):
            b=a(self,request,*arg,**kwargs)
        else:
            b=redirect("login")
       
        return b
    return warp


class login_page (View):

    form_class = LoginForm
    template_name = 'login.html'
    
    def get (self , request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            log = dlogin.objects.filter(username = request.POST.get('username') , password =  request.POST.get('password'))
            if log :
                request.session['my_session'] = username
                return redirect('Posts')
            else :
                messages.add_message(request, messages.INFO, 'Not registered , Click to Register.')
        return redirect('/')

class Register(View):
        form_class = RegForm
        template_name = 'register.html'

        def get(self,request):
            lform = self.form_class
            return render (request,self.template_name,{'lform':lform})

        def post(self,request):
            lform = self.form_class(request.POST)
            if lform.is_valid():
                lform.save()
                return render (request,self.template_name,{'lform':lform})
            else:
                print(lform.errors)
                return render (request,self.template_name,{'lform':lform})


class PostList(ListView):
    template_name = 'index.html'
    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        return queryset

    @dec
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    
    

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'

    def get_queryset(self):
        if self.request.session.get('my_session'):
            queryset = Post.objects.filter(status=1).order_by('-created_on')
            return queryset

class PostUpdate(UpdateView):
    model = Post
    fields = ['posts']
    template_name = 'edit.html'


    @dec
    def dispatch(self,request, *args, **kwargs):
        p=kwargs['pk']
        username = self.request.session['my_session']
        obj = self.model.objects.get(id=p)
        if obj.author.username != username:
            raise Http404("You are not allowed to edit this Post")
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)

    # def get_object(self):
    #     return get_object_or_404(Post, pk=self.request.session['my_session'])

class PostDelete(DeleteView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'delete.html'

    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post,id=id_)
    
    def get_success_url(self):
        return reverse_lazy('Posts')


    @dec
    def dispatch(self,request, *args, **kwargs):
        p=kwargs['pk']
        username = self.request.session['my_session']
        obj = self.model.objects.get(id=p)
        if obj.author.username != username:
            raise Http404("You are not allowed to delete this Post")
        return super(PostDelete, self).dispatch(request, *args, **kwargs)



class PostCreate(CreateView):
    model = Post
    fields = ['posts','images']
    template_name = 'index.html'

    def form_valid(self,form):
        username = self.request.session['my_session']
        user=dlogin.objects.get(username = username)
        form.instance.author=user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            kwargs['object_list'] = self.model.objects.all()
            return super().get_context_data(**kwargs)

    def get_success_url(self):
            return reverse('Posts')
    
class P_likes(View):
    model = post_like
    def get(self,request,**arg):
        user_username=request.session.get('my_session')
        p=arg['id']
        post = Post.objects.get(id=p)
        user= dlogin.objects.get(username=user_username)
        obj= self.model.objects.filter(user=user,post=post)
        if obj:
            obj[0].delete()
        else:
            obj1  =  self.model(user=user,post=post)
            obj1.save()
        return HttpResponse("<html><script>location.replace(document.referrer);</script></html>")


class p_comment(View):
    model = post_comment
    form_class = CommentForm
    template_name = "comment.html"
    def get(self,request,**arg):
        lform = self.form_class()
        return render (request,self.template_name,{'lform':lform})
    def post(self,request,**arg):
        print(request.POST)
        lform = self.form_class(request.POST)
        if lform.is_valid():
            user_username=request.session.get('my_session')
            p=arg['id']
            user= dlogin.objects.get(username=user_username)
            post = Post.objects.get(id = p)
            comments=request.POST['comments']
            obj=self.model(user=user,post=post,comments=comments)
            obj.save()
            return redirect("Posts")
        return render (request,self.template_name,{'lform':lform})

