gujarat_cities = [
    "Ahmedabad",
    "Surat",
    "Vadodara",
    "Rajkot",
    "Bhavnagar",
    "Jamnagar",
    "Junagadh",
    "Gandhinagar",
    "Anand",
    "Nadiad",
    "Morbi",
    "Bharuch",
    "Navsari",
    "Vapi",
    "Porbandar",
    "Dahod",
    "Gandhidham",
    "Mehsana",
    "Palanpur",
    "Veraval"
]

maharashtra_cities = [
    "Mumbai",
    "Pune",
    "Nagpur",
    "Nashik",
    "Thane",
    "Aurangabad",
    "Solapur",
    "Kolhapur",
    "Amravati",
    "Jalgaon"
]

rajasthan_cities = [
    "Jaipur",
    "Jodhpur",
    "Udaipur",
    "Kota",
    "Ajmer",
    "Bikaner",
    "Alwar",
    "Bhilwara",
    "Sikar",
    "Pali"
]

karnataka_cities = [
    "Bengaluru",
    "Mysuru",
    "Mangaluru",
    "Hubballi-Dharwad",
    "Belagavi",
    "Kalaburagi",
    "Ballari",
    "Davangere",
    "Vijayapura",
    "Shivamogga"
]


# print(len(gujarat_cities))

count = 0
# i = 0

print("1 for gujrat\n2 for maharatra\n3 for rajsthan\n4 for karnataka")
choise = int(input("enter your choise : "))
name = []
if choise==1:
    name = gujarat_cities

elif choise==2:
    name = maharashtra_cities
    
elif choise == 3:
    name = rajasthan_cities
    
elif choise ==4:
    name = karnataka_cities

while count < len(name):
    print(name[count],end=" ")
    #increment
    count+=1     # count = count+1 
    # i+=1           # i = i+1
    

# if while loop not contain increment or decrement then infinite loop occurs
    # count = count-1    #decrement

# print(gujarat_cities[1])
# print(gujarat_cities[2])
# print(gujarat_cities[3])