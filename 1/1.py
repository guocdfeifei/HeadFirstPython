#人人都爱列表
movies = ["The Holy Grail","The Life of Brian","The Meaning of Life","阿飞"]
print(movies[3])
print(movies[1])
#测试重新提交
print(len(movies))
movies.append("飞弹")
print(movies)
movies.pop()
print(movies)
add1 = ["guo","fei"]
movies.extend(add1)
print(movies)
movies.remove("guo")
movies.insert(-2,"afei")
print(movies)

#test1
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
movies.pop()
movies.pop()
movies.pop()
print(movies)

add1.append(["fei","is a boy"])
print(add1)
for ad in add1:
	if isinstance(ad,list):
		for a in ad:
			print(a)
	else:
		print(ad)

#不定层列表考虑用递归方法
