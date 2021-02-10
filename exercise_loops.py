l = list(range(71, 100))
for i,c in enumerate(l):
    if c%2:
        say = "tektir."
    else:
        say = "çifttir."
    print("Listemizdeki", (i+1), "numaralı sayı", c, "oluyor, ve bu sayı", say)
