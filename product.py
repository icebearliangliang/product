# 读取档案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品, 价格' in line:
			continue # 继续（跳到下一回）
		name, price = line.strip().split(',') # 做这步的目的是让清单的格式变回和下面的一样，这样后面再做处理就不会出错
		products.append([name,price])

print(products)




while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
	#p = [name, price]
	#products.append([name, price])
print(products)


for p in products:
	print(p[0], '的价格是', p[1])


with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

