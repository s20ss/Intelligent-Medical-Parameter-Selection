#import requests
from Bio import Entrez
import urllib3

def search(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pmc',
                            sort='relevance',
                            retmax='20',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results

def download_file(download_url):
    response = urllib3.PoolManager().request('GET',download_url)
    file = open("/home/shashank/Intelligent Parameters" + '/'+ str(id.upper())+'_PMC_NCBI.pdf', 'wb')
    file.write(response.read())
    file.close()
    print("Completed")


if __name__ == '__main__':
    results = search('breast cancer')
    print(type(results))
    id_list = results['IdList']
    print(id_list)

    for id in id_list:
        print('http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/' % (id.upper()))
        #########################################
        download_file('http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/' % (id.upper()))





        #Downloading PDFs from PMC in NCBI
        #url = 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/pdf/'
        #r = requests.get(url, stream=True)
        #print(r.content)
        # dir="/home/shashank/Intelligent Parameters" + '/'+ str(id.upper())+'_PMC_NCBI'+'.pdf'
        # with open(dir,'wb') as f:
        #     f.write(r.content)