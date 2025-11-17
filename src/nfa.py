class NFA:
def concat(nfa1, nfa2):
offset = max(nfa1.transitions) + 1


transitions = {}
for s, t in nfa1.transitions.items():
transitions[s] = t
for s, t in nfa2.transitions.items():
transitions[s + offset] = {k: [st + offset for st in v] for k, v in t.items()}


transitions[nfa1.accept].setdefault("ε", []).append(nfa2.start + offset)


return NFA(nfa1.start, nfa2.accept + offset, transitions)


@staticmethod
def union(nfa1, nfa2):
offset = max(nfa1.transitions) + 1


transitions = {0: {"ε": [nfa1.start + 1, nfa2.start + offset + 1]}}


for s, t in nfa1.transitions.items():
transitions[s + 1] = {k: [st + 1 for st in v] for k, v in t.items()}
for s, t in nfa2.transitions.items():
transitions[s + offset + 1] = {k: [st + offset + 1 for st in v] for k, v in t.items()}


transitions[nfa1.accept + 1].setdefault("ε", []).append(max(transitions) + 1)
transitions[nfa2.accept + offset + 1].setdefault("ε", []).append(max(transitions) + 1)
transitions[max(transitions) + 1] = {}


return NFA(0, max(transitions), transitions)


@staticmethod
def star(nfa):
start, accept = 0, max(nfa.transitions) + 2


transitions = {start: {"ε": [nfa.start + 1, accept]}}
for s, t in nfa.transitions.items():
transitions[s + 1] = {k: [st + 1 for st in v] for k, v in t.items()}


transitions[nfa.accept + 1].setdefault("ε", []).extend([nfa.start + 1, accept])
transitions[accept] = {}


return NFA(start, accept, transitions)


def epsilon_closure(self, states):
stack = list(states)
closure = set(states)


while stack:
s = stack.pop()
for nxt in self.transitions.get(s, {}).get("ε", []):
if nxt not in closure:
closure.add(nxt)
stack.append(nxt)


return closure
