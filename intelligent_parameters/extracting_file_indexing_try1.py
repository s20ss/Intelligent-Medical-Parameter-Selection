import os
from elasticsearch import Elasticsearch
import json
from tika import parser
import spacy
from spacy import displacy
from collections import Counter
import pprint
from lxml import etree
from bs4 import BeautifulSoup
import en_core_web_sm
nlp = en_core_web_sm.load()
es=Elasticsearch([{'host':'localhost','port':9200}])
print(es)
#print(es.indices.delete(index='parameter', ignore=[400, 404]))
#print(es.index(index='parameter',doc_type='pdf',body={
#    "index.mapping.total_fields.limit": 2000
#}))
def index_files_into_elasticsearch():
    directory="/home/shashank/Intelligent Parameters"


    for files in os.listdir(directory):

      temp_dict={}
      string_of_authors=""
      files_path=os.path.join(directory,files)
      print(files_path)
      temp_dict["file name"]=files_path
      temp=parser.from_file(files_path,xmlContent=True)
      temp_content=temp['content']
      #print(temp_content)
      soup = BeautifulSoup(temp_content, 'html.parser')
      #print(soup)
      all_meta=soup.find_all('meta')
      for meta in all_meta:
          if(meta['name']=='date'):
              date=meta['content']
          if(meta['name']=='Author'):
              print(meta['content'])
              string_of_authors=string_of_authors+" "+ str(meta['content'])
          if(meta['name']=='Keywords'):
              keywords=meta['content']
      all_div=soup.find_all('div')
      i = 1
      for div in all_div:
          #print(div)
          #print("New")
          if 'page' in div['class']:
              all_p=div.find_all('p')
              #print(all_p)

              for p in all_p:
                  #print(p)
                  #print(p.get_text())
                  temp_text=p.get_text()
                  #print(temp_text)
                  temp_text=temp_text.rstrip()
                  temp_text=temp_text.lstrip()
                  temp_text=temp_text.replace('\n','')
                  #print(temp_text)
                  if(len(temp_text)>=50):
                    #print(temp_text)
                    temp_dict[i]=temp_text
                    i=i+1
      #print(temp_dict)
      temp_dict["keywords"]=keywords
      temp_dict["date"]=date
      temp_dict["Authors"]=string_of_authors
      #print(keywords,string_of_authors,date)
      temp_es=temp_dict
      res=es.index(index="parameter",doc_type='pdf',body=temp_es,id=i)

      print(res)
      #print(temp_dict)





index_files_into_elasticsearch()

