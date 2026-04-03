# Proxy Service (Forward Requests)
import httpx

async def forward_request(method: str, url: str, data=None, headers=None):
    
    async with httpx.AsyncClient() as client:
        
        if method == "GET":
            response = await client.get(url, headers=headers)
        
        elif method == "POST":
            response = await client.post(url, json=data, headers=headers)
        
        elif method == "PUT":
            response = await client.put(url, json=data, headers=headers)
        
        elif method == "DELETE":
            response = await client.delete(url, headers=headers)

    return response.json()