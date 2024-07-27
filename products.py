products=[]
while True:
    name = input('輸入商品名稱:')
    if name == 'q':
        break
    price = input('輸入商品價格:')
    products.append([name,price])
print(products)

for p in products:
    print(p[0],'的價格為',p[1])
#寫入檔案
with open('products.csv','w',encoding='utf-8') as my_file : #with可以自動close()
    my_file.write('商品,價格\n')
    for p in products:
        my_file.write(p[0]+','+p[1]+'\n') #寫入
