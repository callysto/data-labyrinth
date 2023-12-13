def start(key):
    """
    Sets up the labyrinth API.
    """
    import requests
    import pandas as pd
    import gzip
    import io
    import json
    import plotly.express as px
    from IPython import get_ipython
    def check(query):
        try:
            r = requests.get('https://script.google.com/macros/s/AKfycbyNwWgQZCm7MR0HmNAat5nqnbWxc8YviiwZfiVXW4NNQLdPRjVHgLP3DSVKUmyvY3OE/exec?room=Cybersecurity&query='+str(query))
            response = r.json()
            get_ipython().run_cell_magic('markdown', '', response['markdown'])
            get_ipython().set_next_input(response['code'])
        except:
            print('Make sure you have entered your answer correctly.')
            get_ipython().set_next_input("check('')")
    check(key)

def cleaning(df):
    """
    Cleans the data.
    """
    import pandas as pd
    import json
    def make_dict(the_string):    
        a_dict = {}
        split_list = the_string.replace('{','').replace('}','').split('":')
        key = split_list[0].replace('"','')
        for item in split_list[1:]:
            item = item.replace('"','')
            split_by_commas = item.split(',')
            if len(split_by_commas) > 2:
                key = split_by_commas[-1]
            else:
                value = split_by_commas[0]
                a_dict[key] = value
            try:
                key = split_by_commas[-1]
            except:
                a_dict[key] = value
                print('done')
        return a_dict

    for_new_df = []
    for row in df['_raw']:
        try:
            j = json.loads(row)    
        except:
            j = make_dict(row)
        for_new_df.append(j)
        
    data = pd.DataFrame(for_new_df)
    return data