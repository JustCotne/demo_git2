import json
import difflib

def modzebna():
    with open("data.json","r") as file:
        dictionary = json.load(file)
        word= input("sheiyvanet sityva: ").lower()
        if word in dictionary:
            print(f'{word} - {dictionary[word]}')
        else:
            matches= difflib.get_close_matches(word,dictionary.keys(),1,0.6)
            if len(matches) != 0: 
                while True:
                    match_choose = input(f'"{matches[0]}" - am sityvas xom ar gulisxmobdit? (y/n): ').lower()
                    if match_choose == "y":
                        print(f'{matches[0]} - {dictionary[matches[0]]}')
                        break
                    elif match_choose =="n":
                        print("tqven mier sheyvanili sityva ver moidzebna!!!")
                        break
                    else:
                        print("archevani arasworea!!!")
            else:
                print("tqven mier sheyvanili sityva ver moidzebna!!!") 

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
            
