from data import documents, directories


def get_name_by_number(docs=documents, number='11-2'):
    needed_number = number
    result = list(filter(lambda item: item['number'] == needed_number, docs))
    if result == []:
        print('Документа нет в базе')
        return
    else:
        print(result[0]['name'])
        return result[0]['name']


def get_shelf_by_number(shelfs=directories, number='11-2'):
    needed_number = number
    for key, value in shelfs.items():
        if needed_number in value:
            print(f'Номер полки с документом: {key}')
            return key
    print('Документа нет ни на одной полке')
    return


def get_docs_list(docs=documents):
    for item in docs:
        print(item['type'], end=' ')
        print('\"' + item['number'] + '\"', end=' ')
        print('\"' + item['name'] + '\"')
    return docs


def add_new_doc(type, number, name, shelf_):
    doc_type = type
    doc_number = number
    owner_name = name
    shelf = shelf_

    if directories.get(shelf) != None:
        documents.append(
            {"type": doc_type, "number": doc_number,
             "name": owner_name}
        )
        directories[shelf].append(doc_number)
        return 'success'
    else:
        print('Введена несуществующая полка!')
        return 'failure'


def delete_doc(number = '11-2'):
    doc_number = number

    search_result = list(filter(lambda item: \
                                    item['number'] == doc_number, documents))
    if search_result == []:
        print('Удаляемый документ отсутствует в базе')
    else:
        documents.remove(search_result[0])
        print('Документ успешно удален из базы')

    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
            print('Документ успешно удален из перечня полок')
            return 'success'

    print('Перечень полок не содержит информации ' + \
          'об удаляемом документе')
    return


def move_doc_to_another_shelf(number='11-2', shelf='3'):
    doc_number = number
    target_shelf = shelf

    search_result = list(filter(lambda item: item['number'] == doc_number, documents))
    if search_result == []:
        print('Перемещаемый документ отсутствует в базе')
        return 'failure'
    elif directories.get(target_shelf) == None:
        print('Целевая полка отсутствует')
        return 'failure'
    else:
        for key, value in directories.items():
            if doc_number in value:
                value.remove(doc_number)
        directories[target_shelf].append(doc_number)
        return 'success'


def add_shelf(number='4'):
    new_shelf = number

    if directories.get(new_shelf) == None:
        directories.update({new_shelf: []})
        return 'success'
    else:
        print('Новая полка уже существует')
        return 'failure'


def get_shelfs_list(shelfs=directories):
    for key, value in shelfs.items():
        print(key, end=': ')
        for item in value:
            print(item, end='; ')
        print()
    return 'success'


if __name__ == '__main__':
    pass
