import logging
from django.http import HttpResponse

logger = logging.getLogger("myapp")

def home(request):
    logger.debug("DEBUG: домашня сторінка")
    logger.info("INFO: користувач відкрив головну")
    logger.error("ERROR: тестова помилка для логування")
    return HttpResponse("Логування працює! Перевірте файли logs/*.log")

