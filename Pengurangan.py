def pengurangan_m(self):
        self.states = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10','q11', 'q12', 'q13', 'q14', 'q15',
                        'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 
                        'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40'}
        self.symbols = {'0', '1', '-', '+', 'B'}
        self.blank_symbol = 'B'
        self.input_symbols = {'0', '1', '-', '+'}
        self.initial_state = 'q1'
        self.accepting_states = {'q41'}
        self.transitions = {
                            ('q1', '-'): ('q2', '-', 1),
                            ('q1', '+'): ('q5', '+', 1),

                            ('q2', '0'): ('q2', '0', 1),
                            ('q2', '1'): ('q3', '1', 1),

                            ('q3', '-'): ('q4', '-', -1),
                            ('q3', '+'): ('q7', '+', -1),

                            ('q4', '0'): ('q4', '0', 1),
                            ('q4', '1'): ('q21', 'B', -1),

                            ('q5', '0'): ('q5', '0', 1),
                            ('q5', '1'): ('q6', '1', 1),

                            ('q6', '+'): ('q4', '+', -1),
                            ('q6', '-'): ('q7', '-', -1),

                            ('q7', '1'): ('q8', '1', -1),

                            ('q8', '0'): ('q8', '0', -1),
                            ('q8', 'B'): ('q8', 'B', -1),
                            ('q8', '+'): ('q9', '+', 1),
                            ('q8', '-'): ('q9', '-', 1),

                            ('q9', 'B'): ('q9', 'B', 1),
                            ('q9', '0'): ('q10', 'B', 1),

                            ('q10', '0'): ('q10', '0', 1),
                            ('q10', '1'): ('q11', '1', 1),

                            ('q11', '+'): ('q12', '+', 1),
                            ('q11', '-'): ('q12', '-', 1),

                            ('q12', '0'): ('q12', '0', 1),
                            ('q12', '1'): ('q13', '0', 1),
                            ('q12', 'B'): ('q18', '0', 1),

                            ('q13', 'B'): ('q14', 'B', -1),

                            ('q14', '0'): ('q14', '0', -1),
                            ('q14', '+'): ('q15', '+', -1),
                            ('q14', '-'): ('q15', '-', -1),

                            ('q15', '1'): ('q16', '1', -1),

                            ('q16', 'B'): ('q16', 'B', -1),
                            ('q16', '0'): ('q17', '0', -1),
                            ('q16', '+'): ('q19', 'B', 1),
                            ('q16', '-'): ('q19', '0', 1),

                            ('q17', '0'): ('q17', '0', -1),
                            ('q17', 'B'): ('q8', 'B', -1),

                            ('q18', 'B'): ('q14', 'B', -1),

                            ('q19', 'B'): ('q19', 'B', 1),
                            ('q19', '1'): ('q20', 'B', 1),

                            ('q20', '0'): ('q20', '0', 1),
                            ('q20', '+'): ('q20', '-', 1),
                            ('q20', '-'): ('q20', '+', 1),
                            ('q20', 'B'): ('q41', 'B', 1),

                            ('q21', '0'): ('q22', '1', 1),
                            ('q21', '+'): ('q30', '+', 1),
                            ('q21', '-'): ('q30', '-', 1),

                            ('q22', 'B'): ('q23', 'B', 1),

                            ('q23', 'B'): ('q23', 'B', 1),
                            ('q23', '+'): ('q24', '+', 1),
                            ('q23', '-'): ('q24', '-', 1),

                            ('q24', '0'): ('q24', '0', 1),
                            ('q24', '1'): ('q25', 'B', -1),
                            ('q24', 'B'): ('q31', 'B', -1),

                            ('q25', '0'): ('q26', '1', -1),
                            ('q25', '+'): ('q27', '+', -1),
                            ('q25', '-'): ('q27', '-', -1),

                            ('q26', '0'): ('q26', '0', -1),
                            ('q26', '+'): ('q27', '+', -1),
                            ('q26', '-'): ('q27', '-', -1),

                            ('q27', 'B'): ('q28', 'B', -1),

                            ('q28', 'B'): ('q28', 'B', -1),
                            ('q28', '1'): ('q29', '1', -1),

                            ('q28', '1'): ('q29', '1', -1),

                            ('q29', '0'): ('q29', '0', -1),
                            ('q29', '+'): ('q4', '+', 1),
                            ('q29', '-'): ('q4', '-', 1),
                
                            ('q30', 'B'): ('q30', 'B', 1),
                            ('q30', '+'): ('q31', '+', 1),
                            ('q30', '-'): ('q31', '-', 1),

                            ('q31', 'B'): ('q31', 'B', -1),
                            ('q31', '0'): ('q31', '0', 1),
                            ('q31', '1'): ('q32', 'B', -1),
                            ('q31', '+'): ('q38', 'B', -1),
                            ('q31', '-'): ('q38', 'B', -1),

                            ('q32', '0'): ('q32', '0', -1),
                            ('q32', '+'): ('q33', '-', -1),
                            ('q32', '-'): ('q33', '+', -1),
                            
                            ('q33', 'B'): ('q33', 'B', -1),
                            ('q33', '+'): ('q34', 'B', 1),
                            ('q33', '-'): ('q34', 'B', 1),

                            ('q34', 'B'): ('q34', 'B', 1),
                            ('q34', '+'): ('q35', '+', 1),
                            ('q34', '-'): ('q35', '-', 1),

                            ('q35', '0'): ('q36', '0', 1),
                            ('q35', 'B'): ('q37', 'B', -1),

                            ('q36', 'B'): ('q41', 'B', 1),

                            ('q37', '+'): ('q36', 'B', 1),
                            ('q37', '-'): ('q36', 'B', 1),

                            ('q38', 'B'): ('q38', 'B', -1),
                            ('q38', '+'): ('q39', '+', 1),
                            ('q38', '-'): ('q39', '-', 1),
                            ('q38', '1'): ('q39', '0', 1),
                            
                            ('q39', 'B'): ('q40', '0', 1),

                            ('q40', 'B'): ('q41', 'B', 1),
                            
                            }