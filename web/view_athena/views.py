from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.http import HttpResponse

def search(request):
    if request.method == 'GET':
        term = request.GET.get('term_search')

        if term == None:
            term = ""

        response = search_term(term)
        pages = []

        for hit in response['hits']['hits']:
            result = {'source': hit["_source"], 'highlight': hit["highlight"]["text"][0]}
            pages.append(result)

        return render(request, 'view_athena/index.html', {'pages':pages,'term_search':term})

def search_term(term):
    es = Elasticsearch()

    res = es.search(index="athena", body={"query": {"bool":
                                                   {"should": [ { "match_phrase": { "title": "\"" + str(term) + "\"" }},
                                                   { "match_phrase": { "text": "\"" + str(term) + "\"" }},
                                                   { "match_phrase": { "description": "\"" + str(term) + "\"" }}]}},
                                                        "highlight": {"fields" : {"text" : {}}}})

    return res
