import json

with open("euro.json", "r", encoding="utf-8") as file:
    a = json.load(file)
    
    b = "Date\tBuying Rate\tSelling Rate"
    print(b)
    print('=' * len(b) + "=======")
    
    

    for rate in a.get('rates', []):
        d = rate.get("effectiveDate")
        e = rate.get("bid")
        f = rate.get("ask")
        print(f'{d}\t {e}\t {f}\t')
    