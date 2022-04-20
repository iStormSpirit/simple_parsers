import caldav
from datetime import datetime


def get_link_from_discr(description):
    try:
        x = description.split('Ссылка на видеовстречу: ')[1].split('\n')[0]
        if 'telemost' or 'zoom' in x:
            return x 
    except:
        return 

URL = 'https://caldav.yandex.ru/'
USERNAME = 'next.shadecs@yandex.ru'
PASSWORD = 'gmvdmkdnzvhkmiga'

if __name__ == "__main__":
    client = caldav.DAVClient(url=URL, username=USERNAME, password=PASSWORD)
    principal = client.principal()
    calendar = principal.calendar(name='testcaldav')
    events_fetched = calendar.date_search(start=datetime(2022,4,21), end=datetime(2022,4,22))

    for event in events_fetched:
        title = event.vobject_instance.vevent.summary.value
        print(title)

        dtsatrt = event.vobject_instance.vevent.dtstart.value
        print(dtsatrt)

        dtend = event.vobject_instance.vevent.dtend.value
        print(dtend)

        organizer = event.vobject_instance.vevent.organizer.value
        print('organizer', organizer)

        attendees = event.vobject_instance.vevent.contents['attendee']
        for people in attendees:
            print(people.value)
        # attendee = event.vobject_instance.vevent.attendee.value
        # print('attendee', attendee)

        description = event.vobject_instance.vevent.description.value
        print(description)
        link_conf = get_link_from_discr(description)
        if link_conf != None:
            print(link_conf)

        url = event.vobject_instance.vevent.url.value
        print(url)
        print('')

        # attendee2 = event.vobject_instance.vevent
        # print(attendee2)
