from maclookup import ApiClient
#import logging

client=ApiClient('at_jsPLyLDQnR49h77YtyKAwXtMAlIJk')
#logging.basicConfig(filename='myapp.log',level=logging.WARNING)

print(client.get_raw_data('3c:a6:f6:34:b1:98','csv'))
"""print(client.get_vendor('44:38:39:ff:ef:57'))
print(client.get('44:38:39:ff:ef:57'))

response=client.get('44:38:39:ff:ef:57')
print(response.vendor_details.is_private)
print(response.block_details.date_created)
print(client.get_vendor('44:38:39:ff:ef:57'))"""