import asyncio
import os

if os.path.exists('API.txt'):
    os.remove('API.txt')
if os.path.exists('Database.txt'):
    os.remove('Database.txt')
if os.path.exists('Cache.txt'):
    os.remove('Cache.txt')

def write_file(file_name: str, content: str):
    with open(file_name, "a") as f:
        f.write(f"{content}\n")

def read_file(file_name: str) -> list[dict]:
    try:
        info = list()

        with open(file_name, "r") as f:
            for line in f:
                #Delete space and ","-> list
                tmp = list(line.strip().split(","))
                info.append({"product": tmp[0], "quantity": int(tmp[1]),"price": int(tmp[2])})
        return info
    
    except FileNotFoundError:
        print("Not Found File")

        #Tránh trường hợp file rỗng
        return []

async def fetch_order_source(source_name, delay):
    print(f"From {source_name}")
    await asyncio.sleep(delay)
    order_list = read_file(source_name)
    return order_list

async def calculator_revenue():
    api, database, cache = await asyncio.gather(
        fetch_order_source("API.txt", 3),
        fetch_order_source("Database.txt", 4.5),
        fetch_order_source("Cache.txt", 2)
    )

    merge_order = api + database + cache
    sum_revenue = sum([order['quantity'] * order['price'] for order in merge_order])
    print(f'Revenue: {sum_revenue}')

    max_quantity = 0
    for order in merge_order:
        if order['quantity'] > max_quantity:
            max_quantity = order['quantity']

    max_quantity_order = [order['product'] for order in merge_order if order['quantity'] == max_quantity]
    print(max_quantity_order)

# API
write_file('API.txt', 'Laptop,2,1000')
write_file('API.txt', 'Phone,5,10000')
write_file('API.txt', 'Computer,3,80000')
write_file('API.txt', 'Car,1,10000')
write_file('API.txt', 'Home,1,100000')

# Database
write_file('Database.txt', 'Laptop,1,5000')
write_file('Database.txt', 'Supercar,2,1000000')
write_file('Database.txt', 'Bycle,2,1000')
write_file('Database.txt', 'Keyboard,2,1000')
write_file('Database.txt', 'Mouse,2,1000')

# Cache
write_file('Cache.txt', 'Dog,1,5000')
write_file('Cache.txt', 'Cat,2,1000000')
write_file('Cache.txt', 'Lion,2,1000')
write_file('Cache.txt', 'Elephant,2,1000')
write_file('Cache.txt', 'Monkey,2,1000')

asyncio.run(calculator_revenue())