def powerMode(self):
    self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10','q11', 'q12', 
                   'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 
                   'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35'}
    self.symbols = {'0', '1', 'B', 'X'}
    self.blank_symbol = 'B'
    self.input_symbols = {'0', '1'}
    self.initial_state = 'q0'
    self.accepting_states = {'q35'}
    self.transitions = {
                        ('q0', '0'): ('q1', 'B', 1),
                        ('q0', '1'): ('q7', 'B', 1),

                        ('q1', '0'): ('q1', '0', 1),
                        ('q1', '1'): ('q2', '1', 1),

                        ('q2', '0'): ('q3', 'X', 1),
                        ('q2', '1'): ('q5', '1', 1),

                        ('q3', '0'): ('q3', '0', 1),
                        ('q3', '1'): ('q3', '1', 1),
                        ('q3', 'B'): ('q4', '0', -1),

                        ('q4', '0'): ('q4', '0', -1),
                        ('q4', '1'): ('q4', '1', -1),
                        ('q4', 'X'): ('q2', 'X', 1),

                        ('q5', '0'): ('q5', '0', 1),
                        ('q5', '1'): ('q5', '1', 1),
                        ('q5', 'B'): ('q6', '1', -1),

                        ('q6', '0'): ('q6', '0', -1),
                        ('q6', '1'): ('q6', '1', -1),
                        ('q6', 'X'): ('q6', '0', -1),
                        ('q6', 'B'): ('q0', 'B', 1),

                        ('q7', '0'): ('q7', 'B', 1),
                        ('q7', '1'): ('q8', '1', 1),

                        ('q8', '0'): ('q8', '0', 1),
                        ('q8', '1'): ('q8', '1', 1),
                        ('q8', 'B'): ('q9', 'B', -1),

                        ('q9', '1'): ('q10', '1', -1),

                        ('q10', '0'): ('q11', 'X', -1),

                        ('q11', '0'): ('q11', '0', -1),
                        ('q11', '1'): ('q12', '1', -1),

                        ('q12', '0'): ('q13', 'X', 1),
                        ('q12', '1'): ('q18', '1', 1),
                        ('q12', 'B'): ('q33', 'B', 1),
                        ('q12', 'X'): ('q12', 'X', -1),

                        ('q13', 'X'): ('q13', 'X', 1),
                        ('q13', '1'): ('q14', '1', 1),

                        ('q14', '0'): ('q14', '0', 1),
                        ('q14', 'X'): ('q14', 'X', 1),
                        ('q14', '1'): ('q15', '1', 1),

                        ('q15', '0'): ('q15', '0', 1),
                        ('q15', 'B'): ('q16', '0', -1),

                        ('q16', '0'): ('q16', '0', -1),
                        ('q16', '1'): ('q17', '1', -1),

                        ('q17', '0'): ('q17', '0', -1),
                        ('q17', 'X'): ('q17', 'X', -1),
                        ('q17', '1'): ('q12', '1', -1),

                        ('q18', 'X'): ('q18', '0', 1),
                        ('q18', '1'): ('q19', '1', 1),

                        ('q19', '0'): ('q19', '0', 1),
                        ('q19', 'X'): ('q20', 'X', -1),

                        ('q20', '0'): ('q11', 'X', -1),
                        ('q20', '1'): ('q21', '1', 1),

                        ('q21', 'X'): ('q21', '1', 1),
                        ('q21', '1'): ('q22', '1', -1),

                        ('q22', '0'): ('q23', '1', -1),
                        ('q22', '1'): ('q22', '1', -1),

                        ('q23', '0'): ('q23', '1', -1),
                        ('q23', '1'): ('q24', '1', 1),

                        ('q24', '0'): ('q24', '0', 1),
                        ('q24', '1'): ('q24', '1', 1),
                        ('q24', 'B'): ('q25', 'B', -1),

                        ('q25', '0'): ('q25', '0', -1),
                        ('q25', '1'): ('q26', '1', -1),

                        ('q26', '0'): ('q29', '0', -1),
                        ('q26', '1'): ('q30', '1', 1),
                        ('q26', 'B'): ('q27', 'B', 1),

                        ('q27', '0'): ('q28', '0', 1),
                        ('q27', '1'): ('q28', '1', 1),

                        ('q28', '0'): ('q28', '0', 1),
                        ('q28', '1'): ('q28', '1', 1),
                        ('q28', 'B'): ('q10', '1', -1),

                        ('q29', '0'): ('q29', '0', -1),
                        ('q29', '1'): ('q27', '1', 1),

                        ('q30', '1'): ('q31', '0', 1),

                        ('q31', '0'): ('q31', '0', 1),
                        ('q31', 'B'): ('q32', 'B', -1),

                        ('q32', '0'): ('q25', 'B', -1),

                        ('q33', '1'): ('q34', '1', 1),

                        ('q34', '0'): ('q34', '0', 1),
                        ('q34', 'X'): ('q35', '0', 1),
                        }