import random

LOG_COUNT = 5_000_000

ips = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.40",
    "192.168.1.50"
]

methods = ["GET", "POST"]

pages = [
    "/",
    "/home",
    "/about",
    "/contact",
    "/products",
    "/cart",
    "/profile",
    "/login"
]

status_codes = [200, 200, 200, 200, 404, 500, 403]

output_file = "logs/five_million_logs.log"

with open(output_file, "w") as file:

    for _ in range(LOG_COUNT):

        ip = random.choice(ips)
        method = random.choice(methods)
        page = random.choice(pages)
        status = random.choice(status_codes)

        file.write(
            f"{ip} {method} {page} {status}\n"
        )

print(f"Generated {LOG_COUNT:,} log entries")
print(f"Saved to: {output_file}")