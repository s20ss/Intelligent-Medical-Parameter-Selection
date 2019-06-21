import os
from elasticsearch import Elasticsearch
import json
from tika import parser
import spacy
from spacy import displacy
from collections import Counter
import pprint
import en_core_web_sm
nlp = en_core_web_sm.load()
es=Elasticsearch([{'host':'localhost','port':9200}])
print(es)



def index_files_into_elasticsearch():
    directory="/home/shashank/Intelligent Parameters"
    i=1

    for files in os.listdir(directory):
      files_path=os.path.join(directory,files)
      temp=parser.from_file(files_path,xmlContent=True)
      temp_content=temp['content']


      #file_name.append(files_path)
      print(temp_content)
      # doc=nlp(temp_content[0:1500])
      # print(files)
      # for X in doc.ents:
      #     if(X.label_== 'PERSON'):
      #       i=0


      # temp_es={
      #     "file_name":files_path,
      #     "file_content":temp_content
      # }
      # res=es.index(index="parameter2",doc_type='pdf',body=temp_es,id=i)
      # i=i+1
      # print(res)
      #
      # print(i)
      print("New File\n")


#index_files_into_elasticsearch()

