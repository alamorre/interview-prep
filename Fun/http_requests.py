# Get and Post
# Headers
# Error handling
# Parallel requests
# Sessions
import requests, datetime, json
import asyncio, aiohttp


def post_full_payload():
    try:
        url = f"https://api.chatengine.io/users/{264427}/"
        data = {"username": "adam_smith", "email": "adam_smith@chatengine.io"}
        headers = {'PRIVATE-KEY': '8c63dbce-80a7-455a-890b-9368d16e1dcb'}
        response = requests.patch(url=url, headers=headers, data=data)
        print(response.status_code)
        print(response.headers.__class__)
        print(json.loads(response.text))
    except Exception as e:
        print(f'Error due to: {e.__class__}')

def requests_vs_session():
    def ping_site_helper(client, x: int):
        try:
            url = f'https://scrapethissite.com/pages/forms/?page_num={x}'
            client.get(url)
            print(f'Page {x} done!')
        except Exception as e:
            print("Unable to get url {} due to {}.".format(url, e.__class__))
    
    start = datetime.datetime.now()
    for i in range(0, 21):
        ping_site_helper(requests, i)
    print(f'Request\'s time: {datetime.datetime.now() - start}')

    start = datetime.datetime.now()
    s = requests.Session()
    for i in range(0, 21):
        ping_site_helper(s, i)
    print(f'Session\'s time: {datetime.datetime.now() - start}')

# post_full_payload()



"""
Parallel requests: good to make requests in parallel 
if responses/request dont need to be sequential
"""

def scrape_ex():
    async def get_helper(url, session):
        try:
            response_promise = await session.get(url=url)
            r = await response_promise.read()
            print("Successfully got url {} with resp of length {}.".format(url, len(r)))
        except Exception as e:
            print("Unable to get url {} due to {}.".format(url, e.__class__))
        
    async def ping_site_parallel():
        urls = [f'https://scrapethissite.com/pages/forms/?page_num={x}' for x in range(0,21)]
        session = aiohttp.ClientSession()
        ret = await asyncio.gather(*[get_helper(url, session) for url in urls])
        await session.close()
        print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))
    
    # Run async stuff in sync fashion
    asyncio.run(ping_site_parallel())
scrape_ex()

