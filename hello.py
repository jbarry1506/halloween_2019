import mysecrets
import urllib3
import requests
import bs4

# original test
print("Hello-ween is almost here!!!")

# test import var from other file
pw = mysecrets.password

# test import function from other file
test_phrase = "IT is gonna get you!"
mysecrets.test_func(test_phrase)

# Bill of Materials
    # Pennywise the clown mask
    # High torque servo
    # manequin head
    # red LEDs for eyes

# TODO:  SET SECURITY ACROSS ALL COMMUNICATION METHODS!!!!
    # SECURITY FIRST SECURITY FIRST SECURITY FIRST
# TODO:  set up and interface with Raspberry Pi camera
    # https://www.youtube.com/watch?v=qk1IVs5B1GI
# TODO:  set up text messaging with pi and twilio
    # https://www.youtube.com/watch?v=Oi37lg_ciJ8
# TODO:  interface Pi with servo
# TODO:  set up website
# TODO:  write REST API to interact with website
# TODO:  set up CI/CD pipeline to Raspberry Pi
# TODO:  interface with LEDs for eyes
    # https://www.youtube.com/watch?v=WLo5Rgvj6qo

# facebook developer page
# https://developers.facebook.com/docs/live-video-api/guides/streaming#broadcast-on-a-page

# fake api calls
# https://jsonplaceholder.typicode.com

# headers
    # bash-3.2$ curl -I  https://jsonplaceholder.typicode.com/posts
    # HTTP/1.1 200 OK
    # Date: Sun, 01 Sep 2019 05:27:21 GMT
    # Content-Type: application/json; charset=utf-8
    # Connection: keep-alive
    # Set-Cookie: __cfduid=d7f7de065dfca58f8c42afea65dade9f71567315641; expires=Mon, 31-Aug-20 05:27:21 GMT; path=/; domain=.typicode.com; HttpOnly
    # X-Powered-By: Express
    # Vary: Origin, Accept-Encoding
    # Access-Control-Allow-Credentials: true
    # Cache-Control: public, max-age=14400
    # Pragma: no-cache
    # Expires: Sun, 01 Sep 2019 09:27:21 GMT
    # X-Content-Type-Options: nosniff
    # Etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
    # Via: 1.1 vegur
    # CF-Cache-Status: HIT
    # Age: 1251
    # Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
    # Server: cloudflare
    # CF-RAY: 50f4d5a78bab557a-ORD

headers = {'X-API-TOKEN': 'your_token_here'}
payload = {'title': 'value1', 'name': 'value2'}

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(r.content )