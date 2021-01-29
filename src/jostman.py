#! /usr/bin/python3
import requests
import json
import os


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

def get(url:str):
    response = requests.get(url=url,headers=headers)
    return response


def post(url:str,data:dict):
    response = requests.post(url=url,headers=headers,data=data)
    return response

def print_results(response: requests.Response) -> None:
    clear()
    print("response status:",response.status_code)
    print("response text:")
    print(response.text)

def check_url(url:str) -> str:
    if url.startswith('http://'):
        return url
    elif url.startswith('https://'):
        return url
    else:
        url = 'http://' + url
        return url

def clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system("cls")
    

def main():
    while True:
        print(" 0 ======= quit program")
        print(" 1 ======= get method")
        print(" 2 ======= post method")
        method = int(input("please choose the mode: "))
        if method == 1:
            url = input("please input the url: ")
            url = check_url(url)
            r = get(url)
            print_results(r)
        elif method == 2:
            url = input("please input the url: ")
            url = check_url(url)
            data = input("please input the data: ")
            data = json.loads(data)
            r = post(url,data)
            print_results(r)
        elif method == 0:
            break
        else:
            print("Invalid input, choose again!")
