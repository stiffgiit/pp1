facebook = input("facebook = ") == 'true'
twitter = input("twitter = ") == 'true'
instagram = input("instagram = ") == 'true'
if facebook + twitter + instagram >= 2:
    print("A person can be a good influencer!")
else:
    print("A person cannot be a good influencer..")