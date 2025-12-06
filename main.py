#1-misol
hujjat_top = input('Hujjat topshirganmisiz: ')
intervyu = input('Suhbatdan otganmisiz: ')
test = input('Test sinovidan otganmisiz: ')

if hujjat_top == 'ha':
    print('Hujjat topshirilgan.')
    if intervyu == 'ha':
        print('Suhbatdan otgan.')
        if test == 'ha':
            print('Siz ishga qabul qilindingiz.')
        else:
            print('Jarayon davom etmoqda.')
    else:
        print('Suhbatdan otmagansiz.')
else:
    print('Avvalo hujjatingizni topshiring.')

#2-misol
s = input("Matn kirit: ")

words = s.split()
secret = "".join(i[0] for i in words)

print(secret)

#3-misol
words = ['dasturlash', 'kitob', 'shunday', 'kompyuter', 'maktab']
print(words)

max1 = max(words, key=len)

others = [i for i in words if len(i) < len(max1)]

max2 = max(others, key=len)

print("Eng uzun so‘z :", max1)
print("Ikkinchi uzun :", max2)

#4-misol
soz = input('Soz kirit: ')

for i in soz:
    print(f'{i}-{i}')







