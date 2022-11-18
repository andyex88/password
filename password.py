password = 'a123456'
i = 3
while i > 0:
	name = input('請輸入密碼： ')
	if name == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤！ 還有', i - 1 ,'次機會')
	i = i - 1