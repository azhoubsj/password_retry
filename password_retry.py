password = 'a123456'
x = 1
while x <= 3:
	code = input('请输入密码:')
	y = 3 - x
	if code != 'a123456':
		print('密码输入错误!', '您还有', y, '次机会')
	else:
		print('密码正确，欢迎！')
		break
	x = x + 1
if x > 3:
	print('次数已达上限')