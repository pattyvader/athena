from elasticsearch import Elasticsearch

#localhost:9200
es = Elasticsearch()

def create_index():
    res = es.indices.create(index='athena', ignore=400)

def insert_page(url, title, description, image, text):
    doc = {
        'url': url,
        'title': title,
        'description':description,
        'image':image,
        'text':text
    }

    res = es.index(index="athena", doc_type='page', body=doc)

def main():
    create_index()

if __name__ == "__main__":
    main()
