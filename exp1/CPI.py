def validate_input(courses, all_courses):
    # Check number of semesters
    if len(all_courses) > 8:
        raise ValueError("Invalid input: Number of semesters cannot exceed 8.")
    
    for credits, grade in courses:
        if credits <= 0 or credits > 4:
            raise ValueError("Invalid input: Credit cannot be negative, 0, or greater than 4.")
        if grade < 0:
            raise ValueError("Invalid input: Grade cannot be negative.")
    
    for credits, grade in all_courses:
        if credits <= 0 or credits > 4:
            raise ValueError("Invalid input: Credit cannot be negative, 0, or greater than 4.")
        if grade < 0:
            raise ValueError("Invalid input: Grade cannot be negative.")


def calculate_spi(courses):
    total_credits = 0
    weighted_grade_points = 0

    for credits, grade in courses:
        weighted_grade_points += credits * grade
        total_credits += credits

    spi = weighted_grade_points / total_credits
    return round(spi, 2)


def calculate_cpi(all_courses):
    total_credits = 0
    weighted_grade_points = 0

    for credits, grade in all_courses:
        weighted_grade_points += credits * grade
        total_credits += credits

    cpi = weighted_grade_points / total_credits
    return round(cpi, 2)


# Test cases
test_cases = [
    # Positive Case
    {
        "current_semester": [(4, 9), (3, 8), (2, 7), (3, 10), (1, 5)],
        "all_semesters": [(4, 9), (3, 8), (2, 7), (3, 10), (1, 5), (3, 6), (2, 8)],
        "expected_spi": 8.38,
        "expected_cpi": 7.94,
    },
    # Positive Case
    {
        "current_semester": [(3, 8), (3, 7), (3, 6), (3, 9)],
        "all_semesters": [(3, 8), (3, 7), (3, 6), (3, 9), (3, 7), (2, 8)],
        "expected_spi": 7.50,
        "expected_cpi": 7.47,
    },
    # Negative Case (Invalid Credit - 0)
    {
        "current_semester": [(0, 10), (3, 7), (2, 8)],
        "all_semesters": [(0, 10), (3, 7), (2, 8), (4, 5), (3, 6)],
        "expected_error": "Invalid input: Credit cannot be negative, 0, or greater than 4.",
    },
    # Negative Case (Invalid Credit - Negative)
    {
        "current_semester": [(4, 9), (3, -1), (2, 7)],
        "all_semesters": [(4, 9), (3, -1), (2, 7), (3, 6), (2, 5)],
        "expected_error": "Invalid input: Grade cannot be negative.",
    },
    # Negative Case (More than 8 Semesters)
    {
        "current_semester": [(4, 0), (3, 0), (2, 0)],
        "all_semesters": [(4, 0), (3, 0), (2, 0), (3, 0), (4, 0), (3, 0), (2, 0), (3, 0), (4, 0)],
        "expected_error": "Invalid input: Number of semesters cannot exceed 8.",
    },
]

# Testing the program
for i, test in enumerate(test_cases):
    print(f"Test Case {i + 1}:")
    try:
        validate_input(test["current_semester"], test["all_semesters"])
        spi = calculate_spi(test["current_semester"])
        cpi = calculate_cpi(test["all_semesters"])
        print(f"SPI: {spi} (Expected: {test.get('expected_spi')})")
        print(f"CPI: {cpi} (Expected: {test.get('expected_cpi')})")
        print(f"SPI Correct: {spi == test.get('expected_spi')}")
        print(f"CPI Correct: {cpi == test.get('expected_cpi')}")
    except ValueError as e:
        print(f"Error: {str(e)} (Expected: {test.get('expected_error')})")
        print(f"Error Correct: {str(e) == test.get('expected_error')}")
    print()
