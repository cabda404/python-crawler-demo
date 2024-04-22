import time
import requests


for page in range(1, 11):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Referer": f"https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1713700252&keyword=&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=1&pageNum={str(page)}&requestId=2a6b51f7426baa7d5995f3cd7a64c4a9&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb&u_atoken=33ca0bd6-69de-4276-9993-08f33f6df589&u_asession=01lOL02EnsTNr0FI0sCc0Dr3bNsNsF9aCXNnzUAktJmfe40d5Kckpt6YSiUyOiDRgTfcWKOBECpU3HwO65WZhAftsq8AL43dpOnCClYrgFm6o&u_asig=05fuxXBjFy9WSzPTqC0P4yv_Yz7il2u7ZSSKYz-BZ-l8OmlMkKm63yHeN5LW-dBHNKAu4MYoS7adxUh9KynI-CoD-pRC6eJKoJSwU_K9LGm-yu5eXCLDJ7tTtDhteQFjjz7DAbgFCJ-Je4soYW_sIQit2eRFBFNx4c8EZV3g5_AASVW4hmskRIo3x425F9UKFnksmHjM0JOodanL5-M1Qs1fXvJFRDUkaUAppxCwj_XMt-szP66ZzXdWKBdA2dGH8XFQkc8XjkiKrK_5pg5he8PzUhJKI6w7KH5Ki5r2_VDDDUpLHxH1iRKZmnjAu0Zefw&u_aref=rDhSk1Czj3mnAIQm%2F%2FHmwqUuucI%3D",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "guid": "24f03a1946781ac1b062ea4cb3efd438",
        "acw_sc__v2": "662667f2ec8ea52115f12b265effa299b0f3632d"
    }
    url = "https://we.51job.com/api/job/search-pc"
    params = {
        "api_key": "51job",
        "timestamp": int(time.time()),
        "keyword": "",
        "searchType": "2",
        "function": "",
        "industry": "",
        "jobArea": "000000",
        "jobArea2": "",
        "landmark": "",
        "metro": "",
        "salary": "",
        "workYear": "",
        "degree": "",
        "companyType": "",
        "companySize": "",
        "jobType": "",
        "issueDate": "",
        "sortType": "1",
        "pageNum": str(page),
        "requestId": "2a6b51f7426baa7d5995f3cd7a64c4a9",
        "pageSize": "20",
        "source": "1",
        "accountId": "",
        "pageCode": "sou|sou|soulb",
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.text)
    print(response)