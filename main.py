from Services import ClientService
import datetime

# Resource is the type of DB service

client_service = ClientService()

client_data = {
    'name': 'Melisa Joan Hart',
    'phone': '9341128492',
    'email': 'melisajoanhart@gmail.com',
    'address': 'Calle 23 #123'
}

client_service.create_row('cusomer#5', 'profile#5', 'customer', client_data)
print("Item insertado correctamente")

result = client_service.get_row('customer#1', 'profile#1')

if result is not None:
    print(result['Item'])
    print("Parsed data:", result['Item']['data']['name'])
    print("Parsed data:", result['Item']['data']['phone'])
    print("Parsed data:", result['Item']['data']['email'])