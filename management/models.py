from django.db import models as m

# Create your models here.
class Post(m.Model):
    title = m.CharField(max_length=255)
    content = m.TextField()
    view = m.IntegerField(default=0)
    created = m.DateTimeField(auto_now_add=True)
    midified = m.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} . {self.title}"
    
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"


class Comment(m.Model):
    post = m.ForeignKey(Post,on_delete=m.CASCADE,related_name="comment")
    text = m.TextField(verbose_name="نظر")
    like = m.IntegerField(default=0)
    created = m.DateTimeField(auto_now_add=True)
    midified = m.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.id}"

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
    