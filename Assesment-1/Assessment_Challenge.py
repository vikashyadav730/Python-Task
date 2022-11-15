import os

def load_data():
    try:
        file_name = input('file name: ') + '.csv'
        if file_name==None or file_name.endswith('.csv')==False:
            print('File not found')
        elif os.path.getsize(file_name) == 0:
            print('File empty...')
        elif  file_name.endswith('.csv')==True:
            try:
                dataset = open(file_name, 'r')
                data2 = list(dataset.readline().split(','))
                data4 = list(dataset.readline().split(','))
                data5 = list(dataset.readline().split(','))
                get_data2 = data2[len(data2) - 1]
                data2.remove(get_data2)
                data2.append(get_data2.replace("\n", ""))
                hh = data2[1:]
                # for i in hh:
                #     tt = int(i)
                get_data4 = data4[len(data4)-1]
                data4.remove(get_data4)
                data4.append(get_data4.replace("\n",""))
                hh2 = data4[1:]
                # for x in hh2:
                #     tt2 = int(x)
                get_data5 = data5[len(data5) - 1]
                data5.remove(get_data5)
                data5.append(get_data5.replace("\n", ""))
                hh3 = data5[1:]
                # for h in hh3:
                #     tt3 = int(h)
                print('File Loaded successfully.')
            except ValueError:
                print('ValueError ')

            get_data1 = {}
            get_data1[data2[0]] = data2[1:len(data2)]
            get_data1[data4[0]] = data4[1:len(data4)]
            get_data1[data5[0]] = data5[1:len(data5)]
            dataset.close()
            # print(get_data1)
            return get_data1

    except:
        print('FileNotFoundError: No such file in directory: ')


def display_data():
    try:
        if len(get_data1)>0:
            for i in get_data1.items():
                key = i[0]
                print(key)
                hh = len(key)
                print(hh*'_')
                kk = i[1:]
                for i in kk:
                    for x in i:
                        print(x, end=',')
                print('                         ')
                print('                         ')

        else:
            print('No dataset to display')
    except NameError:
        print('No data...')
    except TypeError:
        print('No data...')

def rename_set():
    try:
        datavalues = list(get_data1)
        print('Which set do you want to rename?')
        print('\t1 - ',datavalues[0])
        print('\t2 - ',datavalues[1])
        print('\t3 - ',datavalues[2])
        # print(get_data1)

        try:
            value = int(input('choose number :- '))
            while value < 1 or value > 3:
                print('Invalid option!! Please choose any among 1 to 3.')
                value = int(input('>>>'))
            if value == 1:
                new_key = input('Enter key name')
                while len(new_key)==0 or new_key==list(get_data1.keys())[0]:
                    print('Name cannot be blank,Name must be unique')
                    new_key = input('Enter key name')
                name = list(get_data1.keys())[0]
                if len(new_key)>=1:
                    data = list(get_data1)
                    data.pop(0)
                    data.insert(0,new_key)
                    first_key = data[0]
                    sec_key = data[1]
                    thrd_key = data[2]
                    new_keys1 = [first_key, sec_key, thrd_key]
                    hh = dict(zip(new_keys1, get_data1.values()))
                    get_data1.clear()
                    get_data1.update(hh)
                    print('successfully change {} To {}'.format(name,new_key))
            elif value ==2:
                new_key = input('Enter key name')
                while len(new_key) == 0 or new_key == list(get_data1.keys())[1]:
                    print('Name cannot be blank,Name must be unique')
                    new_key = input('Enter key name')
                name = list(get_data1.keys())[1]
                if len(new_key)>=1:
                    data = list(get_data1)
                    data.pop(1)
                    data.insert(1, new_key)
                    first_key = data[0]
                    sec_key = data[1]
                    thrd_key = data[2]
                    new_keys1 = [first_key, sec_key, thrd_key]
                    hh = dict(zip(new_keys1, get_data1.values()))
                    get_data1.clear()
                    get_data1.update(hh)
                    print('successfully change {} To {}'.format(name,new_key))

            elif value ==3:
                new_key = input('Enter key name')
                while len(new_key) == 0 or new_key == list(get_data1.keys())[2]:
                    print('Name cannot be blank,Name must be unique')
                    new_key = input('Enter key name')
                name = list(get_data1.keys())[2]
                if len(new_key)>=1:
                    data = list(get_data1)
                    data.pop(2)
                    data.insert(2, new_key)
                    first_key = data[0]
                    sec_key = data[1]
                    thrd_key = data[2]
                    new_keys1 = [first_key, sec_key, thrd_key]
                    hh = dict(zip(new_keys1, get_data1.values()))
                    get_data1.clear()
                    get_data1.update(hh)
                    print('successfully change {} To {}'.format(name,new_key))

            else:
                print('Invalid option!! Please choose any among 1 to 3.')
        except:
            print('Enter integer values only')
    except NameError:
        print('No data...')
    except TypeError:
        print('No data...')

