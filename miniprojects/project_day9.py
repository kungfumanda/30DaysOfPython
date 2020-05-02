# simple credict card validator using Luhn algorithm
#for test use stripe.com/docs/testing#cards

card = input("Please enter your card number: ").strip()
digits = [int(number) for number in card]

# remove the rightmost digit from the card number (checking digit)
checking_digit = digits.pop()
total = checking_digit

# reverse the order of the remaining digits
digits.reverse()

# double the digits at each of the even indices
for i in range(len(digits)):
    if not (i % 2):
        digits[i] = 2*digits[i]
        if digits[i] > 9:  # if any of the results are greater than 9, subtract 9 from those numbers
            digits[i] -= 9
    # add together all of the results plus the checking digit
    total += digits[i]

# if the result is divisible by 10, the number is a valid card number, else, it's not valid.
if not (total % 10):
    print("This is a valid card number.")
else:
    print("This is not a valid card number.")
