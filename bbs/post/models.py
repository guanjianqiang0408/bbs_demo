from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ["-createtime"]
    
    createtime = models.DateTimeField(help_text="创建时间", auto_now_add=True)
    last_modified = models.DateTimeField(help_text="更新时间", auto_now=True)

    def __str__(self):
        return NotImplementedError

class Topic(BaseModel):
    title = models.CharField(help_text="话题标题", max_length=255, unique=True)
    content = models.TextField(help_text="话题内容")
    is_online = models.BooleanField(help_text="话题是否在线", default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="关联用户表")

    def __str__(self):
        return "{}: {}".format(self.id, self.title[0:20])

class Comment(BaseModel):
    content = models.TextField(help_text="评论内容")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, help_text="关联话题")
    up = models.IntegerField(help_text="支持", default=0)
    down = models.IntegerField(help_text="反对", default=0)
    def __str__(self):
        return "{}: {}".format(self.id, self.content[0:20]) 
