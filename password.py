password = 'a123456'
i = 3
while i > 0:
	name = input('請輸入密碼： ')
	if name == password:
		print('登入成功')
		break
	else:
		i = i - 1
		if i  == 0:
			break
		print('密碼錯誤！ 還有', i ,'次機會')
		