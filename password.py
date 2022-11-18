password = 'a123456'
i = 3
while i > 0:
	name = input('Please enter a password: ')
	if name == password:
		print('Successful access!')
		break
	else:
		i = i - 1
		if i  == 0:
			break
		print('Wrong password!', i ,'more chances left')
		