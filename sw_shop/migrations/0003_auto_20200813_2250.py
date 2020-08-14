# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2020-08-13 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_shop', '0002_auto_20200813_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name_af',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ast',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_be',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_bg',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_bn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_bs',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ca',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_cs',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_cy',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_da',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_dsb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_el',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_en_au',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_eo',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_es_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_es_co',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_es_mx',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_es_ni',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_es_ve',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_et',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_eu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_fa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_fi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_fy',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ga',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_gd',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_gl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_he',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_hi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_hr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_hsb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_hu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ia',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ind',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_io',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_is',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_it',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ka',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_kk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_km',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_kn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ko',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_lb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_lt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_lv',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_mk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ml',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_mn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_mr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_my',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_nb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ne',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_nl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_nn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_os',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_pa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_pl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ro',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_sk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_sl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_sq',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_sr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_sr_latn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_sv',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_sw',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ta',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_te',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_th',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_tr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_tt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_udm',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_uk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_vi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_zh_hant',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
