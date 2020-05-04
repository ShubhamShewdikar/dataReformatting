import pandas as pd
import uuid

df = pd.read_excel("data/inputfile-for-test-batch.xlsx")
data = df['result']
def data_format():
    arr = []
    for a in data:
        a = a.split('{')

        latest_city = [x for x in a if x.startswith('city')]
        latest_postcode = [x for x in a if x.startswith('postcode')]
        latest_suburb = [x for x in a if x.startswith('suburb')]
        road = [x for x in a if x.startswith('road')]


        remaining = [x for x in a if not x.startswith('city')]
        final = [x for x in remaining if not x.startswith('postcode')]
        dct = {}
        dct['id'] = str(uuid.uuid4())

        if len(latest_suburb) > 0:
            dct['suburb'] = latest_suburb[-1].split('suburb')[-1].strip()
        else:
            if road:
                dct['suburb'] = road[-1].split('road')[-1].strip()
            else:
                dct['suburb'] = latest_city[-1].split('city')[-1].strip()
        if len(latest_city) > 0:
            dct['city'] = latest_city[-1].split('city')[-1].strip()

        # address_str = ''

        # for i in final:
        #     k = i.split(' ', 1)
        #     if len(k) == 2:
        #         address_str += k[1]
        #     dct["address"] = address_str.replace(']', '')
        if len(latest_postcode) > 1:
            dct['postcode'] = latest_postcode[-1].split('postcode')[-1].strip()
        else:
            dct['postcode'] = latest_postcode[0].split('postcode')[-1].strip() if len(latest_postcode) > 0 else ''

        arr.append(dct)
    df2 = pd.DataFrame(arr)
    return df2

my_xl = data_format()
my_xl.to_excel("test_final_v2.xlsx", sheet_name='test')
