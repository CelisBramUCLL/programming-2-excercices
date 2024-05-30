# Write your code here
def format_time(hours, minutes, seconds):
    def format(int):
        return str(int).rjust(2, "0")

    return format(hours) + ":" + format(minutes) + ":" + format(seconds)
