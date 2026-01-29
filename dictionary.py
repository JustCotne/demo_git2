import json
import difflib

def modzebna():
    with open("data.json","r") as file:
        dictionary = json.load(file)
        word= input("sheiyvanet sityva: ").lower()
        if word in dictionary:
            print(f'{word} - {dictionary[word]}')
            
        

def damateba():
    with open('data.json',"r") as file:
        dictionary = json.load(file)
    key= input("sityva: ")
    if key not in dictionary:
        with open('data.json',"w") as file:
            value=input("ganmarteba: ")
            dictionary[key]=value
            json.dump(dictionary,file,indent=2)
    else:
        print("aseti sityva ukve arsebobs.")

def washla():
    with open('data.json',"r") as file:
        dictionary = json.load(file)
    key= input("romeli sityvis washla gsurt: ")
    if key in dictionary:
        with open('data.json',"w") as file:
            del dictionary[key]
            json.dump(dictionary,file,indent=2)
    else:
            print("aseti sityva ar arsebobs.")
            
