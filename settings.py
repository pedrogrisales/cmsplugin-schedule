#-*- coding: utf-8 -*-
from django.conf import settings
import os


BXSLIDER_JS_URL = getattr(settings, 'BXSLIDER_JS_URL', 'static/js/bxslider/jquery.bxSlider.min.js',)