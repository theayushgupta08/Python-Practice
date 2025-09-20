qty=float(input("Enter the no. of items sold: "))
cost=float(input("Enter the cost of item: "))
dis=float(input("Enter the discount percentage: "))
tax=float(input("Enter the Tax: "))
amt=qty*cost
disamt=(dis*amt)/100
damt=amt-disamt
taxamt=(tax*amt)/100
totalamt=damt+taxamt
print(f"******************BILL******************"
      f"\nQuantity Sold: {qty}"
      f"\nCost of Item: Rs.{cost}"
      f"\nDiscount: {dis} %"
      f"\nTax Applicable: {tax} %"
      f"\n****************************************"
      f"\nTotal Amount: Rs.{amt}"
      f"\nAmount after Discount applied: Rs.{damt}"
      f"\nGST: {tax} %"
      f"\nAmount to be Paid: Rs.{totalamt}"
      f"\n****************************************")

