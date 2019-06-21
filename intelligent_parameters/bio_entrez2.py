#import requests
from Bio import Entrez
import urllib3
from urllib.request import urlretrieve
def search(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pmc',
                            sort='relevance',
                            retmax='20',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results

def download_file(download_url,id):
    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', download_url, preload_content=False)
    chunk_size=2000
    with open('/home/shashank/Intelligent Parameters/'+id+'.pdf', 'wb') as out:
        while True:
            data = r.read(chunk_size)
            if not data:
                break
            out.write(data)

    r.release_conn()
    return 0


def search_and_download_file(query):
    results = search(query)
    id_list = results['IdList']
    for id in id_list:
        print('http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/' % (id.upper()))
        #########################################
        download_file('http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/' % (id.upper()),id.upper())

#
# if __name__ == '__main__':
#     results = search('breast cancer')
#     print(type(results))
#     id_list = results['IdList']
#     print(id_list)
#
#
#     for id in id_list:
#         print('http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/' % (id.upper()))
#         #########################################
#         download_file('http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/' % (id.upper()),id)





        #Downloading PDFs from PMC in NCBI
        #url = 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/'
        #r = requests.get(url, stream=True)
        #print(r.content)
        # dir="/home/shashank/Intelligent Parameters" + '/'+ str(id.upper())+'_PMC_NCBI'+'.pdf'
        # with open(dir,'wb') as f:
        #     f.write(r.content)