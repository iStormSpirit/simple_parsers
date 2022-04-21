import caldav
import re
from datetime import datetime
from icalendar import Calendar, Event
from pytz import UTC
import json
from requests.auth import AuthBase


# def __print_obj(obj):
#     attrs = vars(obj)
#     print('\n============================')
#     print('\n'.join("%s: %s" % item for item in attrs.items()))
#     print('============================\n\n')


def get_title(event):
    title = event.vobject_instance.vevent.summary.value
    return title


def get_data_start(event):
    dtsatrt = event.vobject_instance.vevent.dtstart.value
    return dtsatrt


def get_data_end(event):
    dtend = event.vobject_instance.vevent.dtend.value
    return dtend


def get_organizer_meet(event):
    organizer = event.vobject_instance.vevent.organizer.value
    return organizer


def get_attendees_meet(event):
    attendees = event.vobject_instance.vevent.contents['attendee']
    # '''show raw string all attendees'''
    # attendee = event.vobject_instance.vevent.attendee.value
    # print('attendee', attendee)
    members = []
    for people in attendees:
        members.append(people.value)
        # return people.value
    return members


def get_link_telemost(event):
    description = event.vobject_instance
    try:
        link = re.findall("(?P<url>https?://telemost[^\s]+)", str(description))
        return link[-1]
    except:
        None


def get_calendar_url(event):
    url = event.vobject_instance.vevent.url.value
    return url


# def get_link_from_discr(description):
#     try:
#         x = description.split('Ссылка на видеовстречу: ')[1].split('\n')[0]
#         if 'telemost' in x:
#             return x
#     except:
#         return


# def parse_link(link):
#     # system_message = 'Ссылка на видеовстречу появится здесь за 3 часа до встречи: '
#     # if system_message in link:
#     #     return 'no time'
#     # else:
#         try:
#             pattern = re.split('\s', link)
#             urld = []
#             url = ''
#             for i in pattern:
#                 if 'https://telemost' in i:
#                     url = url.join(i)
#                     urld.append(i)
#             return url
#         except:
#             pass
    # pattern = re.split('\s+', link)
    # url = ''
    # for i in pattern:
    #     if 'https://telemost' in i:
    #         url = url.join(i)
    # return url


URL = 'https://caldav.yandex.ru'
USEERNAME = 'thoth@sirius.online'
PASSWORD = 'wxyaorsuajiujqmu'
# USEERNAME = 'next.shadecs@yandex.ru'
# PASSWORD = 'gmvdmkdnzvhkmiga'


if __name__ == '__main__':
    client = caldav.DAVClient(URL, username=USEERNAME, password=PASSWORD)
    principal = client.principal()

    # calendar = principal.calendar(name="testcaldav")
    calendar = principal.calendar(name="Хеопс")
    events_fetched = calendar.date_search(start=datetime(2022, 4, 19), end=datetime(2022, 4, 20))

    for event in events_fetched:
        print('='*50)
        print(get_title(event))
        print(get_data_start(event))
        print(get_data_end(event))
        # # print(get_organizer_meet(event))
        print(get_attendees_meet(event))
        telemost = get_link_telemost(event)
        if telemost != None:
            print(telemost)
        print(get_calendar_url(event))

        # description = event
        # disc = Calendar.from_ical(description.data)
        # # print(disc)
        # for components in disc.walk():
        #     if components.name == "VEVENT":
        #         aldesc = components.get('description')
        #         # if 'Ссылка на видеовстречу появится здесь за 3 часа до встречи' in str(aldesc):
        #         #     print('wait')
        #         # else:
        #         #     print(aldesc)
        #         # print(aldesc)
        #         telemost_link = parse_link(aldesc)
        #         print(telemost_link)


    # description = events_fetched[0].vobject_instance.vevent.contents['description']
    # print(description)


        # print('='*50)



    # for event in events_fetched:
    #     print(event.vobject_instance.vevent.summary.value)
    #     print('%s — %s' % (event.vobject_instance.vevent.dtstart.value, event.vobject_instance.vevent.dtend.value))
    #     print(event.data)
    #     print(event.vobject_instance.vevent.contents['url'][0].value)
        # # __print_obj(event.vobject_instance.vevent.contents['url'][0])
        # print(event.icalendar_instance)
        # try:
        #     print(f'{event.vobject_instance.vevent.description.value}')
        # except:
        #     pass
        # try:
        #     for attend in event.vobject_instance.vevent.contents['attendee']:
        #         print('attendee', attend.value)
        #         # __print_obj(attend)
        # except:
        #     pass
        # print()

    # calendars = principal.calendars()
    # if len(calendars) > 0:
    #     calendar = calendars[0]
    #     print("Using calendar", calendar)
    #     results = calendar.events()
    #     eventSummary = []
    #     eventDescription = []
    #     eventDateStart = []
    #     eventdateEnd = []
    #     eventTimeStart = []
    #     eventTimeEnd = []
    #     eventATTENDEE = []
    #     eventORGZ = []
    #
    #     for eventraw in results:
    #
    #         event = Calendar.from_ical(eventraw.data)
    #         for component in event.walk():
    #             # print(component)
    #             if component.name == "VEVENT":
    #                 print(component.get('summary'))
    #                 eventSummary.append(component.get('summary'))
    #                 print(component.get('description'))
    #                 eventDescription.append(component.get('description'))
    #                 startDate = component.get('dtstart')
    #                 print(startDate.dt.strftime('%m/%d/%Y %H:%M'))
    #                 eventDateStart.append(startDate.dt.strftime('%m/%d/%Y'))
    #                 eventTimeStart.append(startDate.dt.strftime('%H:%M'))
    #                 endDate = component.get('dtend')
    #                 print(endDate.dt.strftime('%m/%d/%Y %H:%M'))
    #                 eventdateEnd.append(endDate.dt.strftime('%m/%d/%Y'))
    #                 eventTimeEnd.append(endDate.dt.strftime('%H:%M'))
    #                 dateStamp = component.get('dtstamp')
    #                 print(dateStamp.dt.strftime('%m/%d/%Y %H:%M'))
    #                 print(component.get('ATTENDEE'))
    #                 eventATTENDEE.append(component.get('ATTENDEE'))
    #                 print(component.get('ORGANIZER'))
    #                 eventORGZ.append(component.get('ORGANIZER'))
    #                 print('')



    # all_description = components.get('description')\
    #     .split('Ссылка на видеовстречу появится здесь за 3 часа до встречи: ')[0].split('\n')[0]\
    #     .split('Ссылка на видеовстречу: ')
    # desc_str = str(all_description)
    # print(dictdescription)
    # print('-'*100)
    # print(strdiscript)
    # print(all_description)
    # print(desc_str.split())
