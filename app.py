# import csv
# import spacy
import pandas as pd
import json

# nlp = spacy.load('en_core_web_sm')
df = pd.read_excel("/home/geospoc/workspace/spacy_test/updated.xlsx")

# [(0,16,'"Nitya-Nilayam"')|(17,41,'Sri Venkatesa Mills Post')|(42,52,'Udumalpet')|(54,63,'Coimbatore')|(64,81,'Tamil Nadu 642128')|]}),

# temp = 'Nitya-Nilayam, Sri Venkatesa Mills Post, Udumalpet, Coimbatore, Tamil Nadu 642128'

d1 = [
 {'long_name': '324003', 'types': 'postal_code'}, {'long_name': 'Kota', 'types': 'locality'}, 
 {'long_name': 'Kota', 'types': 'administrative_area_level_2'}, {'long_name': 'Rajasthan', 'types': 'administrative_area_level_1'},
 {'long_name': 'India', 'types': 'country'}
]

def clean(x):  
    # print(x)
    try:
        x = x.replace("'", '"')
        k = json.loads(x)
        # print(x)
    except:
        print(x + '\n')
        k = ''

    return ""


def format_texts(txt):
    start = 0;
    num_arr = [0]
    l_n = ''
    tp = []
    str3 = ""
    # print(txt)
    for idx,k in enumerate(txt):
        if idx == 0:
            print(k)
            l_n = k['long_name']
            tp.append(k['types'])
        else:
            l_n = l_n + ", " + k["long_name"]
            tp.append(k["types"])
    print(l_n)
    print(tp)


    for i, e in zip(range(len(txt)), txt):
        if e == ",":
            end = i
            start = end
            num_arr.append(end+2)
    num_arr.append(len(txt))

    print(num_arr)

    output = [txt[i:j].replace(", ","") for i,j in zip(num_arr, num_arr[1:]+[None])]

    for idx,obj in enumerate(num_arr):
        if idx<len(num_arr)-1:
            for item in tp:
                if idx == 0:
                    str2 = "("+str(obj)+ ","+str(num_arr[idx+1]-1) +","+"""'"""+ tp[idx] + """')|"""
                else:
                    str2 = "("+str(obj+1)+ ","+str(num_arr[idx+1]-1) +","+"""'"""+ tp[idx] + """')|"""
            str3 = str3+str2
        else:
            pass

    str4 = "(u"+'''"'''+txt+''' ",'''+"""{'entities': ["""+str3+"""]}),"""
    print(str4)
    return str4

# my_data = df['result'].apply(clean)

format_texts(d1)
# df['output'] = df['result'].apply(format_texts)

# df.to_excel("text_formatter_file_v2.xlsx",sheet_name='test')























# str2 = ""
#doc = nlp(u"Nitya-Nilayam, Sri Venkatesa Mills Post, Udumalpet, Coimbatore, Tamil Nadu 642128, India")
#doc = nlp(u"IT Park Baner Road Baner Pune 411045")

# def format_address_func(params):
#     str3 = ""
#     doc = nlp(params)
#     for ent in doc.ents:
#         str2 = ""

#         str2 = "("+str(ent.start_char)+ ","+str(ent.end_char)+","+"""'"""+ent.text+ """')"""
#         str3 = str3+str2


#     str4 = "(u"+'''"'''+doc.text+''' ",'''+"""{'entities': [ """+str3+"""]}),"""
#     # print(str4)
#     return str4

    # str2 = ""
    # str3 = ""
    # doc = nlp(params)
    # # print(doc)
    # for ent in doc.ents:
    #     # print(ent.text)
    #     print(doc.ents)
    #     str1 = ""
    #     str1 = "("+str(ent.start_char)+ ","+str(ent.end_char)+","+"""'"""+ent.text+ """')"""
    #     # print(str1)
    #     str2 = str2+str1
    # str3 = "(u"+'''"'''+doc.text+''' ",'''+"""{'entities': ["""+str2+"""]}),"""
    # # print(str3)
    # return str3

# format_address_func("12 No.Slum Area, Shahpura, Bhopal, Madhya Pradesh 462039")
# df['output'] = df['address'].apply(format_address_func)

# df.to_excel("latest_spacy_data.xlsx",sheet_name='test')

# print(str4)

# for r in output:
#     for d in str3:
#         d.replace("_",r)
#         break

# dd = [((x, y), z) for x, y in zip(range(len(my_arr)), my_arr) for y in output]

# def format_address_func(params):
#     for ent in doc.ents:
#         str2 = ""

#         str2 = "("+str(ent.start_char)+ ","+str(ent.end_char)+","+"""'"""+ent.text+ """')"""
#         str3 = str3+str2


    # str4 = "(u"+'''"'''+doc.text+''' ",'''+"""{'entities': [ """+str3+"""]}),"""

# for i in range(len(my_arr)):
#     str1 = "("+str(my_arr[i])+ ","+str(my_arr[i+1])+","+"""'"""+""+ """')"""
#     str2 = str2+str1
    
# print(dd)

# [(1,14,'Nitya-Nilayam')(17,41,'Sri Venkatesa Mills Post')(43,52,'Udumalpet')(66,83,'Tamil Nadu 642128')]}),