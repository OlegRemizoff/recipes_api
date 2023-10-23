arr = [{"time": 10, "description": "Подготовить продукты."}, {"time": 20, "description": "Картофель очистить и нарезать средними кусочками.."}, {"time": 2, "description": "Поместить нарезанный картофель в сотейник или в сито, установленное над кастрюлей, и залить кипятком."}]




def get_total_time():
    counter = 0
    for i in arr:
        counter += i['time']
    return counter


