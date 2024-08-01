def celculate_statd(numebers):
    total_sum = sum(numebers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum


numbers = [5,10,15,20,25]
total, avg, max_num, min_num = celculate_statd(numbers)

print(f"Total Sum: (total)")
print(f"Average: {avg}")
print(f"maximum: {max_num}")
print(f"minimum: {min_num}")