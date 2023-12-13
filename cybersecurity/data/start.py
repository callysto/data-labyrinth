def start(key):
    """
    Sets up the labyrinth API.
    """
    import requests
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