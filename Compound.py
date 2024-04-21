# Take P,N and R as input from user
P = float(input('Please Enter Principal in INR:'))
N = float(input('Please Enter Number of Years:'))
R = float(input('Please Enter Rate of Interest in %p.a:'))
# Calculate Compound interest amount
A = P*(1+R/100)**N
I = A-P
# Print above result
print(f'Amount for Compound interest : {A:.2f} INR')
print(f'Total Interest : {I:.2f} INR')