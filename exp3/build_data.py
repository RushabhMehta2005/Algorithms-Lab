import pandas as pd
import random
from employee import Employee


def generate_employee_data(num_employees):
    names = [f"Employee_{i}" for i in range(num_employees)]
    bases = [random.randint(30000, 100000) for _ in range(num_employees)]
    HRAs = [random.randint(5000, 20000) for _ in range(num_employees)]
    taxes = [random.choice([5, 10, 15, 20, 25]) for _ in range(num_employees)]
    funds = [random.randint(1000, 10000) for _ in range(num_employees)]
    deductions = [random.randint(500, 5000) for _ in range(num_employees)]

    employees = []
    for i in range(num_employees):
        employee = Employee(
            names[i], bases[i], HRAs[i], taxes[i], funds[i], deductions[i]
        )
        employees.append(
            {
                "Name": employee.name,
                "Base Salary": employee.base,
                "HRA": employee.HRA,
                "Tax (%)": employee.tax,
                "Funds": employee.funds,
                "Deductions": employee.deductions,
                "Gross Salary": employee.gross_salary(),
                "Net Salary": employee.net_salary(),
            }
        )
    return employees


Z = ""
num_employees = 2000
employee_data = generate_employee_data(num_employees)
df = pd.DataFrame(employee_data)
df.to_csv(f"employees{Z}.csv", index=False)

print(f"{num_employees} employee records have been saved to 'employees.csv'")
