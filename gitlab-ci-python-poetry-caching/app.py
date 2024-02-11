import pendulum


def print_time(location, tz):
    now = pendulum.now(tz).to_time_string()
    print(f"Current time in {location} is {now}")


print_time("San Diego", "America/Los_Angeles")
print_time("Stockholm", "Europe/Stockholm")
