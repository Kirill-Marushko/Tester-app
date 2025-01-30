# Напишіть програму для знаходження всіх простих чисел в заданому діапазоні

start = int(input("Введіть звідки починаємо: "))
end = int(input("Введіть де закінчуємо: "))

correct = []
prime = True

for i in range(start, end):
    for i2 in range(2, i):
        if i % i2 == 0:
            prime = False
            break
    if prime is True:
        correct.append(i)
    prime = True
print(correct)
