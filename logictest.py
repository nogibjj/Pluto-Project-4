import wikipedia

def wiki(name="War Goddness", length = 1):
    my_wiki = wikipedia.summary(name,length)
    return my_wiki

def wiki_search(name):
    """ Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results

