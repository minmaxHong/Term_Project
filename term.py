from math import prod
import sys
import pickle

office = []
area = []
product = []
off_num = 0

data = {'office':office, 'area':area, 'product':product}

def show_menu():
    print('*******************************************')
    print('1. Office Management')
    print('2. Area Management')
    print('3. Product management')
    print('4. Search Product')
    print('5. Save File')
    print('6. Read File')
    print('7. Quit')
    print('*******************************************')


def show_submenu():
    print('*******************************************')
    print('1. Retrieve')
    print('2. Input')
    print('3. Update')
    print('4. Delete')
    print('5. Back to main')
    print('*******************************************')


def show_product_menu():
    print('*******************************************')
    print('1. Retrieve')
    print('2. Input')
    print('3. Lend/Return')
    print('4. Transfer')
    print('5. Update')
    print('6. Delete')
    print('7. Back to main')
    print('*******************************************')


def show_search_menu():
    print('*******************************************')
    print('1. View all product')
    print('2. Search product')
    print('3. Back to main')
    print('*******************************************')

def show_office():
    f = open('output.txt', 'a')
    print('Ofc.\tBld.\t\tOfc.\t\tOfc.')
    f.write('Ofc.\tBld.\t\tOfc.\t\tOfc.\n')    
    print('Code\tName\t\tAddress\t\tManager')
    f.write('Code\tName\t\tAddress\t\tManager\n')
    print('-------------------------------------------')
    for i in range(len(office)):
        print('{}\t{}\t\t{}\t\t{}'.format(
            office[i][0], office[i][1], office[i][2], office[i][3]))
        f.write('{}\t{}\t\t{}\t\t{}\n'.format(
            office[i][0], office[i][1], office[i][2], office[i][3]))
    f.write('\n')
    f.close()


def office_manage():
    print('\n\tOffice Management')
    show_submenu()
    global off_num

    n = input('Enter the number of the menu > ')
    while True:

        # retrieve
        if n == '1':
            if len(office) == 0:
                print('\nEmpty list. Enter info first.\n')
                office_manage()
            else:
                f = open('output.txt', 'a')
                f.write('\nOffice Retrieve\n')
                    
                print('*******************************************')

                print('Ofc. Code\tBld. name\tOfc. address\tOfc. Manager')
                f.write('Ofc. Code\tBld. name\tOfc. address\tOfc. Manager\n')
                for i in range(len(office)):
                    print('{}\t\t{}\t\t{}\t\t{}'.format(
                        office[i][0], office[i][1], office[i][2], office[i][3]))
                    f.write('{}\t\t{}\t\t{}\t\t{}\n'.format(
                        office[i][0], office[i][1], office[i][2], office[i][3]))
                f.close()
                office_manage()

        # input menu
        elif n == '2':
            off_num += 1
            off_code = format(off_num, '04')
            b_name = input('Enter building name(-1 to exit) > ')
            if b_name == '-1':
                break
            off_name = input('Enter a office name > ')
            om_name = input('Enter a office manager\'s name > ')

            office.append([off_code, b_name, off_name, om_name])
            
            f = open('output.txt', 'a')
            f.write('\nOffice Input\n')
            f.close()
            show_office()
            
            print('Input completed.\n')

            office_manage()

        # Update
        elif n == '3':
            print('Available office code')
            for i in range(len(office)):
                print(office[i][0], end='\t')
            isUpdated = False

            while True:
                off_code = input(
                    '\nEnter office code to update(-1 to exit) > ')
                if off_code == '-1':
                    break

                for j in range(len(office)):
                    if off_code == office[j][0]:
                        office[j][1] = input('Enter new building name > ')
                        office[j][2] = input('Enter new office name > ')
                        office[j][3] = input(
                            'Enter new office manager\'s name > ')
                        isUpdated = True
                        print('Updated.\n')
                        f = open('output.txt', 'a')
                        f.write('\nOffice Update\n')
                        f.close()

                        show_office()
                        break
                if isUpdated == True:
                    break
                print('Check office code name correctly.')
            office_manage()

        elif n == '4':
            print('Deletable office code')
            for i in range(len(office)):
                print(office[i][0], end='\t')
            isDeleted = True
            o_cnt = a_cnt = p_cnt = 0

            while True:
                off_code = input(
                    '\nEnter office code to delete(-1 to exit) > ')
                if off_code == '-1':
                    break

                for j in range(len(office)):
                    if off_code == office[j][0]:
                        office.remove(office[j])
                        o_cnt += 1
                        isDeleted == True
                        f = open('output.txt', 'a')
                        f.write('\nOffice Delete\n')
                        f.close()

                        show_office()
                        break   # 영역코드가 같은 것은 한개 뿐
                if o_cnt > 0:
                    print('{} Office deleted.'.format(o_cnt))
                
                if len(area) > 0:
                    for k in range(len(area) - 1, -1, -1):
                        if off_code == area[k][1]:
                            area.remove(area[k])
                            a_cnt += 1

                    if a_cnt > 0:
                        print('{} Area deleted.'.format(a_cnt))
                    f = open('output.txt', 'a')
                    f.write('\nArea Delete\n')
                    f.close()

                    show_area()

                if len(product) > 0:
                    for l in range(len(product)-1, -1, -1):
                        if off_code == product[l][1]:
                            product.remove(product[l])
                            p_cnt += 1

                    if p_cnt > 0:
                        print('{} Product deleted.\n'.format(p_cnt))
                    f = open('output.txt', 'a')
                    f.write('\nProduct Delete\n')
                    f.close()

                    show_product()

                
                # 종료 조건
                if isDeleted == True:
                    break
                print('!!! Check office code correctly.')

            office_manage()

        # back to main
        elif n == '5':
            main_menu()
        else:
            print('\n !!! Please enter number between 1 to 5.\n')
            office_manage()


