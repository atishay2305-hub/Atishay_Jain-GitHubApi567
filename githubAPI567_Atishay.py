#Homework 04a - Develop with the Perspective of the Tester in mind
# Author: Atishay Jain
# Date: 7th October 2022

from itertools import count
from unicodedata import name
from urllib import response
import requests
import json

def Github(user_ID):
    try:

        last = requests.get('https://api.github.com/users/' + user_ID + '/repos')

        # output should go in https://api.github.com/users/<user_ID>/repos

        # repo_comm = input("Enter the repo")

        #output should go in https://api.github.com/repos/<user_ID>/<repo_comm>/commits
        #default values i used for saving time: user_ID='atishay2305-hub'
        #default values i used for saving time: repo_comm='Atishay_Jain-GitHubApi567'

        # last = requests.get('https://api.github.com/repos/'+user_ID+'/'+repo_comm+'/commits')

        last = requests.get('https://api.github.com/users/'+user_ID+'/repos')

        
        print("Now printing ")
        for x in enumerate(last.json()):
            print(x["name"],end="----------------- ")
            commit_data = requests.get('https://api.github.com/repos/'+user_ID+'/'+x["name"]+'/commits')
            repo_num += repo_num
            
            tempTotal=0
            for index,z in enumerate(commit_data.json()):
                tempTotal=tempTotal+index
                final_val = "this is "+tempTotal
                print(final_val) 
            return True 
           #added return value as "True" and printed the "final_val" as in the previous function i created i just printed the output which was not correlating with the mock function.
    
    except:
        print("Incorrect Inputs")


if __name__ == "__main__":
    user_id = input('Enter the userid: ')
    Github(user_id) 
