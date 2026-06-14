import random

ips = [f"192.168.1.{i}" for i in range(1, 101)]

pages = [
    "/home",
    "/login",
    "/products",
    "/cart",
    "/profile",
    "/contact",
    "/admin"
]

status_codes = [
    200, 200, 200, 200, 200,
    200, 200, 200, 200,
    403, 404, 500
]

with open("logs/million_logs.log", "w") as file:

    for _ in range(1_000_000):

        if random.random() < 0.05:
        
            garbage = random.choice([
                "hello world",
                "abc xyz",
                "123",
                "GET /home",
                "random garbage data"
            ])

            file.write(garbage + "\n")

        else:

            ip = random.choice(ips)
            page = random.choice(pages)
            status = random.choice(status_codes)

            file.write(
                f"{ip} GET {page} {status}\n"
            )

print("1,000,000 logs generated successfully.")