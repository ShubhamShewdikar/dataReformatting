import pandas as pd
import json


df = pd.read_excel("/home/geospoc/Downloads/testing.xls")

def clean(x):  
    try:
        x = x.replace("'", '"')
        op = json.loads(x)
    except:
        op = ''
    finally:
        start = 0;
        num_arr = [0]
        l_n = ''
        tp = []
        str3 = ""
        arr1 = []
        str2 = ""

        for idx, i in enumerate(op):
            output = {
                "long_name":i['long_name'].replace(",","").replace("  "," "),
                "types": i['types'][0] if len(i["types"]) != 0 and i["types"][0] not in ("political") else i['types'][1] if len(i["types"]) != 0 else ''
            }
            arr1.append(output)

        for idx,k in enumerate(arr1):
            if idx == 0:
                l_n = k['long_name']
                tp.append(k['types'])
            else:
                l_n = l_n + "," + k["long_name"]
                tp.append(k["types"])

        for i, e in zip(range(len(l_n)), l_n):
            if e == ",":
                end = i
                start = end
                num_arr.append(end+2)
        num_arr.append(len(l_n))
        l_n = l_n.replace(","," ")

        for idx,obj in enumerate(num_arr):
            if idx<len(num_arr)-1:
                for item in tp:
                    if idx == 0:
                        str2 = "("+str(obj)+ ","+str(num_arr[idx+1]-2) +","+"""'"""+ tp[idx] + """')|"""
                    else:
                        str2 = "("+str(obj)+ ","+str(num_arr[idx+1]-2) +","+"""'"""+ tp[idx] + """')|"""
                str3 = str3+str2
            else:
                pass

        str4 = "(u"+'''"'''+l_n+''' ",'''+"""{'entities': ["""+str3+"""]}),"""
        # print(str4)
        return str4


df['result'] = df["address_components"].apply(clean)
df.to_excel("final_op.xlsx",sheet_name='test')
