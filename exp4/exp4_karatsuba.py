class KaratsubaMultiplication:
    def regular_multiply(self, x, y):
        return x * y

    def karatsuba_multiply(self, x, y):
        if x < 10 or y < 10:
            return x * y

        max_len = max(len(str(x)), len(str(y)))
        half_max_len = max_len // 2

        high_x, low_x = divmod(x, 10**half_max_len)
        high_y, low_y = divmod(y, 10**half_max_len)

        z0 = self.karatsuba_multiply(low_x, low_y)
        z1 = self.karatsuba_multiply((low_x + high_x), (low_y + high_y))
        z2 = self.karatsuba_multiply(high_x, high_y)

        # Karatsuba formula
        return (
            (z2 * 10 ** (2 * half_max_len)) + ((z1 - z2 - z0) * 10**half_max_len) + z0
        )


class MultiplicationTest:
    def __init__(self):
        self.results = []

    def add_test(self, test_number, regular_result, karatsuba_result):
        same_result = (
            "Both methods produced the same result!"
            if regular_result == karatsuba_result
            else "Results differ!"
        )
        self.results.append(
            (test_number, regular_result, karatsuba_result, same_result)
        )

    def print_results(self):
        for test in self.results:
            test_number, regular_result, karatsuba_result, same_result = test
            print(f"Test {test_number}:")
            print("-" * 40)
            print("Regular Multiplication Result:")
            self.pretty_print(regular_result)
            print("\nKaratsuba Multiplication Result:")
            self.pretty_print(karatsuba_result)
            print(f"\n{same_result}")
            print("-" * 40, "\n")

    def pretty_print(self, num_str, chunk_size=100):
        """Prints a long number string in chunks of specified size for readability."""
        num_str = str(num_str)
        for i in range(0, len(num_str), chunk_size):
            print(num_str[i : i + chunk_size])


# Test execution
def run_tests():
    multiplier = KaratsubaMultiplication()
    test = MultiplicationTest()

    test_cases = [
        (1234567890, 9876543210),  # 10-digit numbers
        (
            12345678901234567890123456789012345678901234567890,
            98765432109876543210987654321098765432109876543210,
        ),  # 50-digit numbers
        (int("8" * 50 + "7" * 50), int("9" * 50 + "1" * 50)),  # 100-digit numbers
        (int("8" * 250 + "7" * 250), int("9" * 250 + "1" * 250)),  # 500-digit numbers
        (int("8" * 500 + "7" * 500), int("9" * 500 + "1" * 500)),  # 1000-digit numbers
    ]

    for i, (x, y) in enumerate(test_cases, start=1):
        print(f"Running test {i}...")
        regular_result = multiplier.regular_multiply(x, y)
        karatsuba_result = multiplier.karatsuba_multiply(x, y)

        test.add_test(i, regular_result, karatsuba_result)

    test.print_results()


run_tests()
