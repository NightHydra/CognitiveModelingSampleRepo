
def simulate_seir(parameters, init_conditions, first_day = 1, last_day=51):
    """TODO"""

    # Extract parameters and initial conditions (Your code here)
    beta, sigma, gamma = parameters
    S0, E0, I0, R0 = init_conditions
    N = S0 + E0 + I0 + R0
    S = [S0] + [None] * (last_day - first_day)
    E = [E0] + [None] * (last_day - first_day)
    I = [I0] + [None] * (last_day - first_day)
    R = [R0] + [None] * (last_day - first_day)
    
    # For each day, perform SEIR update
    for t in range(first_day, last_day):

        # Compute new cases and update equations
        E_new = (beta*S[t-first_day]*I[t-first_day]) / N
        I_new = sigma*E[t-first_day]
        R_new = gamma*I[t-first_day]
      
        # Update equations
        S[t] = S[t-first_day] - E_new
        E[t] = E[t-first_day] + E_new - I_new
        I[t] = I[t-first_day] + I_new - R_new
        R[t] = R[t-first_day] + R_new

    return (S, E, I, R)
