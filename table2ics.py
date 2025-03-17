import json
from datetime import datetime

# 定义节次与时间的映射
class ScheduleConverter:
    def __init__(self, json_data_list):
        self.json_data_list = json_data_list
        self.time_slots = {
            1: ("08:00", "08:45"),
            2: ("08:50", "09:35"),
            3: ("09:50", "10:35"),
            4: ("10:40", "11:25"),
            5: ("13:30", "14:15"),
            6: ("14:20", "15:05"),
            7: ("15:10", "15:55"),
            8: ("16:00", "16:45"),
            9: ("18:00", "18:45"),
            10: ("18:50", "19:35"),
            11: ("19:40", "20:25"),
            12: ("20:30", "21:15"),
        }
        self.location_name = {
            'A': "大连理工大学(开发区校区)教学楼A区\n学府大街大连理工大学(开发区校区)",
            'B': "大连理工大学(开发区校区)教学楼B区\n图强路321号大连理工大学(开发区校区)西区",
            'C': "大连理工大学开发区校区教学楼C区\n图强路321号大连理工大学(开发区校区)西区",
        }
        self.classroom_geo = {
            "A": '''URL;VALUE=URI:
X-APPLE-CREATOR-IDENTITY:com.apple.calendar
X-APPLE-CREATOR-TEAM-IDENTITY:0000000000
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-ADDRESS=学府大街大连理工大学(开发区校区);X-APPL
 E-MAPKIT-HANDLE=CAES1QIIl8QDEMrNwY7opP4BGhIJOh4zUBmLQ0ARu/HuyFh0XkAikQEK
 BuS4reWbvRICQ04aCei+veWugeecgTIJ5aSn6L+e5biCQgnph5Hlt57ljLpSMOWkp+i/nueQ
 huW3peWkp+WtpijlvIDlj5HljLrmoKHljLop5pWZ5a2m5qW8QeWMumIw5aSn6L+e55CG5bel
 5aSn5a2mKOW8gOWPkeWMuuagoeWMuinmlZnlrabmpbxB5Yy6KjDlpKfov57nkIblt6XlpKfl
 raYo5byA5Y+R5Yy65qCh5Yy6KeaVmeWtpualvEHljLoyUeS4reWbvei+veWugeecgeWkp+i/
 nuW4gumHkeW3nuWMuuWkp+i/nueQhuW3peWkp+WtpijlvIDlj5HljLrmoKHljLop5pWZ5a2m
 5qW8QeWMujg5UAFaFQoTCMrNwY7opP4BGJfEAyiQTpgDAQ==;X-APPLE-RADIUS=131.8870
 403446062;X-APPLE-REFERENCEFRAME=2;X-TITLE=大连理工大学(开发区校区)教学楼A区:geo:39.086
 710,121.817919''',
            "B": '''URL;VALUE=URI:
X-APPLE-CREATOR-IDENTITY:com.apple.mobilecal
X-APPLE-CREATOR-TEAM-IDENTITY:0000000000
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-ADDRESS=图强路321号大连理工大学(开发区校区)西区;X
 -APPLE-MAPKIT-HANDLE=CAES7QIIl8QDEOLj7cD8rP4BGhIJSUvl7QiLQ0ARhCugUE90XkA
 ioQEKBuS4reWbvRICQ04aCei+veWugeecgTIJ5aSn6L+e5biCQgnph5Hlt57ljLpSOOWbvuW
 8uui3rzMyMeWPt+Wkp+i/nueQhuW3peWkp+WtpijlvIDlj5HljLrmoKHljLop6KW/5Yy6Yjj
 lm77lvLrot68zMjHlj7flpKfov57nkIblt6XlpKflraYo5byA5Y+R5Yy65qCh5Yy6Keilv+W
 Muiow5aSn6L+e55CG5bel5aSn5a2mKOW8gOWPkeWMuuagoeWMuinmlZnlrabmpbxC5Yy6Mln
 kuK3lm73ovr3lroHnnIHlpKfov57luILph5Hlt57ljLrlm77lvLrot68zMjHlj7flpKfov57
 nkIblt6XlpKflraYo5byA5Y+R5Yy65qCh5Yy6Keilv+WMujgvUAFaFQoTCOLj7cD8rP4BGJf
 EAyiQTpgDAQ==;X-APPLE-RADIUS=141.5635708098784;X-APPLE-REFERENCEFRAME=2;
 X-TITLE=大连理工大学(开发区校区)教学楼B区:geo:39.086210,121.817341''',
            "C": '''URL;VALUE=URI:
X-APPLE-CREATOR-IDENTITY:com.apple.calendar
X-APPLE-CREATOR-TEAM-IDENTITY:0000000000
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-ADDRESS=图强路321号大连理工大学(开发区校区)西区;X
 -APPLE-MAPKIT-HANDLE=CAES6wIIl8QDENTNv47opP4BGhIJSrN5HAaLQ0ARlzjyQGR0XkA
 ioQEKBuS4reWbvRICQ04aCei+veWugeecgTIJ5aSn6L+e5biCQgnph5Hlt57ljLpSOOWbvuW
 8uui3rzMyMeWPt+Wkp+i/nueQhuW3peWkp+WtpijlvIDlj5HljLrmoKHljLop6KW/5Yy6Yjj
 lm77lvLrot68zMjHlj7flpKfov57nkIblt6XlpKflraYo5byA5Y+R5Yy65qCh5Yy6Keilv+W
 Muiou5aSn6L+e55CG5bel5aSn5a2m5byA5Y+R5Yy65qCh5Yy65pWZ5a2m5qW8Q+WMujJZ5Li
 t5Zu96L695a6B55yB5aSn6L+e5biC6YeR5bee5Yy65Zu+5by66LevMzIx5Y+35aSn6L+e55C
 G5bel5aSn5a2mKOW8gOWPkeWMuuagoeWMuinopb/ljLo4L1ABWhUKEwjUzb+O6KT+ARiXxAM
 okE6YAwE=;X-APPLE-RADIUS=141.563572883323;X-APPLE-REFERENCEFRAME=2;X-TIT
 LE=大连理工大学开发区校区教学楼C区:geo:39.086124,121.818619''',
        }

    def get_localtion(self, build_name):
        return self.location_name[build_name]

    def get_gps(self, build_name):
        return self.classroom_geo[build_name]

    def get_time_range(self, start_slot, duration):
        start_time_str, _ = self.time_slots[start_slot]
        end_slot = start_slot + duration - 1
        _, end_time_str = self.time_slots[end_slot]
        return start_time_str.replace(':', ''), end_time_str.replace(':', '')

    def convert_to_ics(self):
        ics_events = []
        for json_data in self.json_data_list:
            if json_data['KKXQM'] != '2' or json_data["JXDD"][-4] == "安":
                continue
            location = self.get_localtion(json_data["JXDD"][-4])
            classroom = json_data["JXDD"][-4:]
            course_name = json_data["KCMC"]
            start_date = json_data["SKRQ"]
            start_slot = int(json_data["SKJC"])
            duration = int(json_data["CXJC"])
            teacher_name = json_data["JSXM"]
            geo = self.get_gps(json_data['JXDD'][-4])
            start_time, end_time = self.get_time_range(start_slot, duration)

            ics_event = f"""BEGIN:VEVENT
SUMMARY:{course_name}|{classroom}|{teacher_name}
LOCATION:{location}
{geo}
DTSTART;TZID=Asia/Shanghai:{start_date.replace('-', '')}T{start_time}00
DTEND;TZID=Asia/Shanghai:{start_date.replace('-', '')}T{end_time}00
END:VEVENT
"""
            ics_events.append(ics_event)

        # 生成完整的 ICS 内容
        ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
{''.join(ics_events)}
END:VCALENDAR
"""
        return ics_content


with open('classdata.json',encoding='utf-8') as f:
   # print(f.read())
    a=json.loads(f.read())


# 创建转换器并生成 ICS 内容
converter = ScheduleConverter(a)
ics_output = converter.convert_to_ics()

with open('table_class.ics', 'w', encoding='utf-8') as f:
    f.write(ics_output)
# 输出 ICS 内容
# print(ics_output)