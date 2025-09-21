name=input("Enter Your Name : ")
age=int(input("Enter Your Age : "))
mobile_num = input("Enter Your Phone Number : ")
#id_generated = name[:2].upper mobile_num[-4:0]
print(f"Hello {name}, Welcome to Voting Application")
if age <= 18 :
    print("Age is OK")
else:
    print("Not Accepted")