def show_area():
    if len(area) > 0:
        f = open('output.txt', 'a')

        area.sort()
        print('*******************************************')
        f.write('Area Code\tOfc. Code\tArea Name\tArea Manager\n')
        print('Area Code\tOfc. Code\tArea Name\tArea Manager')
        for i in range(len(area)):
            print('{}\t\t{}\t\t{}\t\t{}'.format(
                area[i][1], area[i][0], area[i][2], area[i][3]))
            f.write('{}\t\t{}\t\t{}\t\t{}\n'.format(
                area[i][1], area[i][0], area[i][2], area[i][3]))
        f.write('\n')
        f.close()
    else:
        print('-------------------------------------------')
        print('There is no data\n')



def area_manage():
    if len(office) == 0:
        print('\n!!! Enter office info first. please.\n')
    else:

        print('\n\tArea Management')
        show_submenu()

        n = input('Enter the number of the menu > ')
        while True:
            show_submenu()
            if n == '1':
                if len(area) == 0:
                    print('\n!!! Empty list. Enter info first.\n')
                    area_manage()
                else:
                    f = open('output.txt', 'a')
                    f.write('\nArea retrieve\n')
                    f.close()
                    show_area()
                    area_manage()

            elif n == '2':
                if len(office) == 0:
                    print('\n !!! No office data. Input office first.\n')
                    area_manage()
                else:
                    print('Exist office code')
                    for i in range(len(office)):
                        print('{}'.format(office[i][0]))
                    isInput = False
                    while True:
                        ar_cnt = 1

                        off_code = input('Enter office code(-1 to exit) > ')
                        if off_code == '-1':
                            break
                        for i in range(len(area)):
                            if off_code == area[i][0]:
                                ar_cnt += 1

                        for i in range(len(office)):
                            if off_code == office[i][0]:                            
                                ar_code = format(ar_cnt, '03')
                                ar_name = input('Enter area name > ')
                                ar_m_name = input('Enter area manager Name > ')

                                area.append(
                                    [off_code, ar_code, ar_name, ar_m_name])
                                f = open('output.txt', 'a')
                                f.write('\nArea input\n')
                                f.close()
                                show_area()
                                print('Input completed.\n')
                                isInput = True

                        if isInput == True:
                            break
                        print('\n!!! Enter exist Office code.')
                    area_manage()
            elif n == '3':
                if len(area) > 0:
                    print('\nUpdate Area Info')
                    show_area()
                    isUpdated = False
                    while True:
                        f_ar_code = input(
                            'Enter area code to update(-1 to exit) > ')
                        if f_ar_code == '-1':
                            break

                        f_of_code = input('Enter office code to delete > ')
                        for i in range(len(area)):
                            if f_ar_code == area[i][1] and f_of_code == area[i][0]:
                                area[i][2] = input('Enter new area name > ')
                                area[i][3] = input(
                                    'Enter new area manager Name > ')
                                f = open('output.txt', 'a')
                                f.write('\nArea update\n')
                                f.close()
                                show_area()
                                print('\nUpdate completed.\n')
                                isUpdated = True
                        if isUpdated == True:
                            break
                        print('!!! Enter exist Area code and office code correctly. !!!')
                    area_manage()
                else:
                    print('Enter area info first.')
                    area_manage()

            elif n == '4':
                print('\nDelete Area Info')
                show_area()
                isDeleted = False
                a_cnt = p_cnt = 0

                while True:

                    # 영역 삭제
                    f_ar_code = input('Enter area code to delete(-1 to exit) > ')
                    if f_ar_code == '-1':
                        break
                    f_of_code = input('Enter office code to delete > ')
                    for i in range(len(area)-1, -1, -1):
                        if f_ar_code == area[i][1] and f_of_code == area[i][0]:
                            area.remove(area[i])
                            print('Deleted.\n')
                            f = open('output.txt', 'a')
                            f.write('\nArea delete\n')
                            f.close()
                            show_area()
                            a_cnt += 1
                            isDeleted = True

                    if a_cnt > 0:
                        print('{} Area deleted.'.format(a_cnt))

                    # 영역에 보관된 물품도 삭제
                    if len(product) > 0:
                        for j in range(len(product)-1, -1, -1):
                            if product[j][1] == f_of_code and product[j][2] == f_ar_code:
                                product.remove(product[j])
                                p_cnt += 1

                        if p_cnt > 0:
                            print('{} product deleted.\n'.format(p_cnt))
                        f = open('output.txt', 'a')
                        f.write('\nProduct delete\n')
                        f.close()
                        show_product()
                    if isDeleted == True:
                        break
                    print('Enter exist Area code and office code correctly.')
                area_manage()
            elif n == '5':
                main_menu()
            else:
                print('\nPlease enter number between 1 to 5.\n')
                area_manage()


