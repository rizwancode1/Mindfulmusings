from django.shortcuts import render,  redirect ,get_object_or_404  
from django.urls import reverse_lazy ,reverse
from django.http import JsonResponse
from django.db.models import Q
## using class base view for update article
from django.views.generic import UpdateView , DeleteView , ListView
from .models import Article, Comment ,Categories ,Tag
from .forms import CreateArticalForm , CommentForm 

# Create your views here.


def home_view(request):
    categories = Categories.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    articles = Article.objects.filter(
        Q(title__icontains=q)|
        Q(category__name__icontains=q)|
        Q(tag__hashtag__icontains=q)
    )
    



    ctx = {
        'articles':articles,
        'categories':categories
    }
    return render(request,'blog/home.html', ctx)

class ArticalListView(ListView):
    categories = Categories.objects.all()
    queryset = Article.objects.all()
    template_name = 'blog/articles_list.html'



def create_article_view(request):
    categories = Categories.objects.all()
    tags_list = Tag.objects.all()
    form = CreateArticalForm()
    
    if request.method == 'POST':

        category_name =request.POST.get('category')
        category, created  =Categories.objects.get_or_create(name = category_name)
        tag_hashtag = request.POST.get('tag')

        tag , created  = Tag.objects.get_or_create(hashtag = tag_hashtag)

        if not created:
            tag = Tag.objects.get(hashtag=tag_hashtag)
            category = Categories.objects.get(name = category_name)
            
        article = Article.objects.create(
            author = request.user,
            title = request.POST.get('title'),
            content = request.POST.get('content'),   
        )
        article.category.add(category)
        article.tag.add(tag)
        return redirect('home')
    else:
        form = CreateArticalForm()
    
    ctx = {
        'form': form,
        'categories': categories,
        'tags_list': tags_list,
        
    }
    return render(request, 'blog/create_article.html', ctx)

##### function base view

# def update_article(request, pk):
#     article = get_object_or_404(Article, pk=pk)

#     if request.method == 'POST':
#         form = CreateArticalForm(request.POST, instance=article)
#         if form.is_valid():
#             form.save()
#             return redirect('article_detail', id=pk)  # Redirect to the article detail page
#     else:
#         form = CreateArticalForm(instance=article)

#     return render(request, 'update_article.html', {'form': form, 'article': article})

## class base view

class UpdateArticleView(UpdateView):
    model = Article
    form_class = CreateArticalForm  # Use the form you've defined
    template_name = 'blog/update_article.html'
    # success_url = reverse_lazy('home')
    def get_success_url(self):
        # return reverse('articles:article-list')
        return reverse('list-article')

class DeleteArticleView(DeleteView):
    template_name =  'blog/delete_article.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        print(id_)
        return get_object_or_404(Article, id=id_)


    # success_url = reverse_lazy('home')

    def get_success_url(self):
        # return reverse('articles:article-list')
        return reverse('list-article')




def create_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = article
            comment.save()
            return redirect('article_detail', pk=article.id)  # Redirect to the article detail page
    else:
        form = CommentForm()

    return render(request, 'artical_detail.html', {'article': article, 'form': form})


def article_detail(request, id):
    categories = Categories.objects.all()
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.all()
    ## for artical create form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = article
            comment.save()
            return redirect('article-detail', id=id)  # Redirect to the article detail page
    else:
        form = CommentForm()

    ctx = {
        'article':article,
        'comments':comments,
        'categories':categories,
        'form':form,
    }
    return render(request, 'blog/article_detail.html' , ctx)


    
def like_article(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.user not in article.likes.all():
        article.likes.add(request.user)
        article.save()
        
    return JsonResponse({'likes': article.likes.count()})

    # return redirect('article_detail', article_id=article.id)
    

def unlike_article(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.user in article.likes.all():
        article.likes.remove(request.user)
        article.save()
        
    return JsonResponse({'likes': article.likes.count()})

    # return redirect('article_detail', article_id=article.id)





