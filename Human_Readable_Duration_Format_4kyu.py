def format_duration(secs):
    def return_s(word, time_dict):
        write_word = word
        if time_dict[word] > 1:
            write_word += 's'
            return write_word
        else:
            return write_word
    if secs == 0: return 'now'
    result = ""

    time_dict = {
                'year': 0,
                'day': 0,
                'hour': 0,
                'minute': 0,
                'second': 0
    }

    times = [31536000, 86400, 3600, 60, 1]
    for i in range(len(times)):
        while secs >= times[i]:
            secs = secs - times[i]
            if times[i] == 31536000:
                time_dict['year'] += 1
            elif times[i] == 86400:
                time_dict['day'] += 1
            elif times[i] == 3600:
                time_dict['hour'] += 1
            elif times[i] == 60:
                time_dict['minute'] += 1
            elif times[i] == 1:
                time_dict['second'] += 1

    words_list_not_changed = []
    num_of_time_unit = []
    words_list = []

    for key in time_dict:
        if time_dict[key] != 0:
            words_list_not_changed.append(key)
            num_of_time_unit.append(time_dict[key])

    for item in words_list_not_changed:
        words_list.append(return_s(item, time_dict))

    updated_dict_of_time = {}
    for i in range(len(words_list)):
        if num_of_time_unit[i] != 0:
            updated_dict_of_time.update({words_list[i]:num_of_time_unit[i]})

    i = 0
    for key in updated_dict_of_time:
        if len(words_list) == 1:
            return str(updated_dict_of_time[key]) + " " + key
        if i == len(words_list) - 1:
            result = result[:-2]
            result += " and " + str(updated_dict_of_time[key]) + " " + key
        else:
            result += str(updated_dict_of_time[key]) + " " + key + ", "
        i += 1
    return result
