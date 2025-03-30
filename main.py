def calculate_discount():
    price = float(input("Enter original price: "))
    discount_percent = int(input("Enter discount percantage e.g 10, 20... : "))
    if discount_percent >= 20:
        discount_amount = (price * (discount_percent / 100))
        new_price = price - discount_amount
        final_price =  new_price
        print(f"Discount applied! Final Price: {final_price}")

    else:
       final_price = price
       print(f"No discount applied. Original Price: {final_price}")
    
    
    
# Testing the function
calculate_discount()
