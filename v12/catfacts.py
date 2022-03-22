import requests
import random

def get_random_cat_fact():
        cat_facts_data = requests.get('https://cat-fact.herokuapp.com/facts')
        cat_facts = cat_facts_data.json()

        random_cat_fact = random.choice(cat_facts)
        return random_cat_fact["text"]
