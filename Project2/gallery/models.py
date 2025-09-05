from django.db import models
from accounts.models import Account
from django.utils.text import slugify

class Post(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    likes = models.ManyToManyField(Account,related_name="liked_posts",blank=True)
    like_count = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='posts/',blank=False,null=True)
   
    def __str__(self):
        return self.title

    def update_likes_count(self):
        self.like_count = self.likes.count()
        self.save()
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def get_comment_count(self):
        return self.comments.count()

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.title}"
    
    
