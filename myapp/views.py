from django.http import HttpResponse
import logging

logger = logging.getLogger('myapp')

def index(request):
    logger.debug("DEBUG: index opened")
    logger.info("INFO: index opened")
    logger.warning("WARNING: test warning")
    logger.error("ERROR: test error")
    return HttpResponse("Hello from myapp!")
