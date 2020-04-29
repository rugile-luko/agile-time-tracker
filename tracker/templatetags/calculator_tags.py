from django import template


register = template.Library()


@register.filter
def duration(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    if hours == 0 and minutes == 0:
        return 'No Time Tracked'
    if hours == 0:
        return '{} min'.format(minutes)
    elif hours == 1 and minutes > 0:
        return '{} hour {} min'.format(hours, minutes)
    elif hours == 1 and minutes == 0:
        return '{} hour'.format(hours)
    elif hours > 1 and minutes == 0:
        return '{} hours'.format(hours)
    else:
        return '{} hours {} min'.format(hours, minutes)
