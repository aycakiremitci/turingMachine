def dfa():
    transitions = {}

    states = input("States (separated by -): ").split('-')
    alphabet = input("The Alphabet (separated by -): ").split('-')
    enter_state = input("Enter State: ")
    accept_states = input("Accept States (separated by -): ").split('-')

    state_length = len(states)
    alphabet_length = len(alphabet)

    state_index = 0
    alphabet_index = 0

    while state_index < state_length:
        while alphabet_index < alphabet_length:
            next_state = input(f"State {states[state_index]} -> ? on {alphabet[alphabet_index]}\n? = ")
            transitions[(states[state_index], alphabet[alphabet_index])] = next_state
            alphabet_index += 1
        alphabet_index = 0
        state_index += 1

    current_state = enter_state
    print(f"Start state: {current_state}")

    transition_letters = input("Input Letters (separated by -): ").split('-')
    transition_length = len(transition_letters)
    transition_index = 0

    while transition_index < transition_length:
        previous_state = current_state
        current_state = transitions[(current_state, transition_letters[transition_index])]
        if current_state is None:
            print("Something went wrong, invalid transition.")
            return

        print(f"Input: {transition_letters[transition_index]}\nTransition: {previous_state} -> {current_state}")
        transition_index += 1

    if accept_states.__contains__(current_state):
        print("Input Accepted.")
        return

    print("Input Rejected.")


def create_turing_machine():
    states = input("States (separated by -): ").split('-')
    alphabet = input("The Alphabet (separated by -): ").split('-')
    blank_symbol = input("Blank Symbol: ")
    enter_state = input("Enter State: ")
    accept_state = input("Accept State: ")
    reject_state = input("Reject State: ")

    transitions = construct_transitions(states, alphabet)
    input_letters = input("Input Letters (separated by -): ").split('-')

    return transitions, blank_symbol, enter_state, accept_state, reject_state, input_letters


def construct_transitions(states, alphabet):
    transitions = {}

    state_length = len(states)
    alphabet_length = len(alphabet)

    state_index = 0
    alphabet_index = 0

    while state_index < state_length:
        while alphabet_index < alphabet_length:
            next_state = input(f"State {states[state_index]} -> ? on {alphabet[alphabet_index]}\n? = ")
            write_symbol = input(f"Write Symbol: ")
            move_direction = input(f"Direction (L/R): ")
            transitions[(states[state_index], alphabet[alphabet_index])] = (next_state, write_symbol, move_direction)
            alphabet_index += 1
        alphabet_index = 0
        state_index += 1

    return transitions


def run_turing_machine(transitions, blank_symbol, enter_state, accept_state, reject_state, input_letters):
    head_position = 0
    current_state = enter_state

    while not current_state == accept_state and not current_state == reject_state:
        input_letters, head_position = handle_head_movement(input_letters, head_position, blank_symbol)
        current_state = handle_state_transition(transitions, input_letters, head_position, current_state)

    is_accepted = current_state == accept_state
    if is_accepted:
        print("Input Accepted.")
        return

    print("Input Rejected.")


def handle_head_movement(input_letters, head_position, blank_symbol):
    if head_position < 0:
        input_letters.append(blank_symbol)

    if head_position >= len(input_letters):
        input_letters.append(blank_symbol)

    return input_letters, head_position


def handle_state_transition(transitions, input_letters, head_position, current_state):
    current_symbol = input_letters[head_position]
    action = transitions[(current_state, current_symbol)]

    if action is not None:
        next_state, input_letters[head_position], move_direction = action
        head_position += 1 if move_direction.lower() == 'r' else -1

        print(f"Symbol: {current_symbol}\nWrite: {input_letters[head_position]}\nMove: {move_direction}\n Transition: {current_state} -> {next_state}")

        return next_state

    print("Something went wrong, invalid transition.")
    return


def turing():
    transitions, blank_symbol, enter_state, accept_state, reject_state, input_letters = create_turing_machine()
    run_turing_machine(transitions, blank_symbol, enter_state, accept_state, reject_state, input_letters)


def run():
    option = -1
    switch = {
        0: dfa,
        1: turing
    }

    try:
        option = int(input("0- DFA\n1- TM\n"))
    except KeyError:
        print("Invalid option.")
    except ValueError:
        print("Invalid option.")

    switch[option]()


run()
