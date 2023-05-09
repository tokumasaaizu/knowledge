#from accounts.models import CustomUser
from django.db import models


class KnowledgeData(models.Model):
    #ForeignKey の「K」は大文字
    title = models.CharField(verbose_name='タイトル',max_length=100)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    member_list = (
        ('徳竹', 'tokutake'),
        ('www', 'www'),
    )
    member = models.CharField(max_length=50, choices=member_list, blank=True)

    #class Meta:
        #verbose_name_plural = 'List'
    #def __str__(self):
        #return self.title





