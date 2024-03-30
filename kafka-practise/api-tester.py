import http.client

conn = http.client.HTTPSConnection("youtube-search-and-download.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "ee16b418f8msh87811de9cafc296p19e793jsn8849f3edbb02",
    'X-RapidAPI-Host': "youtube-search-and-download.p.rapidapi.com"
}

conn.request("GET", "/trending?type=mu&hl=en&gl=US", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))