from django.db import models

# Create your models here.
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(verbose_name='カテゴリ', max_length=20)

    def __str__(self):
     return self.title
    
class InventoryPost(models.Model):
   user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
   category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
   title = models.CharField(verbose_name='数量', max_length=10)
   comment = models.TextField(verbose_name='商品名', max_length=10)
   image1 = models.ImageField(verbose_name='イメージ1', upload_to='inventorys')
   image2 = models.ImageField(verbose_name='イメージ２', upload_to='inventorys')
   posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)

   
   def __str__(self):
      return self.title