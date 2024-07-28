import os
# 讀取檔案
def readfile (filename,products):
        with open(filename,'r', encoding='utf-8') as my_file:
            for line in my_file:
                if '商品,價格' in line :
                    continue
                name,price = line.strip().split(',')
                products.append([name,price])
            print ('目前商品:', products)
        return products
#使用者輸入
def user_input(products):
    while True:
        name = input('輸入商品名稱:')
        if name == 'q':
            break
        price = input('輸入商品價格:')
        products.append([name,price])
    return products
#印出來
def print_list (products):
    for p in products:
        print(p[0],'的價格為',p[1])
#寫入檔案
def write_into_file(filename,products):
    with open(filename,'w',encoding='utf-8') as my_file : #with可以自動close()
        my_file.write('商品,價格\n')
        for p in products:
            my_file.write(p[0]+','+p[1]+'\n') #寫入

def main() :
    products=[]    
    filename = 'products.csv'
    if os.path.isfile(filename):
        print ('檔案存在!')
        products = readfile(filename,products)
    else :
            print('檔案不存在...')
    products = user_input(products)
    print_list(products)
    write_into_file (filename,products)

main()