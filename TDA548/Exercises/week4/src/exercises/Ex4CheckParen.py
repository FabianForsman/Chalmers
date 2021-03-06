# package exercises

# Use a Stack to check parentheses (balanced and correct nesting)
# The parentheses are: (), [] and {}
#
# See:
# - UseAStack
# - UseString
# - SwitchStatement

parentheses = {
	"open": "([{",
	"closed": ")]}",
	0: "()",
	1: "[]",
	2: "{}"
}

def check_paren_program():
	# All should be true
	print(check_parentheses("()"))
	print(check_parentheses("(()())"))
	print(not check_parentheses("(()))"))  # Unbalanced
	print(not check_parentheses("((())"))  # Unbalanced

	print(check_parentheses("({})"))
	print(not check_parentheses("({)}"))  # Bad nesting
	print(not check_parentheses("({} [()] ({}))"))
	print(not check_parentheses("({} [() ({)})"))  # Unbalanced and bad nesting


# ----------- Methods -------------------------
def check_parentheses(string) -> bool:
	list = []
	for elem in string:
		list.append(elem)
	for i in list:
		if len(list) % 2 == 0:
			if i in parentheses["open"]:
				mirror = list[len(list) - 1 - list.index(i)]
				if mirror in parentheses["closed"]:
					if not (i + mirror in parentheses[0] or i + mirror in parentheses[1] or i + mirror in parentheses[2]):
						return False
		else:
			return False
	return True


def matching(string):
	paren_switcher = {
		'(': ')',
		'[': ']',
		'{': '}'
	}
	match = paren_switcher.get(string)
	if match is None:
		raise ValueError
	return match


if __name__ == "__main__":
	check_paren_program()
