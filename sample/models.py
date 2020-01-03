from django.db import models


class MainList(models.Model):
    title = models.CharField(verbose_name='メイン項目名', max_length=100)
    datetime = models.DateTimeField(verbose_name='日付')

    class Meta:
        db_table = 'mainlist'

    def __str__(self):
        return self.title


class SubList(models.Model):
    main_list = models.ForeignKey(MainList, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='サブ項目名', max_length=100)
    total_num = models.IntegerField(verbose_name='総数', default=0)

    class Meta:
        db_table = 'sublist'

    def __str__(self):
        return self.title
