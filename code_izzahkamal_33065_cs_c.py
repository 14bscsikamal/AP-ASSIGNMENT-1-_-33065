#izzah kamal
# reg # 33065
import json
import string
import csv
import re

#getting keys of dictionary
dicwords=((json.loads(open("dictionary.json").read())).keys())
set_list=list()
#assigning two letter words from dictionary to list having no special characters
for dic in dicwords:
    if len(dic)==2:
        if re.match("^[a-zA-Z0-9]*$",dic):
            set_list.append(dic)
# generating a graph connecting words which differ in one letter
graph={}
#if a word is present in list of two letter words list
def is_present(word):
    return set(wrd for wrd in word if wrd in set_list)
#making list of words differ in one letter
def letter(word):
    #spliting
    s=((word[:wrd],word[wrd:]) for wrd in range(len(word)+1))
    #replacing
    p=(x+y+z[1:] for x,y in s for z in string.ascii_uppercase if z if z not in x+y+z[1:])
    return set(p)
#assigning each word (a key of graph) a set of list as values 
for wrd in set_list:
    graph[wrd]=(is_present(letter(wrd)))
print(graph)
#searching path for source and destination
def search_p(graph,source,destination):
    queue=[(source,[source])] #inserting source in queue
    while queue:#while queue is not empty
        (vertex,path)=queue.pop(0)#popinf first element
        for next in graph[vertex]-set(path):#if element has next node
            if next==destination:#and next node is destination
                yield path+[next]#add node to path
            else:#else keep traversing through queue
                queue.append((next,path+[next]))
                

#returning shortest path from search_p^ function 
def pth (gph,source,destination):
    try:
        return next(search_p(gph,source,destination))
    
    except StopIteration:
        return None
#functions to find chain through hamming distance
def searchchain(word1,word2,set_list):
 if(word1==word2):
  print 'Source and destination are same'
 finallist=[word1]
 dict1={}
 list3=['c']
 while (word1!=word2):
   
   for n in range(len(word1)):
     
     word4=word1
     if(word1[n]!=word2[n]):
        
        b_s=bytearray(word1)#converting string to byte and swaping letter of wotd
        b_c=bytearray(word2)
        b_s[n]=b_c[n]
        word1=str(b_s)#converting back from byte to string
        word2=str(b_c)
        
        for x in list1:
           
           if word1==x:
             word1=x
             finallist.append(word1)
             break
        else :
             word1=word4
#passing words from list to search shortest path
for wrd in range(len(set_list)):
    a=wrd+1
    while a<(len(set_list)):
        word1=set_list[wrd]        
        word2=set_list[a]
        if(pth(graph,word1,word2)) is None:
            print('none')
            break;
        else:
         print('here')
         finallist=pth(graph,word1,word2)

         dict1={}
         xyz=len(finallist)-1
         dict1[str(finallist)]=xyz
         print(dict1)

         with open('myfile.csv','a') as foo:
                w=csv.writer(foo)
                w.writerows(dict1.itms())
                foo.close()
                a+=1
print('done')                

                

    



            
