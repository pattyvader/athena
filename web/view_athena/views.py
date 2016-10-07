from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.http import HttpResponse

def search(request):
    if request.method == 'GET':
        term = request.GET.get('term_search')
        response = search_term(term)
        pages = []

        for hit in response['hits']['hits']:
            pages.append(hit["_source"])

        return render(request, 'view_athena/index.html', {'pages':pages})

def search_term(term):
    es = Elasticsearch()

    res = es.search(index="athena", body={"query": {"match": {"url": "\"" + str(term) + "\""}}})

    return res
