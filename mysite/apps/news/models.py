from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self):
        # отсюда не получить количество постов и комментариев,
        # поэтому правильнее сделать автоизменение рейтинга автора
        # непосредственно при лайке или дислайке
        return True


class Category(models.Model):
    name = models.CharField(max_length = 255)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    article = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length = 1255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        Author.objects.get(id=self.author).rating += 3
        return self.rating

    def dislike(self):
        self.rating -= 1
        Author.objects.get(id=self.author).rating -= 3
        return self.rating

    def preview(self):
        return self.text[:124] if len(self.text) <=124 else self.text[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        Author.objects.get(user=Post.objects.get(id=self.post).author).rating += 1
        if len(Author.objects.filter(user=user)) > 0:
            Author.objects.filter(user=user)[0].rating += 1
        return self.rating

    def dislike(self):
        self.rating -= 1
        Author.objects.get(id=Post.objects.get(id=self.post).author).rating -= 1
        if len(Author.objects.filter(user=user)) > 0:
            Author.objects.filter(user=user)[0].rating -= 1
        return self.rating