def check_code():
    isOfCode = False
    isArCode = False

    print('Available Office number & Area number')
    print('-------------------------------------')
    print('Ofc. number\tArea number')
    # 사용가능한 코드 출력
    
    print('\nAvailable office code')
    for i in range(len(office)):
        print(office[i][0], end='\t')
    print()
    while True:
        off_num = input('Enter Office Code > ')
        for j in range(len(office)):
            if off_num == office[j][0]:
                isOfCode = True
                break
        if isOfCode == True:
            break
        print('!!! Please check Office code correctly.')


    print('\nAvailable area code')
    for i in range(len(area)):
        if off_num == area[i][0]:
            print(area[i][1], end='\t')
    print()
    while True:
        ar_num = input('Enter Area Code > ')
        for k in range(len(area)):
            if ar_num == area[k][1] and off_num == area[k][0]:
                isArCode = True
                break
        if isArCode == True:
            break
        print('!!! Please check Area code correctly.')

    return off_num, ar_num, isOfCode, isArCode


def show_product():
    product.sort()
    f = open('output.txt', 'a')
    print('-------------------------------------')
    print('Prod.\tOfc.\tArea\tProd.\t\t\t\tLend\t\tReturn')
    f.write('Prod.\tOfc.\tArea\tProd.\t\t\t\tLend\t\tReturn\n')
    print('code\tnumber\tnumber\ttype\tname\tprice\tLender\tdate\t\tdate')
    f.write('code\tnumber\tnumber\ttype\tname\tprice\tLender\tdate\t\tdate\n')
    for i in range(len(product)):
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            product[i][0], product[i][1], product[i][2], product[i][3], product[i][4], product[i][5], product[i][6], product[i][7], product[i][8]))
        f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
            product[i][0], product[i][1], product[i][2], product[i][3], product[i][4], product[i][5], product[i][6], product[i][7], product[i][8]))
    f.close()


