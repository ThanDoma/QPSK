def check(check_new_1_2_3, check_new_1_2_4, check_new_1_3_4, check_new_2_3_4, dist):
    quarter_1_2_3 = check_new_1_2_3
    quarter_1_2_4 = check_new_1_2_4
    quarter_1_3_4 = check_new_1_3_4
    quarter_2_3_4 = check_new_2_3_4

    checked_1_2_3, checked_1_3_4, checked_1_2_4 = [], [], []
    checked_2_3_4 = []

    # Исключение запрещенных комбинаций I, II, III четвертей
    if len(quarter_1_2_3) == 128:
        for i in range(0, 128, 2):
            checked_1_2_3.append([quarter_1_2_3[i], quarter_1_2_3[i+1]])

        def remove_duplicates(arr):
            check_arr = arr
            unique_arr = []

            for sublist in arr:
                i = 0
                el = check_arr.pop(i)

                if el not in check_arr:
                    unique_arr.append(el)

                i += 1
                check_arr.append(el)
            return unique_arr

        new_quarter_1_2_3 = remove_duplicates(checked_1_2_3)
        new_quarter_1_2_3_ = new_quarter_1_2_3
        
        count = []
        count_ = []
        
        for i in range(len(new_quarter_1_2_3)):
            for j in range(i+1, len(new_quarter_1_2_3_)):
            
                if (abs(new_quarter_1_2_3[i][0] - new_quarter_1_2_3_[j][0]) <= dist) and (abs(new_quarter_1_2_3[i][1] - new_quarter_1_2_3_[j][1]) <= dist):
                    count.append(j)
                    count_.append(i)
                    
        count = list(set(list(set(count)) + list(set(count_))))
        
        for i in sorted(count, reverse=True):
            del new_quarter_1_2_3[i]
        
    elif len(quarter_1_2_3) == 0:
        pass

    # Исключение запрещенных комбинаций I, III и IV четвертей
    if len(quarter_1_3_4) == 128:
        for i in range(0, 128, 2):
            checked_1_3_4.append([quarter_1_3_4[i], quarter_1_3_4[i + 1]])

        def remove_duplicates(arr):
            check_arr = arr
            unique_arr = []

            for sublist in arr:
                i = 0
                el = check_arr.pop(i)

                if el not in check_arr:
                    unique_arr.append(el)

                i += 1
                check_arr.append(el)
            return unique_arr

        new_quarter_1_3_4 = remove_duplicates(checked_1_3_4)
        new_quarter_1_3_4_ = new_quarter_1_3_4
        
        count = []
        count_ = []
        
        for i in range(len(new_quarter_1_3_4)):
            for j in range(i+1, len(new_quarter_1_3_4_)):
            
                if (abs(new_quarter_1_3_4[i][0] - new_quarter_1_3_4_[j][0]) <= dist) and (abs(new_quarter_1_3_4[i][1] - new_quarter_1_3_4_[j][1]) <= dist):
                    count.append(j)
                    count_.append(i)
                    
        count = list(set(list(set(count)) + list(set(count_))))
        
        for i in sorted(count, reverse=True):
            del new_quarter_1_3_4[i]
    elif len(quarter_1_3_4) == 0:
        pass

    # Исключение запрещенных комбинаций I, II и IV четвертей
    if len(quarter_1_2_4) == 128:
        for i in range(0, 128, 2):
            checked_1_2_4.append([quarter_1_2_4[i], quarter_1_2_4[i + 1]])

        def remove_duplicates(arr):
            check_arr = arr
            unique_arr = []

            for sublist in arr:
                i = 0
                el = check_arr.pop(i)

                if el not in check_arr:
                    unique_arr.append(el)

                i += 1
                check_arr.append(el)
            return unique_arr

        new_quarter_1_2_4 = remove_duplicates(checked_1_2_4)
        new_quarter_1_2_4_ = new_quarter_1_2_4
        
        count = []
        count_ = []
        
        for i in range(len(new_quarter_1_2_4)):
            for j in range(i+1, len(new_quarter_1_2_4_)):
            
                if (abs(new_quarter_1_2_4[i][0] - new_quarter_1_2_4_[j][0]) <= dist) and (abs(new_quarter_1_2_4[i][1] - new_quarter_1_2_4_[j][1]) <= dist):
                    count.append(j)
                    count_.append(i)
                    
        count = list(set(list(set(count)) + list(set(count_))))
        
        for i in sorted(count, reverse=True):
            del new_quarter_1_2_4[i]
    elif len(quarter_1_2_4) == 0:
        pass
    
    # Исключение запрещенных комбинаций II, III и IV четвертей
    if len(quarter_2_3_4) == 128:
        for i in range(0, 128, 2):
            checked_2_3_4.append([quarter_2_3_4[i], quarter_2_3_4[i + 1]])

        def remove_duplicates(arr):
            check_arr = arr
            unique_arr = []

            for sublist in arr:
                i = 0
                el = check_arr.pop(i)

                if el not in check_arr:
                    unique_arr.append(el)

                i += 1
                check_arr.append(el)
            return unique_arr

        new_quarter_2_3_4 = remove_duplicates(checked_2_3_4)
        new_quarter_2_3_4_ = new_quarter_2_3_4
        
        count = []
        count_ = []
        
        for i in range(len(new_quarter_2_3_4)):
            for j in range(i+1, len(new_quarter_2_3_4_)):
            
                if (abs(new_quarter_2_3_4[i][0] - new_quarter_2_3_4_[j][0]) <= dist) and (abs(new_quarter_2_3_4[i][1] - new_quarter_2_3_4_[j][1]) <= dist):
                    count.append(j)
                    count_.append(i)
                    
        count = list(set(list(set(count)) + list(set(count_))))
        
        for i in sorted(count, reverse=True):
            del new_quarter_2_3_4[i]
    elif len(quarter_2_3_4) == 0:
        pass
    
    return new_quarter_1_2_3, new_quarter_1_3_4, new_quarter_1_2_4, new_quarter_2_3_4