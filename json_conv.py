import pandas as pd
import json
from collections import Counter 

# from jsonmerge import merge
# from jsonmerge import Merger

df = pd.read_excel("/home/geospoc/Downloads/tagoutput.xls")

result = []

def clean(x):  
    try:
        x = x.replace("'", '"')
        op = json.loads(x)
    except:
        # print(x + '\n')
        op = ''
    finally:
        arr1 = []
        l_n = ''
        tp = []

        for idx, i in enumerate(op):
            # print(i)
            # for k in i:
            output = {
                "long_name":i['long_name'],
                "types": i['types'][0] if len(i["types"]) != 0 and i["types"][0] not in ("political") else i['types'][1] if len(i["types"]) != 0 else ''
            }
            arr1.append(output)
        # print(arr1)
        for idx,k in enumerate(arr1):
            if idx == 0:
                # print(k)
                l_n = k['long_name']
                tp.append(k['types'])
            else:
                l_n = l_n + ", " + k["long_name"]
                tp.append(k["types"])
        print(l_n)
        print(tp)


    return ''

# clean(pass_data)

data = df["address_components"].apply(clean)
# print(data)
# for idx, i in enumerate(data):
#     arr1 = []
#     for k in i:
#         output = {
#             "long_name":k['long_name'],
#             "types": k['types'][0] if len(k["types"]) != 0 and k["types"][0] not in ("political") else k['types'][1] if len(k["types"]) != 0 else ''
#         }
#         arr1.append(output)
#     result.append(arr1)
# df["result"] = result
# print(df['result'])


# df.to_excel("updated.xlsx")

d1 = [
 {'long_name': '324003', 'types': 'postal_code'}, {'long_name': 'Kota', 'types': 'locality'}, 
 {'long_name': 'Kota', 'types': 'administrative_area_level_2'}, {'long_name': 'Rajasthan', 'types': 'administrative_area_level_1'},
 {'long_name': 'India', 'types': 'country'}
]

# r = ''
# for idx,k in enumerate(d1):
#     r = r + " " + k["long_name"]
# print(r)

