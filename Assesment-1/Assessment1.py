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
            values = int(input())
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
    except NameError as Np:
        print('No data...')
    except TypeError:
        print('No data...')

def get_valid_option():
    try:
        x = int(input('>>>'))
        while x < 1 or x > 6:
            print('Invalid option!! Please choose any among 1 to 6.')
            x = int(input('>>>'))

        return x
    except :
        print('Invalid option!! Please choose any among 1 to 6.')


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
        print('\t6 - Quit')

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
            quit()
