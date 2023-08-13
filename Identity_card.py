def identify(id):
    local_table = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
            'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
            'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
    check = False
    while True:
        try:
            error = ''
            id_list = list(id)
            print(id_list)
            if len(id_list) != 10:
                error+='身分字號長度錯誤'
                break
            local = str(local_table[id_list[0]])
            check_id = list(local)
            check_id[0] = int(check_id[0])
            check_id[1] = int(check_id[1]) * 9
            sex = id_list[1]
            if sex != '1' and sex != '0':
                error += '身份證字號第二碼性別錯誤'
                break
            check_id.append(int(sex) * 8)
            for i in range(7):
                check_id.append(int(id_list[i+2]*(7-i)))
            check_num = 10 - sum(check_id) % 10
            print(check_num)
            if check_num == int(check_id[9]):
                check = True
                break
            else:
                error += '身份證字號檢查碼錯誤'
                break
        except Exception as e:
            print(e)

    if check == True:
        print('身份證字號驗證正確')
    else:
        print('身份證字號驗證錯誤，'+'錯誤原因:'+error)
id = input('請輸入身分證字號:').upper()
identify(id)





