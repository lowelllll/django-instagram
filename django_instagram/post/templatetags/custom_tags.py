# -*- coding:UTF-8 -*-
from django import template
from datetime import datetime, timezone

register = template.Library()

@register.filter
def post_date(upload_date): # date 필터
    now_date = datetime.now(timezone.utc)
    day = now_date - upload_date
    if day.days!=0:
        if day.days > 364:
            return "{0}년 {1}월 {2}일".format(upload_date.year,upload_date.month,upload_date.day)
        elif day.days >= 31:
            return "{0}달 전".format(round(day.days/31))
        else:
            return "{0}일 전".format(day.days)
    else:
        if upload_date.hour == now_date.hour:
            return "{0}분 전".format(now_date.minute-upload_date.minute)
        else:
            return "{0}시간 전".format(now_date.hour-upload_date.hour)