from data.processor import process_data
from util.helpers import calculate_total

numbers = [1, 2, 3, 4, 5]
processed = process_data(numbers)
total = calculate_total(processed)
print(processed)
print(total)
