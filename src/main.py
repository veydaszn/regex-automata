from regex_to_nfa import regex_to_nfa
from dfa import DFA


# Simple example: a(b|c)*
# In postfix form: a b c | * .


regex = "abc|*." # a(b|c)*
nfa = regex_to_nfa(regex)


# DFA Conversion (simplified)
start = frozenset(nfa.epsilon_closure({nfa.start}))
transitions = {}
queue = [start]
accept_states = set()


while queue:
state = queue.pop(0)
if state not in transitions:
transitions[state] = {}


for symbol in ['a', 'b', 'c']:
move = set()
for s in state:
move.update(nfa.transitions.get(s, {}).get(symbol, []))
if move:
closure = frozenset(nfa.epsilon_closure(move))
transitions[state][symbol] = closure
if closure not in transitions:
queue.append(closure)


if nfa.accept in state:
accept_states.add(state)


dfa = DFA(start, accept_states, transitions)


# Test strings
print("Accepted?", dfa.accepts("abbb"))
print("Accepted?", dfa.accepts("accc"))
print("Accepted?", dfa.accepts("a"))
print("Accepted?", dfa.accepts("bca"))
