from typing import List, Tuple


class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

    def dimensions(self) -> Tuple[int, int]:
        return (self.rows, self.cols)


class MeteorologicalData:
    def __init__(self, matrices: List[Matrix]):
        self.matrices = matrices

    def get_matrix_dimensions(self) -> List[Tuple[int, int]]:
        return [matrix.dimensions() for matrix in self.matrices]


class MatrixChainOrderCalculator:
    def __init__(self, dimensions: List[Tuple[int, int]]):
        self.dimensions = dimensions
        self.num_matrices = len(dimensions)
        self.cost_table = [[0] * self.num_matrices for _ in range(self.num_matrices)]
        self.split_table = [[0] * self.num_matrices for _ in range(self.num_matrices)]

    def calculate_optimal_order(self) -> int:
        for length in range(2, self.num_matrices + 1):  # length of the chain
            for i in range(self.num_matrices - length + 1):
                j = i + length - 1
                self.cost_table[i][j] = float("inf")
                for k in range(i, j):
                    # Calculate the cost/scalar multiplications
                    cost = (
                        self.cost_table[i][k]
                        + self.cost_table[k + 1][j]
                        + self.dimensions[i][0]
                        * self.dimensions[k][1]
                        * self.dimensions[j][1]
                    )

                    # Check if this split is optimal
                    if cost < self.cost_table[i][j]:
                        self.cost_table[i][j] = cost
                        self.split_table[i][j] = k

        return self.cost_table[0][self.num_matrices - 1]

    def get_optimal_order(self) -> str:
        return self._construct_optimal_order(0, self.num_matrices - 1)

    def _construct_optimal_order(self, i: int, j: int) -> str:
        if i == j:
            return f"M{i+1}"
        else:
            k = self.split_table[i][j]
            left_order = self._construct_optimal_order(i, k)
            right_order = self._construct_optimal_order(k + 1, j)
            return f"({left_order} x {right_order})"


# Client Code
if __name__ == "__main__":
    matrices = [
        Matrix(10, 30),  # Temperature
        Matrix(30, 5),  # Dew Point
        Matrix(5, 60),  # Wind Direction
        Matrix(60, 20),  # Wind Speed
        Matrix(20, 50),  # Cloud Cover
        Matrix(50, 70),  # Cloud Layer
    ]

    # Wrap data in MeteorologicalData class
    data = MeteorologicalData(matrices)

    # Calculate optimal order for matrix multiplication
    calculator = MatrixChainOrderCalculator(data.get_matrix_dimensions())
    min_cost = calculator.calculate_optimal_order()
    optimal_order = calculator.get_optimal_order()

    print("Minimum multiplication cost:", min_cost)
    print("Optimal multiplication order:", optimal_order)
