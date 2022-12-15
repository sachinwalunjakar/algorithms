# ---------- bit shifting ----------

# a << b = a * 2^b

# a >> b = a / 2^b      if a > 2^b 
#        = 0            if a < 2^b 

n = 6 << 3
n = 2 >> 2


# ---------- logical operator ----------

# and
n = 1 & 1

# or
n = 0 & 1

# xor

n = 0 ^ 1



def countingBits(n):
  count = 0
  while n > 0:
    if n & 1 == 1:
      count += 1
    n = n >> 1
  return count

print(countingBits(23))



