from django import template
from django.forms.utils import ErrorList

register = template.Library()

class FormErrorList(ErrorList):
    @register.filter
    def as_divs(value, arg=None):
        """
        Convert an ErrorList to a string of div elements.

        Args:
            value (ErrorList): The ErrorList to convert.
            arg: Additional argument passed by the filter (unused in this case).

        Returns:
            str: A string of div elements.
        """
        if not isinstance(value, ErrorList):
            return value

        return '%s' % ''.join(['\n%s' % e for e in value])
        # return '<div class="alert alert-danger">%s</div>' % ''.join(['<div>%s</div>' % e for e in value])

    def __str__(self):
        return self.as_divs(self)

@register.filter
def as_str(value):

    return value