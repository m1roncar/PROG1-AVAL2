#           3ª QUESTÃO          #

from sys import stdin
import re

def main():
    while True:
        
        words = stdin.readline().strip()

        if words == '':
            break
        else:
            pass

        person = ''
        tense = ''

        verb_list = re.compile(r'[o]$|[e]+[i]$|[a]+[i]$|[o]+[s]$|[e]+[s]$|[a]+[i]+[s]$|[a, e, i]$|[o]+[m]$|[e]+[m]$|[a]+[e]+[m]$|[o]+[n]+[s]$|[e]+[s]+[t]$|[a]+[i]+[s]+[t]$|[a]+[m]$|[i]+[m]$|[a]+[i]+[m]$')
        
        infinitive = str(re.split(verb_list, words)).replace('[', '').replace(']', '').replace(',', '').replace("'", "").replace("\n", "").strip()
        
        for i in words:
            if re.search(r'[o]$|[o]+[s]$|[a]$|[o]+[m]$|[o]+[n]+[s]$|[a]+[m]$', words):
                tense = ' presente,'
            if re.search(r'[e]+[i]$|[e]+[s]$|[e]$|^[a]+[e]+[m]$|[e]+[s]+[t]$|^[a]+[i]+[m]$', words):
                tense = ' pretérito,'
            if re.search(r'[a]+[i]$|[a]+[i]+[s]$|[i]$|[a]+[e]+[m]$|[a]+[i]+[s]+[t]$|[a]+[i]+[m]$', words):
                tense = ' futuro,'
            if re.search(r'[o]$|[e]+[i]$|[a]+[i]$', words):
                person = ' 1a pessoa'
            if re.search(r'[o]+[s]$|[e]+[s]$|[a]+[i]+[s]$', words):
                person = ' 2a pessoa'
            if re.search(r'[a, e, i]$', words):
                person = ' 3a pessoa'
            if re.search(r'[o]+[m]$|[e]+[m]$|[a]+[e]+[m]$', words):
                person = ' 4a pessoa'
            if re.search(r'[o]+[n]+[s]$|[e]+[s]+[t]$|[a]+[i]+[s]+[t]$', words):
                person = ' 5a pessoa'
            if re.search(r'[a]+[m]$|[i]+[m]$|[a]+[i]+[m]$', words):
                person = ' 6a pessoa'

        if not re.search(verb_list, words):
            print (words + ' - não é um tempo verbal')
        else:
            print (words + " - verbo " + infinitive +'en'+',' + tense + person)

if __name__ == '__main__':
    main()