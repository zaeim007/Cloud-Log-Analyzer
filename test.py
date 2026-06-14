import time
from analyzer import analyze_log

start = time.time()

result = analyze_log("logs/five_million_logs.log")

end = time.time()

print(result)

print(f"\nExecution Time: {end - start:.2f} seconds")