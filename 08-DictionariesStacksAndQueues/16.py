Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    names = ", ".join(hotel["name"] for hotel in hotels)
    return names

def avg_price(hotels):
    prices = [hotel["price"] for hotel in hotels]
    return sum(prices)/len(prices)
    
a = hotel_list(Hotels_in_Krakow)
print("Hotels in Krakow: ", a)

        
        
b = avg_price(Hotels_in_Krakow)
print("Average hotel price in Krakow: ", b) 
c = hotel_list(hotels_in_Sopot)
print("Hotels in Sopot: ", c)

        
        
d = avg_price(hotels_in_Sopot)
print("Average hotel price in Sopot: ", d) 

       
        
        