def product_manage():
    if len(area) == 0:
        print('\n!!! No data. Input office & area data first. please.\n')
    else:
        show_product_menu()
        n = input('Enter the number of the menu > ')
        while True:
            # retrieve
            if n == '1':
                if len(product) == 0:
                    print('No data. Input product data first. please')
                else:
                    f = open('output.txt', 'a')
                    f.write('\nProduct retrieve\n')
                    f.close()
                    show_product()
                    print()

                product_manage()

            # Input
            elif n == '2':
                off_num, ar_num, isOfCode, isArCode = check_code()

                if isOfCode == True and isArCode == True:
                    p_code = input('Enter Product Code > ')
                    if len(product) > 0:
                        # 물품 코드 중복 방지
                        for i in range(len(product)):
                            while product[i][0] == p_code:
                                print('Already exists. Input again.')
                                p_code = input('Enter Product Code > ')

                    p_type = input('Enter Product Type > ')
                    p_name = input('Enter Product Name > ')
                    p_price = input('Enter Product Price > ')
                    lender = ' '
                    len_date = ' '
                    ret_date = ' '

                product.append([p_code, off_num, ar_num, p_type,
                               p_name, p_price, lender, len_date, ret_date])

                f = open('output.txt', 'a')
                f.write('\nProduct input\n')
                f.close()
                show_product()
                product_manage()

            # Lend/Return
            elif n == '3':
                if len(product) == 0:
                    print('There is no data of product. Input data first.')
                    product_manage()
                else:
                    while True:
                        print('-------------------------------------')
                        print('1. Lend')
                        print('2. Return')
                        print('-------------------------------------')

                        num = int(input('Enter the number of the menu > '))
                        # 대출
                        if num == 1:
                            show_product()
                            print('\n*************Lend process************\n')

                            isLent = False
                            while True:
                                off_num, ar_num, isOfCode, isArCode = check_code()
                                p_code = input('Enter Product Code to lend > ')
                                for i in range(len(product)):
                                    if product[i][0] == p_code and product[i][1] == off_num and product[i][2] and isOfCode == True and isArCode == True:
                                        # 물품이 현재 사용 중인 상태
                                        if product[i][7] != ' ' and product[i][8] == ' ':
                                            print(
                                                '\n!!! This product has already been lent.')

                                            if len(product) == 1:
                                                print(
                                                    '!!! There no product you can lend.')
                                                product_manage()
                                            break

                                        product[i][6] = input(
                                            'Enter lender\'s name > ')
                                        product[i][7] = input(
                                            'Enter lend date(must be 8 numbers) > ')
                                        while len(product[i][7]) != 8:
                                            product[i][7] = input(
                                                'Enter lend date correctly(must be 8 numbers) > ')
                                        # 이전에 대여했던 물품의 반납일자를 초기화함. 대여한 적이 없을 때도 적용됨.
                                        product[i][8] = ' '
                                        print('Lending completed.\n')
                                        isLent = True
                                        f = open('output.txt', 'a')
                                        f.write('\nProduct lent\n')
                                        f.close()

                                        show_product()
                                        break

                                if isLent == True:
                                    break

                                print('\n!!!Check Product Code again. Please.')
                                show_product()
                            product_manage()

                        # 반납
                        elif num == 2:
                            show_product()
                            print('\n************Return process***********\n')
                            isReturned = False
                            while True:
                                # 반납할 물품이 없을 때
                                cnt = 0
                                for i in range(len(product)):
                                    if (product[i][7] != ' ' and product[i][8] != ' ') or (product[i][7] == ' ' and product[i][8] == ' '):
                                        cnt += 1
                                if cnt == len(product):
                                    print(
                                        '!!! There is no product can be returned. Move to previous menu.\n')
                                    break

                                p_code = input(
                                    'Enter Product Code to return > ')
                                for i in range(len(product)):
                                    if product[i][0] == p_code and product[i][7] != ' ' and product[i][8] == ' ':
                                        product[i][8] = input(
                                            'Enter Return Date(must be 8 numbers). > ')
                                        while len(product[i][8]) != 8:
                                            product[i][8] = input(
                                                'Enter Return date correctly(must be 8 numbers) > ')
                                        isReturned = True
                                if isReturned == True:
                                    f = open('output.txt', 'a')
                                    f.write('\nProduct return\n')
                                    f.close()
                                    show_product()
                                    break
                                print('\n!!! Check Product Code again. Please.\n')

                            product_manage()

                        else:
                            print('Enter the number between 1 to 2')

            # Change place
            elif n == '4':
                if len(product) == 0:
                    print('There is no data of product. Input data first.')
                    product_manage()
                else:
                    show_product()
                    isMoved = False
                    # 이관할 장소가 있을 때만 실행 가능
                    while len(area) > 1:
                        p_code = input('Enter Product Code to transfer > ')
                        for i in range(len(product)):
                            if p_code == product[i][0]:
                                print('\nSelect to change Office & Area')
                                off_num, ar_num, isOfCode, isArCode = check_code()
                                while product[i][1] == off_num and product[i][2] == ar_num:
                                    print('This is already there.')
                                    break

                                product[i][1], product[i][2] = off_num, ar_num
                                isMoved = True
                                f = open('output.txt', 'a')
                                f.write('\nProduct transfer\n')
                                f.close()
                                show_product()
                                print('Transfer completed.\n')
                                break
                        if isMoved == True:
                            break
                        print('\n!!! Please check Product Code correctly.')
                    if len(area) == 1:
                        print(
                            '\n!!! There is just one area. Cannot transfer products.\n')
                    product_manage()
            elif n == '5':
                show_product()
                isUpdated = False
                while True:
                    p_code = input('Enter product code to update > ')
                    for i in range(len(product)):
                        if p_code == product[i][0]:
                            product[i][3] = input('Enter new product type > ')
                            product[i][4] = input('Enter new product name > ')
                            product[i][5] = input('Enter new product price > ')
                            isUpdated = True
                            f = open('output.txt', 'a')
                            f.write('\nProduct update\n')
                            f.close()
                            show_product
                            break
                    if isUpdated == True:
                        break
                    print('!!! Check product code again.')   
                product_manage()

            # Delete
            elif n == '6':
                if len(product) == 0:
                    print('There is no data of product. Input data first.')
                    product_manage()
                else:
                    show_product()
                    isDeleted = False
                    while True:
                        p_code = input('Enter product code to delete > ')
                        for i in range(len(product)):
                            if p_code == product[i][0]:
                                product.remove(product[i])
                                isDeleted = True
                                f = open('output.txt', 'a')
                                f.write('\nProduct delete\n')
                                f.close()                            
                                show_product()
                                print('Deleted successfully.\n')
                                break
                        if isDeleted == True:
                            break

                        print('\n!!! Please check Product Code correctly.')
                    product_manage()

            # Quit
            elif n == '7':
                main_menu()
            else:
                print('\nPlease enter number between 1 to 6.\n')
                product_manage()


