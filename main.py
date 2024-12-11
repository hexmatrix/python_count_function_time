import time

def count_time_taken(function):
    start_time = time.perf_counter()
    function()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time

def read_delimited_data():
    with open('data.txt', 'r') as file:
        for line in file:
            delimiters = line.strip().split(':')
            for delimiter in delimiters:
                print(delimiter)

elapsed_time = count_time_taken(read_delimited_data)

print(f"Time Taken: {elapsed_time:.6f} seconds")