def find_common_participants(first_group, second_group, separator=','):
    first_group = first_group.split(sep=separator)
    second_group = second_group.split(sep=separator)
    common_participants = list(set(first_group).intersection(second_group))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", participants)
