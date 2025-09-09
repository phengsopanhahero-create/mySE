import math

def calculate_p_t(t: float, M: float, A: float, k: float) -> float:
    """Calculate population P(t) using the logistic growth formula: M/(1 + A*exp(-k*t))"""
    try:
        exponential_term = math.exp(-k * t)
        denominator = 1 + A * exponential_term
        p_t = M / denominator
        return p_t
    except ZeroDivisionError:
        print("Error: Denominator is zero. Please check your input values.")
        return float('nan')
    except ValueError:
        print("Error: Invalid input for mathematical operations (e.g., negative k or t for exp).")
        return float('nan')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return float('nan')

if __name__ == "__main__":
    print("--- Calculate Logistic Function Parameters and Estimate P(t) ---")
    print("Please enter the required parameters")

    try:
        # Get carrying capacity
        M_input = float(input("Enter the Carrying Capacity (M): "))
        if M_input <= 0:
            print("Error: Carrying capacity must be positive.")
            exit()

        # Get two data points for k calculation
        print("\n--- Enter two data points to calculate k ---")
        t1_input = float(input("Enter time t1: "))
        P1_input = float(input("Enter population P1 at t1: "))
        t2_input = float(input("Enter time t2: "))
        P2_input = float(input("Enter population P2 at t2: "))

        # Calculate growth rate constant k
        calculated_k = float('nan')
        if t1_input == t2_input:
            print("Error: t1 and t2 cannot be the same for k calculation.")
        elif P1_input <= 0 or P1_input >= M_input or P2_input <= 0 or P2_input >= M_input:
            print("Error: P1 and P2 must be greater than 0 and less than M.")
        else:
            try:
                numerator_log = P2_input * (M_input - P1_input)
                denominator_log = P1_input * (M_input - P2_input)
                
                if denominator_log == 0:
                    print("Error: Denominator for log calculation is zero. Check P1, P2, and M values.")
                elif numerator_log <= 0 or denominator_log <= 0:
                    print("Error: Both numerator and denominator must be positive for log calculation.")
                else:
                    log_argument = numerator_log / denominator_log
                    calculated_k = (1 / (t2_input - t1_input)) * math.log(log_argument)
            except Exception as e:
                print(f"An error occurred during k calculation: {e}")
        
        if not math.isnan(calculated_k):
            print(f"\nCalculated Growth Rate Constant (k): {calculated_k:.6f}")
        else:
            print("\nCould not calculate k due to input errors or mathematical constraints. Cannot proceed.")
            exit()

        # Calculate constant A using the first data point
        calculated_A = float('nan')
        P_known_for_A = P1_input
        t_known_for_A = t1_input

        if P_known_for_A <= 0 or P_known_for_A >= M_input:
            print("Error: P1 used for A calculation must be greater than 0 and less than M.")
        elif t_known_for_A < 0:
            print("Error: t1 used for A calculation cannot be negative.")
        else:
            try:
                term_in_parentheses = (M_input / P_known_for_A) - 1
                if term_in_parentheses <= 0:
                    print("Error: Term (M/P - 1) must be positive for A calculation.")
                else:
                    exponential_term_for_A = math.exp(calculated_k * t_known_for_A)
                    calculated_A = term_in_parentheses * exponential_term_for_A
            except Exception as e:
                print(f"An error occurred during A calculation: {e}")
        
        if not math.isnan(calculated_A):
            print(f"Calculated constant A: {calculated_A:.4f}")
        else:
            print("\nCould not calculate A due to input errors or mathematical constraints. Cannot proceed.")
            exit()

        # Estimate P(t) at a new time point
        print("\n--- Estimate P(t) and Calculate Error ---")
        try:
            t_estimate = float(input("Enter the time (t) for which you want to estimate P(t): "))
            P_actual = float(input(f"Enter the actual population value for t = {t_estimate}: "))

            estimated_p_t = calculate_p_t(t_estimate, M_input, calculated_A, calculated_k)
            
            if not math.isnan(estimated_p_t):
                print(f"\nEstimated P({t_estimate}) = {estimated_p_t:.2f}")
                print(f"Actual P({t_estimate}) = {P_actual:.2f}")

                absolute_error = abs(estimated_p_t - P_actual)
                print(f"Absolute Error: {absolute_error:.2f}")

                if P_actual != 0:
                    percentage_error = (absolute_error / P_actual) * 100
                    print(f"Percentage Error: {percentage_error:.2f}%")
                else:
                    print("Cannot calculate percentage error: Actual population is zero.")
            else:
                print(f"Could not estimate P({t_estimate}) due to calculation errors.")

        except ValueError:
            print("Error: Please enter valid numerical values for estimation.")
        except Exception as e:
            print(f"An unexpected error occurred during estimation: {e}")

    except ValueError:
        print("Error: Please enter valid numerical values for all parameters.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")