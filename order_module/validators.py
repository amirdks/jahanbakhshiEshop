from django.core.exceptions import ValidationError


def min_count_validator(value):
    if value < 1:
        raise ValidationError("تعداد نمیتواند کمتر از 1 باشد")
    else:
        return value
