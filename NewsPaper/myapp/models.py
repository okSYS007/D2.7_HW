
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):

    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rate = models.IntegerField(default=0)
    
    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating = Sum('post_rate'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.author_user.comment_set.all().aggregate(commentRating = Sum('comment_rate'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.author_rate = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return '%s %s' % (self.author_user, self.author_rate)
 
class Category(models.Model):

    category_name = models.CharField(max_length=255, unique=True)

class Post(models.Model):

    def like(self):
        self.post_rate += 1
        self.save()
    def dislike(self):
        self.post_rate -= 1
        self.save()

    def preview(self):
        return self.post_text[:124] + '...' if len(self.post_text) > 124 else self.post_text + '...'

    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    CHOICES = [
        (1, 'Статья'), 
        (2, 'Новость')
        ]
    post_choice = models.CharField(max_length = 2, 
                            choices = CHOICES, 
                            default = 'Статья')
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=255)
    post_text = models.TextField(default='content')
    post_rate = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s %s %s' % (self.creation_date, self.post_author.author_user.username, self.post_author.author_rate, self.post_title, self.preview())

class PostCategory(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):

    def like(self):
        self.comment_rate += 1
        self.save()
    def dislike(self):
        self.comment_rate -= 1
        self.save()

    def __str__(self):
        return self.post.post_author.author_user.username

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(default='Комментарий')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_rate = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s %s' % (self.comment_date, self.user.username, self.comment_rate, self.comment_text)