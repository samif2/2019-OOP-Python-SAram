import pickle, sys, time

ID = ''
PASSWORD = ''
def setinform():
    global ID, PASSWORD
    try:
        IDf = open('idf', 'rb')
        PWf = open('pwf', 'rb')
        ID = pickle.load(IDf)
        PASSWORD = pickle.load(PWf)
        IDf.close()
        PWf.close()
    except:
        pass

setinform()
while True:
    command = input('>')

    if command == 'help':
        print('setting - ID와 PASSWORD 를 설정합니다. \n'
              'check   - 설정한 ID와 PASSWORD를 확인합니다. \n'
              'reset   - ID와 PASSWORD 를 초기화합니다.\n'
              'exit    - 프로그램을 종료합니다.'
              )

    elif command == 'check':
        if ID == '':
            print("ID와 PASSWORD가 설정되지 않았습니다.")
        else:
            print("ID :", ID,  "\nPASSORD :", PASSWORD)

    elif command == 'setting':
        IDF = open('idf', 'wb')
        PWF = open('pwf', 'wb')
        setID = input("설정하고자 하는 ID를 입력해주세요 : ")
        setPW = input("설정하고자 하는 PASSWORD를 입력해주세요 : ")
        pickle.dump(setID, IDF)
        pickle.dump(setPW, PWF)
        print("ID와 PASSWORD의 설정이 완료되었습니다.")
        IDF.close()
        PWF.close()
        setinform()

    elif command == 'reset':
        IDF = open('idf', 'wb')
        PWF = open('pwf', 'wb')
        pickle.dump('', IDF)
        pickle.dump('', PWF)
        print("ID와 PASSWORD의 초기화가 완료되었습니다.")
        IDF.close()
        PWF.close()
        setinform()


    elif command == 'exit':
        print("프로그램을 종료합니다")
        time.sleep(0.1)
        sys.exit(0)



