n=int(input("Enter the number of items purchased: "))
itemname=[]
itemqty=[]
itemprice=[]
for i in range(n):
    name=input(f"Item Name {i+1}: ")
    price=float(input(f"Item Price {i+1}:Rs.  "))
    qty=int(input(f"Item Quantity {i+1}: "))
    print("-----------------------------------------")
    itemname.append(name)
    itemprice.append(price)
    itemqty.append(qty)
print("***********************BILL***********************"
      "\nITEM NAME     ITEM QUANTITY    RATE     ITEM PRICE\n")
total=0
for i in range(n):
    print(f"{itemname[i]}"
          f"\t\t\t  {itemqty[i]} "
          f"\t\t\t{itemprice[i]}"
          f"\t\t\t{itemprice[i]*itemqty[i]}\n")
    total+=(itemprice[i]*itemqty[i])
print("**************************************************"
      f"\nTotal Amount to be Paid: Rs. {total}")