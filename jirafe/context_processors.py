from django.conf import settings


def jirafe(request):
    """
    Add variables to indicate when to submit variables to Jirafe
    """
    return {
        'JIRAFE_ID': settings.JIRAFE_ID
    }