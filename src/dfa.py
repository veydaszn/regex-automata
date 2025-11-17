class DFA:
def __init__(self, start_state, accept_states, transitions):
self.start_state = start_state
self.accept_states = accept_states
self.transitions = transitions


def accepts(self, s):
current = self.start_state
for c in s:
if c not in self.transitions[current]:
return False
current = self.transitions[current][c]
return current in self.accept_states
