from elasticsearch import Elasticsearch

#localhost:9200
es = Elasticsearch()

def create_index():
    doc = {
        'url': 'https://www.python.org/events/python-events/462/',
        'title': 'Python Brasil [12]',
        'description':'The official home of the Python Programming Language',
        'image':'https://www.python.org/static/opengraph-icon-200x200.png',
        'text':'Notice: While Javascript is not essential for this website'
    }

    res = es.index(index="athena", doc_type='page', body=doc)
    print(res['created'])

def main():
    create_index()

if __name__ == "__main__":
    main()
