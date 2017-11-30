
#
###  Imports from application
#
from blog_main.models import Post, PostComment
from blog_main.forms import CommentForm, PostForm
#
### Utility imports
#
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
#
### For working with class based views
#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
DeleteView, CreateView,
UpdateView, DeleteView )



#######################
### Views for Posts ###
#######################


class AboutView(TemplateView):
    template_name = 'about.html'

class PostList(ListView):
    model = Post

    def get_queryset(self):
        ### Quering the database for Post objects and filtering the data by
        ### Publish_date earlier than current time and
        ### ordering the result by most recent posts
        return Post.objects.filter(publish_date__lte = timezone.now()).order_by('-published_date'))


class PostCreateView(CreateView, LoginRequiredMixin):
    ###
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog_main/post_detail.html'
    from_class = PostForm


    # def get_absolute_url(self):
    #     return reverse('post_list')

# Create your views here.
class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog_main/post_detail.html'
    from_class = PostForm

class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('blog_main:post_list')
    login_url = '/login/'
    from_class = PostForm

class PostDraftListView(ListView, LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog_main:post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('-creation_date')




########################
## View for comments ###
########################


def add_comment_to_post(request, pk):
    ### Checking if there is the post withnthe given pk in the database
    ### If not return 404 page
    post = get_object_or_404(Post, pk = pk)
    ### Cheching if the incomming request's method is POST
    if request.method == 'POST':
        ### Creating a temporary object with provided data
        form = CommentForm(request.post)
        ### Checking for validation of the provided data
        if form.is_valid():
            ### If the data is valid, creating a comment object
            comment = form.save(commit = False)
            ### Creating a relationship with Post object
            comment.post = post
            ### Saving to the database
            comment.save()
            ### Redirecting to the details page of the post
            return redirect('blog_main:post_detail', pk=post.pk)
    else:
        ### If request method is not POST, creating comment form object
        form = CommentForm()
    ### Returning html page with form as context
    return render('blog_main/comment_form.html', {'form' : form})



@login_required
def aprove_comment(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve_comment()
    return redirect("post_detail", pk_alt = comment.post.pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk)
    post_pk = comment.post.pk
    comment.detele()
    return redirect('blog_main:post_detail', pk_alt = post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish_post()
    return redirect('blog_main:post_detail')
