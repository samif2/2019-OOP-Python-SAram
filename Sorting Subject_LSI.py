
def Sort_Subject(sub):
    """

    :param sub: string 형태의 과목 묶음.
    :return: sub 를 과목별로 나눈 list
    """
    sub_list_1 = sub.split("/")
    sub_list_2 = []
    for i in range(len(sub_list_1)):
        j = sub_list_1[i]
        if i == len(sub_list_1)-1:
            sub_list_2 += [j]
            break
        blank_list = []
        if i==0:
            blank_list += [j.split("[")[0]]
        else:
            blank_list += [j.split("[")[0][0:5], j.split("[")[0][6:]]
        blank_list += j.split("[")[1].split("]")
        sub_list_2 += blank_list

    # print(sub_list_2)

    sub_list_3 =[]

    for i in range(len(sub_list_2)//4):
        blank_list = []
        for j in range(4):
            blank_list += [sub_list_2[i*4+j].strip()]
        sub_list_3.append(blank_list)

    # print(sub_list_3)

    return sub_list_3


if __name__ == "__main__":
    test = "객체지향프로그래밍 [1] 강동욱 / S402 고급알고리즘 [1] 문광식 / A401 고급영어독해와 작문 [2] 신현정 / A302 물리학세미나 II [2]" \
           " 장길동 / S213 수학세미나 II [2] 김하림 / S414 수학세미나 II [1] 임상연 / S415 일반물리학실험 II* [2] 정윤화 / S201" \
           " 일반화학 II* [1] 성수미 / S312"
    Sort_Subject(test)
