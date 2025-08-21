#comparative operator
value1 = 2
value2 = 5
print(value1==value2)

value3 = 5
value4 = 10
value5 = 15
print(value3 > value5 or value3 < value4)
print(value3 > value5 and value3 < value4)



#conditional statement
nama = "adam"
tahun_masuk = 2016
tahun_lulus = 2025
spending_time = tahun_lulus - tahun_masuk

if(spending_time < 4 ):
    print("kamu punya potensi cumlaude")
    
elif(spending_time == 4):
    print("tahniah kamu lulus tepat waktu")
    
else:
    print("waduh jangan sampai do")
    
    
nama = "adam"
tahun_masuk = 2016
tahun_lulus = 2019
spending_time = tahun_lulus - tahun_masuk

if(spending_time > 3 and spending_time  <= 6  ):
    print("punya potensi cumlaude")
    
else:
    print("waduh jangan sampai do")