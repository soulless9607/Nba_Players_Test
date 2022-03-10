import json
from urllib.request import urlopen
from collections import defaultdict


def search_players(total):
    #Gather data from HTTP request 
    url = "https://mach-eight.uc.r.appspot.com/"
    response = urlopen(url)
    data = json.loads(response.read())
    nba_players = data["values"]

    #Iterate in list, i is the first player and j the second player. 
    default = defaultdict(list)
    for i in nba_players:
        default[int(i['h_in'])].append(i['first_name'] + " " + i['last_name'])
    return [i + " and " + j
        for height in default
            if total - height in default
                for j in default[total - height]
                    for i in default[height]
                        if i < j
    ]
    return results

#Input the value, execute the function, recognize matches.
height_input = int(input("Height value: "))
result = search_players(height_input)

if len(result) == 0: 
    print("No matches found \n")
else:
    print(result) # Algorithm will have linear time if the input has no players with the same height, that is the best case time complexity, the worst one is going to be O(n²)
