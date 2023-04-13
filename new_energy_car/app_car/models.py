from django.db import models


class UserAccount(models.Model):
    user_account = models.CharField(max_length=200, verbose_name='用户账号', blank=True, null=True)
    password = models.CharField(max_length=200, verbose_name='用户密码', blank=True, null=True)
    email = models.CharField(max_length=200, verbose_name='邮箱', blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name='电话', blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = '用户账号表'
        verbose_name_plural = '用户账号表'

    def __str__(self):
        return '{}-（{}）-{}'.format(self.user_account, self.email, self.phone)


class NewEnergyCar(models.Model):
    serie_name = models.CharField(max_length=200, verbose_name='系列名称', blank=True, null=True)
    serie_img = models.CharField(max_length=200, verbose_name='系列URL', blank=True, null=True)
    serie_pinyin = models.CharField(max_length=200, verbose_name='系列名称拼音', blank=True, null=True)
    serie_level = models.FloatField('系列等级', default=0, blank=True)
    min_price = models.FloatField(max_length=200, verbose_name='最低价格', blank=True, null=True)
    max_price = models.FloatField(max_length=200, verbose_name='最高价格', blank=True, null=True)
    min_guide_price = models.FloatField('最低指导价格', default=0, blank=True)
    max_guide_price = models.FloatField('最高指导价格', default=0, blank=True)
    new_type = models.FloatField('新类型', default=0, blank=True)
    max_energy_range = models.FloatField('最大里程', default=0, blank=True)
    max_pure_energy_range = models.FloatField('纯电续航里程', default=0, blank=True)
    model_config_video_num = models.FloatField('车型款数', default=0, blank=True)
    has_subsidy = models.FloatField('是否有补贴', default=0, blank=True)
    model_count = models.FloatField('车型款数', default=0, blank=True)

    class Meta:
        managed = True
        verbose_name = '新能源电动车价格表'
        verbose_name_plural = '新能源电动车价格表'

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.serie_name, self.max_pure_energy_range, self.min_guide_price, self.max_guide_price)
