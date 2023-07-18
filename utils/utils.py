import json

def read_words():
    """Read JSON Words

    Returns:
        Return a List of dictionaries
    """
    with open('words.json', 'r',encoding='utf-8') as file:
        words = json.load(file) 
    return words