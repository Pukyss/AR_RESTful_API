import requests

#Pick one to add to the code or use input.
#d_Word = "wood"
d_Word = input("please enter the a word for definition:\n")

#Simple Get Function
def GetData(d_Word, web):
        url = web + d_Word
        payload, headers = {}, {}
        return(requests.request("GET", url, headers=headers, data=payload).json())

#Runs Get Restful API for getting word details.
j = GetData(d_Word, "https://api.dictionaryapi.dev/api/v2/entries/en/")
if type(j) != dict:
    print("origin of the word " + d_Word +  " is:\n"+ j[0]["origin"] + "\n")
    print(d_Word + " definition in a sentence:\n" + j[0]["meanings"][0]["definitions"][0]["definition"] + "\n")
    print(d_Word + " example in a sentence:\n" + j[0]["meanings"][0]["definitions"][0]["example"] + "\n")
    print(d_Word + " synonyms:") 
    print(j[0]["meanings"][0]["definitions"][0]["synonyms"]) 
else: print("No Definitions Found")

#Runs Get Restfull API for getting companies details
j = GetData(d_Word, "https://autocomplete.clearbit.com/v1/companies/suggest?query=")
for i in range(len(j)):
    if i == 0: print("\nName/s and domains of available companies at USA with word: " + d_Word) 
    print("Name: " + j[i]["name"])
    print("Domain: " +  j[i]["domain"])

    
