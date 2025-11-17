from nfa import NFA


def regex_to_nfa(regex):
stack = []


for c in regex:
if c.isalpha():
stack.append(NFA.symbol(c))
elif c == '*':
stack.append(NFA.star(stack.pop()))
elif c == '.':
b, a = stack.pop(), stack.pop()
stack.append(NFA.concat(a, b))
elif c == '|':
b, a = stack.pop(), stack.pop()
stack.append(NFA.union(a, b))


return stack.pop()
