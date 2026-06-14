import random

ips = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5"
]

pages = [
    "/home",
    "/login",
    "/products",
    "/cart",
    "/admin",
    "/contact",
    "/profile"
]

status_codes = [
    200,
    200,
    200,
    200,
    404,
    403,
    500
]

with open("logs/large_sample.log", "w") as file:

    for _ in range(1000):

        ip = random.choice(ips)
        page = random.choice(pages)
        status = random.choice(status_codes)

        file.write(
            f"{ip} GET {page} {status}\n"
        )

print("1000 log entries generated successfully.")