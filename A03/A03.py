# Write your code here:

# Don't touch anthing below this line ๐๐ปโโ๏ธ๐๐ปโโ๏ธ
# revenue : ์์ต
# expenses : ์ง์ถ
# tax_credits : ์ธ์ก ๊ณต์ (ํ ์ธ)์จ
# tax_amount : ์ธ์ก

# get_tax_amount๋ if/else๋ฅผ ์ฌ์ฉํ  ๊ฒ
# if (profit > 100,000) -> tax_credits = 0.25
# else -> tax_credits = 0.15

# get_yeraly_revenue : ์ฐ๊ฐ ๋งค์ถ ๊ณ์ฐ
# get_yearly_expenses : ์ฐ๊ฐ ์ง์ถ ๊ณ์ฐ
# get_tax_amount : ์ธ์ก ๊ณ์ฐ
# apply_tax_credits : ์ธ์ก - ํ ์ธ๊ธ์ก

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01


def get_yearly_revenue(montly_revenue):
  return montly_revenue * 12

def get_yearly_expenses(monthly_expenses):
  return monthly_expenses * 12
profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

def get_tax_amount(profit):
  if profit > 100000:
    return profit * 0.25
  else:
    return profit * 0.15
tax_amount = get_tax_amount(profit)

def apply_tax_credits(tax_amount, tax_credits):
  return tax_amount * tax_credits
final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")