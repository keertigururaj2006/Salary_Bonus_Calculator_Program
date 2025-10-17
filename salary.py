# Salary Bonus Calculator

# Input
salary = float(input("Enter employee salary: "))

# Calculate 10% bonus
bonus = salary * 0.10
total_salary = salary + bonus

# Display result
print(f"Base Salary: ₹{salary:.2f}")
print(f"Bonus (10%): ₹{bonus:.2f}")
print(f"Total Salary after Bonus: ₹{total_salary:.2f}")
