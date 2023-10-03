date_time_string = "Oct 03, 2023 - 05:30 PM"
pattern = r"([a-zA-Z]{3}\s\d{2},\s\d{4})\s-\s(\d{2}:\d{2}\s[APap][Mm])"
match = re.match(pattern, date_time_string)
if match:
    event_date = match.group(1)
    event_time = match.group(2)
    print("Event Date:", event_date)
    print("Event Time:", event_time)
