import pandas as pd


class Employee:
    def __init__(self, name, base, HRA, tax, funds, deductions):
        self.name = name
        self.base = base
        self.HRA = HRA
        self.tax = tax
        self.funds = funds
        self.deductions = deductions

    def gross_salary(self):
        gross = self.base + self.funds + self.HRA
        return gross

    def net_salary(self):
        net = (
            ((100 - self.tax) / 100) * (self.base + self.HRA)
            + self.funds
            - self.deductions
        )
        return round(net, 4)


def find_minimum_iterative(df):
    m, n = df.shape
    min_salary = float("inf")
    id, name = None, None
    for i in range(m):
        if df.iloc[i]["Net Salary"] < min_salary:
            min_salary = df.iloc[i]["Net Salary"]
            name = df.iloc[i]["Name"]
            id = i

    return (id, name, min_salary)


def find_maximum_iterative(df):
    m, n = df.shape
    max_salary = float("-inf")
    id, name = None, None
    for i in range(m):
        if df.iloc[i]["Net Salary"] >= max_salary:
            max_salary = df.iloc[i]["Net Salary"]
            name = df.iloc[i]["Name"]
            id = i

    return (id, name, max_salary)


def find_minimum_recursive(df):
    m, n = df.shape

    def find_minimum_recursive_helper(left, right):
        if left == right:
            return left, df.iloc[left]["Name"], df.iloc[left]["Net Salary"]

        mid = left + (right - left) // 2

        left_id, left_name, left_min_salary = find_minimum_recursive_helper(left, mid)

        right_id, right_name, right_min_salary = find_minimum_recursive_helper(mid + 1, right)

        if left_min_salary < right_min_salary:
            return (left_id, left_name, left_min_salary)
        else:
            return (right_id, right_name, right_min_salary)

    return find_minimum_recursive_helper(0, m - 1)


def find_maximum_recursive(df):
    m, n = df.shape

    def find_maximum_recursive_helper(left, right):
        if left == right:
            return left, df.iloc[left]["Name"], df.iloc[left]["Net Salary"]

        mid = left + (right - left) // 2

        left_id, left_name, left_max_salary = find_maximum_recursive_helper(left, mid)

        right_id, right_name, right_max_salary = find_maximum_recursive_helper(
            mid + 1, right
        )

        if left_max_salary >= right_max_salary:
            return (left_id, left_name, left_max_salary)
        else:
            return (right_id, right_name, right_max_salary)

    return find_maximum_recursive_helper(0, m - 1)


def main():
    df = pd.read_csv("employees.csv", delimiter=",")

    """
    print("Metadata: ")
    print("Peek of the dataset: ")
    print(df.head(15))
    """

    print("Size of dataset: ")
    print(df.shape)

    print("Finding Employees with Minimum and Maximum Net Salaries: ")

    print("1. Finding Minimum: ")

    print(f"Iterative Result: ")
    id, name, min_salary = find_minimum_iterative(df)
    print(f"Id: {id}; Name: {name}; Salary: {min_salary}")

    print(f"Divide and Conquer Result: ")
    id, name, min_salary = find_minimum_recursive(df)
    print(f"Id: {id}; Name: {name}; Salary: {min_salary}")

    print("2. Finding Maximum: ")

    print(f"Iterative Result: ")
    id, name, max_salary = find_maximum_iterative(df)
    print(f"Id: {id}; Name: {name}; Salary: {max_salary}")

    print(f"Divide and Conquer Result: ")
    id, name, max_salary = find_maximum_recursive(df)
    print(f"Id: {id}; Name: {name}; Salary: {max_salary}")


if __name__ == "__main__":
    main()