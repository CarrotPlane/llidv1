import random
from datetime import datetime, timezone

def generate_lexlexid():
    # Current UTC time formatted as MMDDHHMMSS
    time_str = datetime.now(timezone.utc).strftime("%m%d%H%M%S")
    
    info = input("Enter 6-digit info code (or leave blank for default): ")
    if not info:
        info = "086230"
    # Ensure info is exactly 6 digits
    info_str = str(info).zfill(6)[:6]

    # Random 10-digit number, zero-padded
    rand_str = str(random.randint(0, 9999999999)).zfill(10)

    return f"{time_str}-{info_str}-{rand_str}"

print(generate_lexlexid())
