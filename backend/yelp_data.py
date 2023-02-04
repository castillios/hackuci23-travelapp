import http.client

conn = http.client.HTTPSConnection("api.yelp.com")

payload = ""

headers = { 'Authorization': "Bearer p50ITgphUvksSaf_a2ENswHKJscwJhR5ps0p00g7nfU8SBeBupjw6bfhaIoyLXygUzlKoN6XFxTvU4JTObchhULslD1PKiSLUf4TcYvhA5uhgI5c9c2Q4ICDsw_eY3Yx" }

conn.request("GET", "/v3/businesses/search?location=irvine&term=korean", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))