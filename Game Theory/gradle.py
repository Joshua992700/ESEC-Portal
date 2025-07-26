x = input()

r = int(len(x)/2)

f,s = x[:r],x[r:]
f = [int(i) for i in f]
s = [int(i) for i in s if i.isdigit()]

if sum(f) == sum(s):
    print("false")
else:
    print("true")
