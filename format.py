import pandas as pd
import uuid
from re import search

df = pd.read_excel("data/inputfile-for-test-batch.xlsx")
data = df['result']


def data_format():
    arr = []
    for a in data:
        a = a.split('{')

        latest_city = [x for x in a if search('city', x)]
        latest_postcode = [x for x in a if search('postcode', x)]
        latest_suburb = [x for x in a if search('suburb', x)]

        # road = [x for x in a if x.startswith('road')]
        city_district = [x for x in a if x.startswith('city_district')]
        state_district = [x for x in a if x.startswith('state_district')]
        final = [x for x in a if not x.startswith('state') and not x.startswith('postcode') and not x.startswith('city')]

        dct={}
        dct['id'] = str(uuid.uuid4())

        address_str = ''

        if len(latest_suburb) > 0:
            dct['address'] = latest_suburb[-1].split('suburb')[-1].strip()
        elif len(city_district) > 0:
            dct['address'] = city_district[-1].split('city_district')[-1].strip()
        elif len(state_district) > 0:
            dct['address'] = state_district[-1].split('state_district')[-1].strip()
        else:
            for i in final:
                k = i.split(' ', 1)
                if len(k) == 2:
                    address_str += k[1]
            dct['address'] = address_str


        if len(latest_city) > 0:
            dct['city'] = latest_city[-1].split('city')[-1].strip()



        # if len(city_district) > 0:
        #     address_str += city_district[-1].split('city_district')[-1].strip()
        #
        # if len(state_district) > 0:
        #     address_str += state_district[-1].split('state_district')[-1].strip()

        # dct["address"] = address_str.replace(']', '')

        if len(latest_postcode) > 1:
            dct['postcode'] = latest_postcode[-1].split('postcode')[-1].strip()
        else:
            dct['postcode'] = latest_postcode[0].split('postcode')[-1].strip() if len(latest_postcode) > 0 else ''

        arr.append(dct)
    df2 = pd.DataFrame(arr)
    return df2

my_xl = data_format()
my_xl.to_excel("demo_11.xlsx", sheet_name='test')
