from linked_list import LinkedList

def get_mid(llist_node):
	slow = llist_node
	fast = slow
	while (fast.next is not None 
			and fast.next.next is not None):
		fast = fast.next.next
		slow = slow.next
	return slow

def check_palindrome(llist):
	# CASE 1: length 1
	if len(llist) == 1:
		print("YES: 1")
	# CASE 2: length 2
	elif len(llist) == 2: 
		if llist.head == llist.head.next:
			print("YES: 2")
		else:
			print("NO: 1")
	else:
	# CASE 3: 
		mid = get_mid(llist.head)
		print(mid)


def main():
	ll = LinkedList.from_array([1, 2, 3, 2, 1])
	check_palindrome(ll)

if __name__ == '__main__':
	main()