def show_p_code():
    print('\nSearchable product code.')
    for i in range(len(product)):
        print(product[i][0], end='\t')
    print('\n')


def show_all_prod():
    f = open('output.txt', 'a')
    f.write('\nSearch all product\n')
    for i in range(len(office)):
        print('\n#{}\t{} {}\t\tManager:{}'.format(
            office[i][0], office[i][1], office[i][2], office[i][3]))
        f.write('\n#{}\t{} {}\t\tManager:{}\n'.format(
            office[i][0], office[i][1], office[i][2], office[i][3]))
        for j in range(len(area)):
            if area[j][0] == office[i][0]:
                for k in range(len(product)):
                    if (area[j][1] == product[k][2]) and (area[j][0] == product[k][1]):
                        print('\t#{} | {}\t(#{}){} | {} in charge'.format(
                            area[j][1], area[j][2], product[k][0], product[k][3], area[j][3]))
                        f.write('\t#{} | {}\t(#{}){} | {} in charge\n'.format(
                            area[j][1], area[j][2], product[k][0], product[k][3], area[j][3]))
        f.write('\n')
        print()
    
    f.close()


def find_prod(idx):
    f = open('output.txt', 'a')
    f.write('\nSearch one product\n')

    for i in range(len(office)):
        if product[idx][1] == office[i][0]:
            print('\n#{}\t{} {}\t\tManager:{}'.format(
                office[i][0], office[i][1], office[i][2], office[i][3]))
            f.write('\n#{}\t{} {}\t\tManager:{}\n'.format(
                office[i][0], office[i][1], office[i][2], office[i][3]))
    for j in range(len(area)):
        if (product[idx][2] == area[j][1]) and (area[j][0] == product[idx][1]):
            print('\t#{} | {}\t(#{}){} | {} in charge'.format(
                area[j][1], area[j][2], product[idx][0], product[idx][3], area[j][3]))
            f.write('\t#{} | {}\t(#{}){} | {} in charge\n'.format(
                area[j][1], area[j][2], product[idx][0], product[idx][3], area[j][3]))
    f.write('\n')
    print()
    f.close()