def sort_set():
    try:
        datavalue = list(get_data1)
        print('Which set do you want to sort?')
        print('\t1 - ',datavalue[0])
        print('\t2 - ',datavalue[1])
        print('\t3 - ',datavalue[2])
        try:
            values = int(input('>>>'))
            if values==1:
                list_empty = []
                data = list(get_data1)
                ll = data[0]
                n = get_data1[ll]
                for x in n:
                    k = int(x)
                    list_empty.append(k)
                list_empty.sort()
                print(list_empty)

            elif values==2:
                list_empty = []
                data = list(get_data1)
                ll = data[1]
                n = get_data1[ll]
                for x in n:
                    k = int(x)
                    list_empty.append(k)
                list_empty.sort()
                print(list_empty)

            elif values==2:
                list_empty = []
                data = list(get_data1)
                ll = data[2]
                n = get_data1[ll]
                for x in n:
                    k = int(x)
                    list_empty.append(k)
                list_empty.sort()
                print(list_empty)

            else:
                print('Invalid option!! Please choose any among 1 to 3.')
        except:
            print('Invalid option!! Please choose any among 1 to 3.')
    except NameError:
        print('No data...')
    except TypeError:
        print('No data...')


def analyze_set():
    try:
        from collections import Counter
        datavalues = list(get_data1)
        print('Which set do you want to Analyze?')
        print('\t1 - ',datavalues[0])
        print('\t2 - ',datavalues[1])
        print('\t3 - ',datavalues[2])
        value = int(input())
        if value == 1:
            kk = list(get_data1)
            first_index = kk[0]
            print(first_index)
            print('----------')
            data = get_data1[first_index]
            data2 =[]
            for x in data:
                k = int(x)
                data2.append(k)

            print('number of values (n):',len(data2))
            print('             minimum: ',min(data2))
            print('             maximum: ',max(data2))
            avg = sum(data2)/len(data2)
            print('                Mean:',avg)

            n = len(data2)
            data2.sort()

            if n % 2 == 0:
                median1 = data2[n // 2]
                median2 = data2[n // 2 - 1]
                median = (median1 + median2) / 2
            else:
                median = data2[n // 2]
            print("              Median: " + str(median))

            n = len(data2)

            data = Counter(data2)
            get_mode = dict(data)
            mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

            if len(mode) == n:
                get_mode = "none"
            else:
                get_mode = "Mode: " + ', '.join(map(str, mode))

            print('               ',get_mode)

            mean = sum(data2) / len(data2)
            variance = sum([((x - mean) ** 2) for x in data2]) / len(data2)
            res = variance ** 0.5
            print("  Standard deviation: ",round(res,2))
            print()
            print()

        elif value ==2:
            kk = list(get_data1)
            sec_index = kk[1]
            print(sec_index)
            print('----------')
            data = get_data1[sec_index]
            data2 = []
            for x in data:
                k = int(x)
                data2.append(k)

            print('number of values (n):', len(data2))
            print('             minimum: ', min(data2))
            print('             maximum: ', max(data2))
            avg = sum(data2) / len(data2)
            print('                Mean:', avg)

            n = len(data2)
            data2.sort()

            if n % 2 == 0:
                median1 = data2[n // 2]
                median2 = data2[n // 2 - 1]
                median = (median1 + median2) / 2
            else:
                median = data2[n // 2]
            print("              Median: " + str(median))

            n = len(data2)

            data = Counter(data2)
            get_mode = dict(data)
            mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

            if len(mode) == n:
                get_mode = "none"
            else:
                get_mode = "Mode: " + ', '.join(map(str, mode))

            print('               ', get_mode)

            mean = sum(data2) / len(data2)
            variance = sum([((x - mean) ** 2) for x in data2]) / len(data2)
            res = variance ** 0.5
            print("  Standard deviation: ",round(res,2))
            print()
            print()

        elif value==3:

            kk = list(get_data1)
            third_index = kk[2]
            print(third_index)
            print('----------')
            data = get_data1[third_index]
            data2 = []
            for x in data:
                k = int(x)
                data2.append(k)

            print('number of values (n):', len(data2))
            print('             minimum: ', min(data2))
            print('             maximum: ', max(data2))
            avg = sum(data2) / len(data2)
            print('                Mean:', avg)

            n = len(data2)
            data2.sort()

            if n % 2 == 0:
                median1 = data2[n // 2]
                median2 = data2[n // 2 - 1]
                median = (median1 + median2) / 2
            else:
                median = data2[n // 2]
            print("              Median: " + str(median))

            n = len(data2)

            data = Counter(data2)
            get_mode = dict(data)
            mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

            if len(mode) == n:
                get_mode = "none"
            else:
                get_mode = "Mode: " + ', '.join(map(str, mode))

            print('               ', get_mode)

            mean = sum(data2) / len(data2)
            variance = sum([((x - mean) ** 2) for x in data2]) / len(data2)
            res = variance ** 0.5
            print("  Standard deviation: " ,round(res,2))
            print()
            print()

        else:
            print('Invalid option!! Please choose any among 1 to 3.')
    except NameError:
        print('No data...')
    except TypeError:
        print('No data...')

def save_file():
    new_fileName = input('Enter the filename, including file extension: ')
    try:
        with open(new_fileName, 'w') as f:
            for key in get_data1.keys():
                f.write("%s, %s\n" % (key, get_data1[key]))
    except IOError:
        print("I/O error")

def compare_two_sets():
    from collections import Counter
    dataset1 = list(get_data1)
    getdataset = []
    for i in range(1):
        print('Please choose which one u want to compare')
        print('\t1 - ',dataset1[0])
        print('\t2 - ',dataset1[1])
        print('\t3 - ',dataset1[2])
        try:
            value = int(input('>>>'))
            if value == 1:
                getdataset.append(dataset1[0])
            elif value ==2:
                getdataset.append(dataset1[1])
            elif value == 3:
                getdataset.append(dataset1[2])
            else:
                print('Invalid option!! Please choose any among 1 to 3.')
        except ValueError:
            print('Enter the int values only')
        for i in range(1):
            print('Please choose which one u want to compare1111')
            print('\t1 - ', dataset1[0])
            print('\t2 - ', dataset1[1])
            print('\t3 - ', dataset1[2])
            try:
                value = int(input('>>>'))
                if value == 1:
                    getdataset.append(dataset1[0])
                elif value == 2:
                    getdataset.append(dataset1[1])
                elif value == 3:
                    getdataset.append(dataset1[2])
                else:
                    print('Invalid option!! Please choose any among 1 to 3.')
            except ValueError:
                print('Enter the int values only')

    if getdataset[0]!= getdataset[1]:
        third_index = getdataset[0]
        third_index2 = getdataset[1]
        print('                  ',third_index,'                        ',third_index2)
        print('                  ','-'*len(third_index),'                  ','     ','-'*len(third_index2))
        data = get_data1[third_index]
        data11 = get_data1[third_index2]
        data2 = []
        data22 = []
        for x in data:
            k = int(x)
            data2.append(k)
        for x in data11:
            k = int(x)
            data22.append(k)

        print('number of values (n):', len(data2),'                           ', len(data22))
        print('             minimum:', min(data2),'                           ', min(data22))
        print('             maximum:', max(data2),'                          ', max(data22))
        avg = sum(data2) / len(data2)
        avg2  = sum(data22) / len(data22)
        print('                Mean:', avg,'                         ', avg2)

        n = len(data2)
        data2.sort()
        n2 = len(data22)
        data22.sort()

        if n % 2 == 0:
            median1 = data2[n // 2]
            median2 = data2[n // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = data2[n // 2]
        if n2 % 2 == 0:
            median1 = data22[n2 // 2]
            median2 = data22[n2 // 2 - 1]
            median11 = (median1 + median2) / 2
        else:
            median11 = data22[n2 // 2]
        print("              Median: " + str(median), "                          " + str(median11))# median

        data = Counter(data2)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

        if len(mode) == n:
            get_mode = "non"
        else:
            get_mode = "Mode: " + ', '.join(map(str, mode))

        data11 = Counter(data22)
        get_mode11 = dict(data11)
        mode11 = [k for k, v in get_mode11.items() if v == max(list(data11.values()))]

        if len(mode11) == n2:
            get_mode11 = "            non"
        else:
            get_mode11 = "       " + ', '.join(map(str, mode11))

        print('               ', get_mode,'               ', get_mode11)#Mode

        mean = sum(data2) / len(data2)
        variance = sum([((x - mean) ** 2) for x in data2]) / len(data2)
        res = variance ** 0.5

        mean11 = sum(data22) / len(data22)
        variance = sum([((x - mean11) ** 2) for x in data22]) / len(data22)
        res11 = variance ** 0.5
        print(" Standard deviation: " ,round(res,2), "                        " ,round(res11,2))
        print()
        print()
    else:
        print("there's no point comparing a set to itself!")

def Edit_a_set():
    datavalues = list(get_data1)
    print('Which set do you want to edit?')
    print('\t1 - ', datavalues[0])
    print('\t2 - ', datavalues[1])
    print('\t3 - ', datavalues[2])
    values = int(input('>>>'))
    while values == values and 0<=values<=len(datavalues):
        print('You are editing {}'.format(datavalues[values-1]))
        print('\t(i)nsert a value')
        print('\t(m)odify a value')
        print('\t(d)elete a value')
        print('\t(f)inish editing')
        value = input('>>>')
        if value=='i':
            kk3 = get_data1[datavalues[values-1]]#list values
            print('You are editing {}'.format(datavalues[values-1]))
            print('\t1 - at the beginning')
            l = 1
            for i in range(len(kk3) - 1):
                print('\t{} - between {} and {}'.format(l+1,kk3[l-1], kk3[l]))
                l = l + 1
            print('\t{} - at the end'.format(len(kk3)+1))
            print('\t{} - cancel insert'.format(len(kk3)+2))
            try:
                new = int(input('>>>'))
                while new < 1 or new > len(kk3) + 2:
                    print('Invalid option!! Please choose any among {} to {}.'.format(0, len(kk3)+2))
                    new = int(input('>>>'))
                if new==1:
                    print('You are inserting at location {}, at the beginning'.format(new))
                    hh2 = input('Enter the value to insert:')
                    kk3.insert(0, hh2)
                    print('you have inserted ', hh2)

                elif 1<new<=len(kk3):
                    print('You are inserting at location {} between {} and {} '.format(new,kk3[new-2],kk3[new-1]))
                    hh2 = input('Enter the value to insert:')
                    kk3.insert(new-1,hh2)
                    print('you have inserted {}'.format(hh2))

                elif new == len(kk3)+1:
                    print('You are inserting at end ')
                    hh2 = input('Enter the value to insert:')
                    kk3.append(hh2)
                    print('you have inserted ', hh2)
                elif new == len(kk3)+2:
                    pass
            except ValueError:
                print('Invalid option!!')
            # except

        elif value == 'm':
            kk3 = get_data1[datavalues[values - 1]]#list values
            print('Which values will you modify?')
            length = len(kk3)
            for i in range(len(kk3)):
                print('\t{}. {}'.format(i+1,kk3[i]))
            print('\t{} cancel modify'.format(length+1))
            hh4 = int(input('>>>'))
            if 0 < hh4 < length:
                print('Enter the new value:')
                hh5 = int(input('>>>'))
                print('You have modified {} to {}'.format(kk3[hh4 - 1], hh5))
                kk3[hh4-1] = hh5

            elif hh4==length+1:
                pass

        elif value=='d':
            kk3 = get_data1[datavalues[values - 1]]  # list values
            print('Which values will you delete?')
            length = len(kk3)
            for i in range(len(kk3)):
                print('\t{}. {}'.format(i + 1, kk3[i]))
            print('\t{} cancel delete'.format(length + 1))
            try:
                no= int(input('>>>'))
                while no<1 or no>len(kk3)+1:
                    print('Invalid option!! Please choose any among {} to {}.'.format(0,length+1))
                    no = int(input('>>>'))
                if 0<no<=len(kk3):
                    print('You have deleted {} from location {} '.format(kk3[no-1],no))
                    del kk3[no-1]
                elif no==len(kk3)+1:
                    pass
            except ValueError:
                print('Invalid option!!')
                return Edit_a_set()

        elif value=='f':
            return option




def get_valid_option():
    try:
        x = int(input('>>>'))
        while x < 1 or x > 9:
            print('Invalid option!! Please choose any among 1 to 9.')
            x = int(input('>>>'))

        return x
    except :
        print('Invalid option!! Please choose any among 1 to 9.')


if __name__=='__main__':

    print('Welcome to The Smart Statistician!')
    print('    Programmed by Vikash\n')

    while True:
        print('Please choose from the following options:')
        print('\t1 - Load data from a file')
        print('\t2 - Display the data to the screen')
        print('\t3 - Rename a set')
        print('\t4 - Sort a set')
        print('\t5 - Analyze a set')
        print('\t6 - Save data to a file')
        print('\t7 - Compare two sets')
        print('\t8 - Edit a set')
        print('\t9 - Quit')

        option = get_valid_option()

        if option == 1:
            get_data1 = load_data()
        elif option == 2:
            display_data()
        elif option == 3:
            rename_set()
        elif option == 4:
            sort_set()
        elif option == 5:
            analyze_set()
        elif option == 6:
            save_file()
        elif option == 7:
            compare_two_sets()
        elif option == 8:
            Edit_a_set()
        elif option == 9:
            quit()
