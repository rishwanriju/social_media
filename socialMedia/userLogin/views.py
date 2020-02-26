from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect,render
from . models import dlogin,Post
from . forms import LoginForm,RegForm
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required



class login_page (View):

    form_class = LoginForm
    template_name = 'login.html'
    
    def get (self , request):
        form = self.form_class()
        print(form)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            log = dlogin.objects.filter(username = request.POST.get('username') , password =  request.POST.get('password'))
            if log :
                request.session['my_session'] = 'username'
                return redirect('posts/')
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
        if self.request.session.has_key('my_session'):
            print("sss")
            queryset = Post.objects.filter(status=1).order_by('-created_on')
            print(queryset)
            return queryset
    

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'

    def get_queryset(self):
        print("kmoklmk")
        if self.request.session.get('my_session'):
            queryset = Post.objects.filter(status=1).order_by('-created_on')
            print(queryset)
            return queryset