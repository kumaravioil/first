prin=int(input("Enter the principal amount: "))
roi=float(input("Enter the rate of interest: "))
time=int(input("Enter the number of years: "))
total=prin*pow((1+roi/100),time)
ci=total-prin
print(f"Total Amount is {total:.2f}")
print(f'Compound interest is {ci:.2f}')
