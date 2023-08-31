from django.urls import path
from .views import home_view , create_article_view ,article_detail, like_article , unlike_article , UpdateArticleView , DeleteArticleView ,ArticalListView


urlpatterns = [
    path('', home_view, name='home'), 
    path('new', create_article_view, name='new-article'),
    # path('article/<int:pk>/update/', update_article, name='update_article'),
    path('articles/', ArticalListView.as_view(), name='list-article'),
    path('article/<int:pk>/update/', UpdateArticleView.as_view(), name='update-article'),
    path('article/<int:id>/delete/', DeleteArticleView.as_view(), name='delete-article'),

    path('article/<int:id>/' ,article_detail, name='article-detail' ),
    path('article/<int:id>/like', like_article, name='like'),
    path('article/<int:id>/unlike', unlike_article, name='unlike')

]
