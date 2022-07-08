import requests
 
url = "https://leetcode-stats-api.herokuapp.com/"
 
user_list = ['raphael-lhs']
def get_info(user_list):
    for user in user_list:
        temp = requests.get(url + user)
        print(temp.json())
#print first 4000 characters of response
get_info(user_list)