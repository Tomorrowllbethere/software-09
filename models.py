from datetime import datetime

from mongoengine import Document
from mongoengine.fields import  ListField, StringField, ReferenceField


class Author(Document):

    fullname = StringField(max_length=70, min_length=5, unique= True)
    born_date=StringField(max_length=70, min_length=5)
    born_location=StringField(max_length=70, min_length=5)
    description=StringField()

class Quote(Document):
    tags= ListField()
    author= ReferenceField(Author, reverse_delete_rule='CASCADE')
    quote= StringField()