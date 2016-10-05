from django.shortcuts import render
from elasticsearch import Elasticsearch

def search(request):
    if request.method == 'GET':
        term = request.GET.get('term_search')

        search_term(term)

        return render(request, 'view_athena/index.html', {})

def search_term(term):
    es = Elasticsearch()

    res = es.search(index="athena", body={"query": {"match": {"url": "\"" + str(term) + "\""}}})

    for hit in res['hits']['hits']:
        print("%(url)s:" % hit["_source"])
