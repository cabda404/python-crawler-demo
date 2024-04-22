import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "From-Domain": "51job_web",
    "Referer": "https://we.51job.com/pc/search?keyword=&searchType=2&sortType=1&metro=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "account-id": "",
    "partner": "",
    "property": "%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3Fkeyword%3D%26searchType%3D2%26sortType%3D1%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D",
    "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sign": "4c208dcbbd81fc0d7e76d3a030b1f4450feabb27658acdd1fb0cd54b059fc9aa",
    "user-token": "",
    "uuid": "24f03a1946781ac1b062ea4cb3efd438"
}
cookies = {
    "NSC_ohjoy-bmjzvo-200-159": "ffffffffc3a0d61945525d5f4f58455e445a4a423660",
    "sajssdk_2015_cross_new_user": "1",
    "guid": "24f03a1946781ac1b062ea4cb3efd438",
    "nsearch": "jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D",
    "search": "jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2224f03a1946781ac1b062ea4cb3efd438%22%2C%22first_id%22%3A%2218effee5dba1082-08c1d7f7926fab8-26001d51-1327104-18effee5dbb220c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThlZmZlZTVkYmExMDgyLTA4YzFkN2Y3OTI2ZmFiOC0yNjAwMWQ1MS0xMzI3MTA0LTE4ZWZmZWU1ZGJiMjIwYyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjI0ZjAzYTE5NDY3ODFhYzFiMDYyZWE0Y2IzZWZkNDM4In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2224f03a1946781ac1b062ea4cb3efd438%22%7D%2C%22%24device_id%22%3A%2218effee5dba1082-08c1d7f7926fab8-26001d51-1327104-18effee5dbb220c%22%7D",
    "acw_sc__v2": "6624fb6f47b6edc337bce9c0107eb24611e3a9c1",
    "partner": "www_baidu_com",
    "seo_refer_info_2023": "%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DQmUuCrfg30nnSh9k_1Prk4aXSXu6OYiMPHcmJXGTuVWMk0muuqtMho5MCdTswZTg76Ph-C_sp6TYuw2GKOJutK%26wd%3D%26eqid%3Df6ae4c0c01129911000000056624fdd8%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2Fhangzhou%5C%2Fhj35002762%5C%2F%22%2C%22landHost%22%3A%22jobs.51job.com%22%2C%22partner%22%3Anull%7D",
    "jobs_search_req": "27f833fd4965c831f0394dd7c7959fde",
    "Hm_lvt_1370a11171bd6f2d9b1fe98951541941": "1713700335",
    "Hm_lpvt_1370a11171bd6f2d9b1fe98951541941": "1713700335",
    "acw_tc": "ac11000117137005103006829e00e0040fc79175b62f69309ed2b4a565d706",
    "JSESSIONID": "B8A2D3EC1CC6A76F0BA029EB8E1EB24E",
    "ssxmod_itna": "mqGOGK4mxjxUxeq0LueKxu0KiI4NG=hrGEYxx05ei=bDSxGKidDqxBmnlxDteb3F0+DN5EK+xPd=EB2B0fpQ+bYacsoxCPGnDBIoWQmDYAkDt4DTD34DYDixib1xi5GRD0KDF7dy/1yDYPDE0KDaxDbDiekIxGCDeKD0PuFDQKDuZKxDG5xzb0xQQKKeIBF=FHpuhr+iDxkD7ypDlPdubDkrbL6ejH+jSfGE7KDXrQDv1H1lcapDBRkZhvGDxp45Y2N30wejj+YlGioNhbA/BWqtYrx3QGMtY9e5mneeDDWiiGPMdD==",
    "ssxmod_itna2": "mqGOGK4mxjxUxeq0LueKxu0KiI4NG=hrGEDn9ERDDtDlgAxjb5i=eRC+2QUi3RtYL5eYR0mucDOcKS+ai8eGPPRnIDLg4obL/mxmY7EU0P9PGFQ3ndSjQTVU1ThXiMGEQMdOiur8K7xXMAgwVG46p3SoOWk=KTQoedbIVKeXsGjN6UQEIiTAx9f2i1xYCn45CReYFAeqF0AjwFSPwj8x83bhXi6HRtpQw0rFm0oiTpxvVQ9oh0gpvoT8X8S7HST6m8/GsP1B4Tza2nK46DbkPBPoybfNCe=MjAf1r2qzjknYrPfZAc5tjMFT2Y6L54QoGMNGMPjqY3BC3dY+41qnPZuY8g1mrz0ObbfrD2ddrk823hem6krq4oC4p+ST+C3aQGDn3sqGIep=epsYOAEd1LGRldDP7AQ+fC3BAzVCzAqoBWEtPtPCsPpAQZr8LCtBN6uQspIiAk8Pt6Tk+4jGgDvDDwEGqQG8Dxs7eQDLwAxA04h8KPiQije5WwqmGXOecPBxAAQ1bQCG/DgCaeKWwx0LHPgwmG0l=+gD+axCCDFADX+Bwe8tsbKYLTIDovGIBDKCDl8yGiDOTD8kdrqPYTEke8KvkY5l37eFiDDjKDewGt7DeKqPUQ3GPIW1z65eiil8yqGxc6Y6AQcAKOXliDX++DpKqezhVBD4D===",
    "tfstk": "f2KZt1Ohkcna1HLcT6sVzXNINrSOFghSun1fnKvcC1fgfALUxtO11xpm6I-VtKx1s1MO0ZADsI7xBs1cgI9D5viSVdpODifqN0iW6iujOErGioD0xtVDQWTEVdpTKtbD92n7u9ynyx5DiNj3tt1hISqDiwqhH6qGnlX0tvWAtsjcotXnxTWVIR4igZ5cNkWPSfi8PucjH-DlidfU4pKGIDBx2Oq0mHWwLX9CTO66YO7NZwsNSYxMOKx6Xw3aSipBzI8DZXa1sUWyTaTZalRy6tvVnCo8U6xw3H79R54GUG5NrhbaFYpCoe-FfhcYyp9FsaSBR2h1lGRwy_QiJXd2L1ODbwVZOsTWdhbeZXZeMZ8DfMxit0SymSB3cIKv7S4VS9BFNvk3PxZWe3b7QXaYkNLdL_MtBrUAS9BFNvkUkrQ9J95SBAC.."
}
url = "https://we.51job.com/api/job/search-pc"
params = {
    "api_key": "51job",
    "timestamp": "1713700759",
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
    "pageNum": "1",
    "requestId": "2a6b51f7426baa7d5995f3cd7a64c4a9",
    "pageSize": "20",
    "source": "1",
    "accountId": "",
    "pageCode": "sou|sou|soulb"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)