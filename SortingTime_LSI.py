import datetime
import locale


def Sort_Time(year=2019, month=None, day=None, day_name=None, hour=None, minute=None, time_name=None):
    """
    모든 변수를 다 사용할 필요는 없다.
    년도는 2019가 기본. 요일 혹은 날짜를 기입해야 한다.
    시간, 혹은 시간표상에서 몇 교시인지 기입한다.

    점호 마감 전이면 0, 8시부터 1교시 시작 전은 0.5
    모든 교시는 정수이며, 그 사이 쉬는시간은 바로 앞 교시에 0.5를 더하여 표기한다.
    1차 자습은 10, 쉬는 시간은 10.5, 2차 자습은 11, 그 이후는 0으로 표기함.
    :param year: 년도, int 타입 지향, string 타입 지원
    :param month: 월, int 타입 지향, string 타입 지원
    :param day: 일, int 타입 지향, string 타입 지원
    :param day_name: 요일, string 타입
    "금", "토", "월" 과 같은 형태로 입력
    :param hour: 시 (24시간 방법 사용!), int 타입 지향, string 타입 지원
    :param minute: 분, int 타입 지향, string 타입 지원
    :param time_name:
    :return: 보아야 하는 시간표를 [ , ] 형태 리스트로 반환한다. 이 순서는 요일 - 시간 순이다.
    요일은 월요일을 0으로 하며 1씩 증가한다.
    """

    answer = []

    day_name_list = ["월", "화", "수", "목", "금", "토", "일"]

    if day_name is not None:
        answer += [day_name_list.index(day_name)]
    else:
        year = int(year)
        month = int(month)
        day = int(day)

        date = datetime.date(year, month, day)
        locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
        day_name = date.strftime('%A')[0:1]

        answer += [day_name_list.index(day_name)]

    hour = int(hour)
    minute = int(minute)
    time = 100*hour + minute

    if time < 800:
        answer.append(0)
    elif time < 840:
        answer.append(0.5)
    elif time <= 930:
        answer.append(1)
    elif time < 940:
        answer.append(1.5)
    elif time <= 1030:
        answer.append(2)
    elif time < 1040:
        answer.append(2.5)
    elif time <= 1130:
        answer.append(3)
    elif time < 1140:
        answer.append(3.5)
    elif time <= 1230:
        answer.append(4)
    elif time < 1320:
        answer.append(4.5)
    elif time <= 1410:
        answer.append(5)
    elif time < 1420:
        answer.append(5.5)
    elif time <= 1510:
        answer.append(6)
    elif time < 1520:
        answer.append(6.5)
    elif time <= 1610:
        answer.append(7)
    elif time < 1620:
        answer.append(7.5)
    elif time <= 1710:
        answer.append(8)
    elif time < 1720:
        answer.append(8.5)
    elif time <= 1810:
        answer.append(9)
    elif time < 1900:
        answer.append(9.5)
    elif time <= 2100:
        answer.append(10)
    elif time < 2130:
        answer.append(10.5)
    elif time <=2330:
        answer.append(11)
    else:
        answer.append(0)


if __name__ == "__main__":
    Sort_Time(year=2019, month=11, day=18, hour=12, minute=35)
