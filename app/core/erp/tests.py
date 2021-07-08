from app.wsgi import *

from core.erp.models import Category

# Listed
for i in Category.objects.filter():
    print(i)
