from django.test import TestCase

# Create your tests here.
from config.wsgi import *
from core.erp.models import Type

#Listar
'''
# select * from Tabla
query =Type.objects.all()
print(query)
'''
#Insercion


'''
Forma de insertar 1
t = Type()      
t.name = 'Prueba'
t.save()'''

'''
Forma de insertar 2
t = Type(name='Prueba2')
t.save() 
'''

'''
Forma de insertar 3
t = Type(name='Prueba3').save()
'''

#edicion
'''
try:
    t = Type.objects.get(pk=1)
    t.name = 'Accionistasmod'
    t.save()
except Exception as e:
    print(e)
    '''
'''
#eliminacion
t = Type.objects.get(pk=1)
t.delete()
'''

'''obj = Type.objects.filter(name__contains='terry')
print(obj)'''

'''obj2 = Type.objects.filter(name__startswith='p')
print(obj2)'''

'''
obj2 = Type.objects.filter(name__endswith='a')
print(obj2)
'''


'''
obj2 = Type.objects.filter(name__in=['Prueba','Presidente'])
print(obj2)
'''
'''
obj2 = Type.objects.filter(name__in=['Prueba','Presidente']).count()
print(obj2)
'''
'''
obj2 = Type.objects.filter(name__endswith='a').exclude(id=5)
print(obj2)
'''
'''
for i in Type.objects.filter(name__endswith='a') :
    print(i.name)
'''

'''
for i in Type.objects.filter(name__endswith='a')[:1]:
    print(i.name)
'''
