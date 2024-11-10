# S: Single Responsibility Principle
class DataFetcher:
    """Handles data fetching responsibility."""

    def fetch_data(self):
        return [1, 2, 3, 4, 5]


class DataProcessor:
    """Handles data processing responsibility."""

    def calculate_mean(self, data):
        return round(sum(data) / len(data), 3)


# Usage
fetcher = DataFetcher()
processor = DataProcessor()

data = fetcher.fetch_data()
result = processor.calculate_mean(data)
print(result)