def search_prod():
    show_search_menu()
    n = int(input('Enter the number of the menu > '))
    if n == 1:
        show_all_prod()
        search_prod()
    elif n == 2:
        show_p_code()
        isFound = False
        while True:
            p_code = input('Enter product code to delete > ')
            for i in range(len(product)):
                if p_code == product[i][0]:
                    find_prod(i)
                    isFound = True
                    break
            if isFound == True:
                break

            print('\n!!! Please enter product code correctly.')
        search_prod()
    elif n == 3:
        main_menu()
    else:
        print('Enter the number between 1 to 3')
        search_prod()


def save_file():
    with open('list.dat','wb') as f:
        pickle.dump(data, f)
    print('File Saved.\n')
   
    main_menu()


def read_file():
    global off_num
    with open('list.dat', 'rb') as f:
        data = pickle.load(f)
   
    office.clear()
    area.clear()
    product.clear()
    office.extend(data['office'])
    area.extend(data['area'])
    product.extend(data['product'])
    off_num = int(len(office))
    
    
    print('File Loaded.\n')
    main_menu()

def main_menu():

    print('\n\t\tMain Menu')
    while True:
        show_menu()
        n = input('Enter the number of the menu > ')
        # 사무실 관리
        if n == '1':
            office_manage()
        # 영역 관리
        elif n == '2':
            area_manage()
        # 물품 관리
        elif n == '3':
            product_manage()
        # 물품 검색
        elif n == '4':
            search_prod()
        # 파일 출력
        elif n == '5':
            save_file()
        # 파일 읽어오기
        elif n == '6':
            read_file()        
        # 종료
        elif n == '7':
            print('Exit program')
            sys.exit(0)
        else:
            print('\n!!! Please enter number between 1 to 5.\n')
            main_menu()


main_menu()
