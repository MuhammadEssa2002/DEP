
def possible_new_states(state):
    for pile, counters in enumerate(state):
        for decrement in (1, 2):
            if counters >= decrement:
                yield state[:pile] + (counters - decrement,) + state[pile + 1:]


def evaluate(state, max_turn):
    if not all(state):
        return -1 if max_turn else 1
    

def minimax(state, max_turn,depth,alpha = -1 , beta = 1):
    if depth == 0:
        return 1 if max_turn else -1
    if (score := evaluate(state, max_turn)) is not None:
        return score

    depth -= 1
    scores = []
    for new_state in possible_new_states(state):
        scores.append(
            score := minimax(new_state, not max_turn,depth, alpha, beta)
        )
        if max_turn:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            break
    return (max if max_turn else min)(scores)
    
def next_move_standard(state,depth):
    next = possible_new_states(state)
    for i in next:
        score = minimax(i, True,depth)
        if score == -1:
            return -score, i
    
    return score, i

def next_move_misere(state,depth):
    if state == (3,1) or state == (1,3):
        return 1, (1,1)
    next = possible_new_states(state)
    for i in next:
        score = minimax(i, True,depth)
        if score == 1:
            return score, i
    return -score, i

def main():
    #print(minimax((20,12),True,10))
    print(next_move_misere((20,21),10))
if __name__ == '__main__':
    main()