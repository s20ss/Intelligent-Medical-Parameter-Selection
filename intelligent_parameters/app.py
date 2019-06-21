import os
from flask import Flask
from flask import render_template
from flask import request
from jinja2 import Template
from bio_entrez2 import search_and_download_file
from file_indexing import index_files_into_elasticsearch

app = Flask(__name__)
from elasticsearch import Elasticsearch
from tika import parser
import json
es=Elasticsearch([{'host':'localhost','port':9200}])
print(es)

def search_query(query_string1):
    res3 = es.search(index='parameter', doc_type='pdf', body={

        'query': {
            'query_string': {

                "query": query_string1

            }
        }
    })
    #print(res3)
    hits=(res3['hits']['hits'])
    temp_dict=[]
    #print(hits)
    table_array=[]
    for i in range(0,len(hits)):
        temp_dict = []
        score=str(((hits[i]['_score'])))
        filename=str(((hits[i]['_source']['file name'])))
        keywords=str(((hits[i]['_source']['keywords'])))
        authors=str(((hits[i]['_source']['Authors'])))
        date = str(((hits[i]['_source']['date'])))
        temp_dict.append(score)
        temp_dict.append(filename)
        temp_dict.append(keywords)
        temp_dict.append(authors)
        temp_dict.append(date)
        table_array.append(temp_dict)
    json_dumps=json.dumps(table_array)
    json_object_table=json.loads(json_dumps)
    print(table_array)

    return render_template('intelligent_parameter.html',table=table_array)
@app.route('/')
def hello_world():
    return render_template('intelligent_parameter.html',table=None)
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['keyword']
    text1=request.form['target_area']
    processed_text = text.upper()
    processed_text1 = text1.upper()
    query=processed_text+'and '+processed_text1
    #search_and_download_file(query)
    #index_files_into_elasticsearch()
    print(processed_text)
    print(processed_text1)
    result=search_query(processed_text)
    return(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1200)



