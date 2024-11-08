#!/usr/bin/python3

def generate_invitations(template, attendees):

    if not template:
        print('Template is empty, no output files generated.')
        return

    if type(template) is not str:
        print('Error: template content must be string.')
        return

    if not attendees:
        print('No data provided, no output files generated.')
        return

    if type(attendees) is not list:
        print('Error: attendees must be a list of dictionaries')
        return

    index = 1
    for dict_attendee in attendees:
        if type(dict_attendee) is not dict:
            print('Error: attendees must be a list of dictionaries')
            return

        name = dict_attendee.get('name')
        event_title = dict_attendee.get('event_title')
        event_date = dict_attendee.get('event_date')
        event_location = dict_attendee.get('event_location')

        invitation = template
        invitation = invitation.replace('{name}', name if name else "N/A")
        invitation = invitation.replace('{event_title}',
                                        event_title if event_title else "N/A")
        invitation = invitation.replace('{event_date}',
                                        event_date if event_date else "N/A")
        invitation = invitation.replace('{event_location}',
                                        event_location
                                        if event_location else "N/A")

        filename = 'output_' + str(index) + '.txt'
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(e)

        index += 1
