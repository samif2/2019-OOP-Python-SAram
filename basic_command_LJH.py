import pickle
import sys
datalist = {'gID': None, 'gPassword': None, 'ID': None, 'Password': None, 'logsys': 'sign_in'}


def load_info():  # 파일에서 아이디랑 비밀번호 정보를 불러옴
    global datalist
    try:
        file = open('MainData', 'rb')
        datalist = pickle.load(file)
        file.close()

    except:
        pass


def dump_info(datas):  # 파일에 정보 업로드
    a_file = open('MainData', 'wb')
    pickle.dump(datas, a_file)
    a_file.close()


def print_help():  # 설명서 출력
    print(
          'setting - ID와 PASSWORD 를 설정합니다. \n'
          "gmail   - 로그인 방식을 'gmail을 통한 로그인' 으로 설정합니다.\n"
          "sign_in - 로그인 방식을 '일반적인 로그인 방식' 으로 설정합니다.\n"
          'check   - 설정한 ID와 PASSWORD를 확인합니다. \n'
          'reset   - ID와 PASSWORD 를 초기화합니다.\n'
          'exit    - 프로그램을 종료합니다.'
          )


def setting():  # 아이디와 비밀번호를 변경하여 내장파일에 저장하는 함수
    global datalist
    datalist['ID'] = input("설정하고자 하는 ID를 입력해주세요 : ")
    datalist['Password'] = input("설정하고자 하는 PASSWORD를 입력해주세요 : ")
    print("ID와 PASSWORD 의 설정이 완료되었습니다.")


def gmail():  # 로그인 방식을 gmail로 바꾸는 함수
    datalist['logsys'] = 'btn.flat'

    print("로그인 방식을 gmail로 설정하기 위해 구글 이메일과 비밀번호를 저장합니다")
    datalist['gID'] = input("구글 이메일을 입력해주세요 : ")
    datalist['gPassword'] = input("구글 비밀번호를 입력해주세요 : ")

    print("로그인 방식이 gmail로 설정되었습니다.")


def sign_in():  # 로그인 방식을 sign_으로 바꾸는 함수
    datalist['logsys'] = 'btn.info'
    reset('reset_gmail')
    print("로그인 방식이 기본방식으로 설정되었습니다.")


def check():  # 아이디와 비밀번호 확인 함수
    if datalist['ID'] is None:
        print("ID와 PASSWORD가 설정되지 않았습니다.")
    else:
        print("ID :", datalist['ID'], "\nPASSWORD :", datalist['Password'])

    if datalist['gID'] is not None:  # gmail 방식을 사용한다면(gmail방식 사용때만 초기화됨)
        print("sasa gmail ID :", datalist['gID'],
              "\nsasa gmail PASSWORD :", datalist['gPassword'])


def reset(gmail=None):  # 프로그램 내 저장되어있는 아이디와 비밀번호를 초기화하는 함수
    datalist['gID'] = None
    datalist['gPassword'] = None
    if gmail == 'reset_gmail':  # gmail정보 '만'  삭제할경우
        return

    datalist['ID'] = None  # 아니라면 일반적인 초기화 마저 진행
    datalist['Password'] = None
    print("모든 정보의 초기화가 완료되었습니다.")


def exit():  # 프로그램을 종료시키는 함수
    print("프로그램을 종료합니다.")
    dump_info(datalist)
    sys.exit(0)


commandlist = {'help': print_help, 'setting': setting, 'check': check,
               'gmail': gmail, 'sign_in': sign_in, 'reset': reset, 'exit': exit}

# 함수 이름과 함수를 연결한 딕셔너리. 이를 통해 명령어로 함수를 실행시킬 수 있도록 함


###
# 여기는 비어있는공간
# 테스트용 main함수와 분리하기 위함
###


if __name__ == '__main__':
    load_info()
    while True:
        command = input('>')
        try:
            func = commandlist[command]
            func()
        except KeyError:
            print("해당하는 명령어가 없습니다.")
