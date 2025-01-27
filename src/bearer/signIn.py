import requests



def sigh_in():
    url = "https://inr-api-01.ixora-auto.ru/Auth/v1/Token/SignIn"
    payload = {'Login': 'IGAliev',
               'Password': 'Aliev1998',
               'Authorization': '0F705198-3C63-43B0-8FC1-7D9A8C4C2743'}
    files = [

    ]
    headers = {
        'accept': 'text/plain',
        'Authorization': '0F705198-3C63-43B0-8FC1-7D9A8C4C2743'
    }
    response = requests.request(method='POST', url=url, headers=headers, files=files, data=payload)
    response_json = response.json()
    return response_json.get('Access')




def main():
    print(sigh_in())

if __name__ == '__main__':
    main()