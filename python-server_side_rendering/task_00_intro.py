from os import exists


def generate_invitations(template, attendees_list):
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees_list:
        print("No data provided, no output files generated")
        return

    if not isinstance(template, str):
        print("Template must be a string")
        return

    if (not isinstance(attendees_list, list) or
            not all(isinstance(item, dict) for item in attendees_list)):
        print("Attendance list must be a list of dictionaries")
        return

    for index, attendee in enumerate(attendees_list, start=1):
        template_schema = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = "{" + f"{key}" + "}"
            value = attendee.get(key) or "N/A"
            template_schema = template_schema.replace(placeholder, value)
        if not exists(f"output_{index}.txt"):
            with open(f"output_{index}.txt", "w") as file:
                file.write(template_schema)
        else:
            print("File already exists")
            