

from googlesearch import search
query = "Geeksforgeeks"

for result in search(query, tld="co.in", num=1, stop=1, pause=0):
    print(result)