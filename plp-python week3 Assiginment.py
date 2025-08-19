# calculate_discount function

def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount_amount = price*(discount_percent/100)
    return price-discount_amount
  else:
      return price
    
    # [prompt]
try:
    original_price = float(input("Enter the original Price of item"))
    discount_percentage = float(input("Enter the discount percentage:"))

        # final price
    final_price= calculate_discount(original_price,discount_percentage)

# print
    if discount_percentage >=20:
         print(f"The final price after applyong a {discount_percentage}% discount is:${final_price:.2f}")
    else:
     print(f"No discount applied.The original price is: ${original_price:.2f}")
except ValueError:
 print("Invalid input.Please enter numeric values for price and discount percentage ")
     