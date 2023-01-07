import http.client

conn = http.client.HTTPSConnection("whatsapp-api5.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "39d091b989mshe16cca78af3bc0ap195c9ajsn2d6c7fed9a43",
    'X-RapidAPI-Host': "whatsapp-api5.p.rapidapi.com"
    }

conn.request("GET", "/api/v2/qrcode/?base64=false", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))