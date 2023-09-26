from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.admin.views.decorators import staff_member_required
from .mypermission import customepermission
from django.utils.decorators import method_decorator
from .models import BlogPost, Comment
from .form import BlogPostForm, CommentForm
from django.views.generic import View,TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


# @login_required(login_url='login')
def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    # Implement pagination here
    return render(request, 'blogtemp/blog_post_list.html', {'blog_posts': blog_posts})

@login_required(login_url='login')
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_post_list')
    else:
        form = BlogPostForm()
    return render(request, 'blogtemp/create_blog_post.html', {'form': form})

# Implement other views (update, delete, comments, etc.) similarly
from django.shortcuts import render

# Create your views here.


@login_required(login_url='login')
@staff_member_required(login_url='blog_post_list')
def update_blog_post(request,id):
    print('insise update 1')
    obj=BlogPost.objects.get(id=id)
    if request.method == 'POST':
        form = BlogPostForm(obj,data=request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_post_list')
    else:
        form = BlogPostForm(instance=obj)
    return render(request, 'blogtemp/update_blog_post.html', {'form': form})


""" first method using decoraters or use if contdion inside function like (request.user.is_superuser or blog.delete_blogpost)"""
                                                                                        # syntax        # (applicationname.action_modelname)                                                                                             
@login_required(login_url='login')
# @permission_required(['blog.delete_blogpost'],login_url='/blog')
@permission_required(['request.user.is_superuser'],login_url='/blog')
def delete_blog_post(request,id): 
    obj=BlogPost.objects.get(id=id)
    print('insde delete')
    # obj.delete()
    return redirect('blog_post_list')


""" another way to check permisiion in template engine we apply it on blog_post_list.html  and check below function"""


# @login_required(login_url='login')
# # @permission_required(['request.user.is_superuser'],login_url='/blog')
# def delete_blog_post(request,id): 
#     obj=BlogPost.objects.get(id=id)
#     print('insde delete')
#     # obj.delete()
#     return redirect('blog_post_list')


""" ----------------------- class based view -------------------------"""



# class BlogListView(View):
    
#     template_name='blogtemp/blog_post_list.html'
#     form=BlogPostForm

#     def get(self,request):
#         blog_posts=BlogPost.objects.all()
#         context={
#             'blog_posts':blog_posts,
#             'form':self.form
#         }
#         return render(request,self.template_name,context)


#     def post(self,request):
#         form=self.form(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'blog added successfully')

#         context={
#             'form':form
#         }            
#         # return render(request,self.template_name,context)
#         return redirect('blog_post_list')


# "templateview used only for view (only get http method support)"
# class BlogListView(TemplateView):
#     template_name='blogtemp/blog_post_list.html'
#     form=BlogPostForm

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context=super().get_context_data()
#         context['form']=self.form
#         context['blog_posts']=BlogPost.objects.all()
#         return context

#     def post(self,request):

#         form=self.form(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'blog added successfully')

#         context={
#             'form':form
#         }            
#         # return render(request,self.template_name,context)
#         return redirect('blog_post_list')



# # by default 
# """for multiple object"""
# class BlogListView(ListView):
#     template_name='blogtemp/blog_post_list.html'
#     form=BlogPostForm
#     model=BlogPost



    

# # customize it
# """for multiple object"""
class BlogListView(ListView):
    # queryset=BlogPost.objects.all()
    template_name='blogtemp/blog_post_list.html'
    form_class=BlogPostForm
    model=BlogPost
    # ordering=['field_name']--> to dispaly order data
    # context_object_name = 'blogpost' --> to access our queryset dat in template(html file) 

    """ by default it (BlogPost)givenmodel.objects.all() if you want customize query you can override get queryset method"""
    def get_queryset(self,request=None) -> QuerySet[Any]:
        return BlogPost.objects.filter(author=5)
    

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)    
        context['form']=self.form_class
        context['blog_posts']=self.get_queryset()
        return context


    # def post(self,request):
    #     form=self.form(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,'blog added succes fully !')
    #         return redirect('blog_post_list')



# customize it  
"""for single object"""

class BlogDetailView(DetailView):
    # queryset=BlogPost.objects.filter(title='title5')
    template_name='blogtemp/update_blog_post.html'
    # form=BlogPostForm
    model=BlogPost
    # pk_url_kwarg='id'--> to change name of pk(default) in given url
    # ordering=['field_name']--> to dispaly order data
    # context_object_name = 'blogpost' --> to access our queryset data in template(html file) 

    # """ by default it (BlogPost)givenmodel.objects.get(pk) if you want customize query you can override get queryset method"""
    
    # default written no need to write just for understaing
    # def get_queryset(self) -> QuerySet[Any]:
    #     # QuerySet=super().get_queryset()
    #     return BlogPost.objects.get(pk=self.kwargs['pk'])
    
    
    def get_queryset(self) -> QuerySet[Any]:
        QuerySet=super().get_queryset()
        return QuerySet.filter(pk=self.kwargs['pk'])
    

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)    
        # context['form']=self.form
        # context['blog_posts']=self.get_queryset()
        return context




""" for creating object or save data into database"""

class BlogCreateView(CreateView):

    template_name='blogtemp/create_blog_post.html'
    # form_class=BlogPostForm --> to override inbult form then use it.
    model=BlogPost
    success_url='/blog'
    fields="__all__"
    # context_object_name=BlogPost

""" how to use inbluilt decorater in class based view"""

# to apply django permission.login_require and staff_member_required @method decoraters in class based view

# @method_decorator(login_required(login_url='blog_post_list'))
# @method_decorator(staff_member_required)
# @method_decorator(permission_required)

# another way to use it
# name=dispatch must same as it is

# @method_decorator((login_required(login_url='blog_post_list'),staff_member_required(login_url='blog_post_list')),name='dispatch')

# another way to use it
# dec=[login_required(login_url='blog_post_list'),staff_member_required(login_url='blog_post_list')]

# @method_decorator(dec,name='dispatch')

# or you can also apply custome permission like inherit customepermission see below line  
# class BlogUpdateView(customepermission,UpdateView):
# class BlogUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):



class BlogUpdateView(UpdateView):    

    template_name='blogtemp/update_blog_post.html'
    # form_class=BlogPostForm 
    # --> to override inbult form then use it.
    model=BlogPost
    success_url='/blog'
    fields="__all__"
    # context_object_name=BlogPost (change name of default given object to acces in html page)



class BlogDeleteview(DeleteView):
    template_name='blogtemp/blogpost_confirm_delete.html'
    model=BlogPost
    success_url='/blog'

