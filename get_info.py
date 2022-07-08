import requests
 
url = "https://leetcode-stats-api.herokuapp.com/"
user_list = ['raphael-lhs']
def get():
    res = []
    for user in user_list:
        temp = requests.get(url + user)
        res.append({'Username':user,'TotalSolved':temp.json()['totalSolved']})
        
    #print(res)
    return res

