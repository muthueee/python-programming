a =int(input())
rev =0
b=a
for i in range(a>0,1001):
	remain =a%10
	rev =(rev*10)+remain
	b =b//10
	if b==a:
		print a, 'is palindrome'
	else:
		print a, 'is not palindrome'
	break
