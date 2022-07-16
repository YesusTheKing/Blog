from django.db import models
from Blog.ent_config import *
from djrichtextfield.models import RichTextField
# Create your models here.

class Blog(models.Model):
    BlogId = models.BigAutoField(primary_key=True,verbose_name="BLOGID")
    BlogCreator = models.CharField(max_length=50,verbose_name="BLOGCREATOR",default=Blog_Creator)
    BlogCreatedDate = models.DateTimeField(verbose_name="CREATEDDATE")
    BlogContent = models.TextField(verbose_name="BLOGCONTENT")
    BlogRichContent = RichTextField(verbose_name="BLOGACTUALCOMMENT",null =True)
    BlogHeader = models.CharField(max_length=100,verbose_name="BLOGHEADER")
    BlogLikes = models.IntegerField(verbose_name="LIKECOUNT")

    class Meta:
        verbose_name = "Blog"
        db_table = "BLOG"
        verbose_name_plural = "Blogs"
    
    def __repr__(self):
        return self.BlogHeader
    def __str__(self):
        return self.BlogHeader
    

class BlogComment(models.Model):
    BlogCommentId = models.BigAutoField(primary_key=True,verbose_name="BLOGCOMMENTID")
    BlogId = models.OneToOneField(Blog, on_delete=models.CASCADE,verbose_name="BLOGID")
    BlogComment = models.TextField(verbose_name="BLOGCOMMENT")
    CreatedDate = models.DateTimeField(verbose_name="CREATEDDATE")

    class Meta:
        verbose_name = "BlogComment"
        db_table = "BLOGCOMMENT"
        verbose_name_plural ="BlogComments"
    
    def __str__(self):
        return self.BlogComment
    