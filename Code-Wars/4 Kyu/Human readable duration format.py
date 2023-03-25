"""Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as
a combination of years, days, hours, minutes and seconds."""

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    time = [ seconds // 31536000, seconds % 31536000 // 86400, seconds % 86400 // 3600, seconds % 3600 // 60, seconds % 60]
    name = ['year', 'day', 'hour', 'minute', 'second']
    result = [(str(i[0]), i[1]) for i in zip(time, name) if i[0] != 0]
    result = [item[0] + ' ' + item[1] if int(item[0]) == 1 else item[0] + ' ' + item[1] + 's' for item in result]
    print(result)
    return result[-1] if len(result) == 1 else ', '.join(result[:-1]) + ' and ' + result[-1]
