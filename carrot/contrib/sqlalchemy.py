"""
Serializer for sqlalchemy query objects.  
"""
from carrot.serialization import registry

from sqlalchemy.ext.serializer import loads, dumps

registry.register('sqlalchemy', dumps, loads,
                  content_type='application/x-python-serialize',
                  content_encoding='binary')
