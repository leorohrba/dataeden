# from ipware import get_client_ip
# import requests

# def get_country_code_from_ip(ip_address, api_key='fb0ffe10b17342615725861c4bd0de41'):
#     url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
#     # url = f'http://api.ipstack.com/{ip_address}?access_key=8481f3f20543580be67d3bce342fa7ff'
    
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         country_code = data.get('country_code')
#         return country_code
#     else:
#         # Log the error message
#         error_message = f"IP lookup failed for IP: {ip_address}, Status Code: {response.status_code}"
#         print(error_message)  # You can use proper logging instead of print
#         return None

# def get_client_location(request):
#     client_ip, _ = get_client_ip(request)  # Ignore the is_routable attribute
#     if client_ip is None:
#         return None

#     # Replace this with your actual function to get the country code
#     country_code = get_country_code_from_ip(client_ip)

#     return country_code
