import json
from models import Author, Quote
from db import connect

# Замість 'authors.json' та 'quotes.json' введіть шляхи до ваших файлів JSON
with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)

with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

connect()

# Завантаження даних у колекцію authors
for author_data in authors_data:
    Author(**author_data).save()

# Завантаження даних у колекцію quotes
for quote_data in quotes_data:
    author = Author.objects(fullname=quote_data['author']).first()
    Quote(author=author, **quote_data).save()
