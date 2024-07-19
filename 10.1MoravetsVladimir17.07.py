import pickle


class Node:
    def __init__(self, key, value, next_key_val=None):
        self.key = key
        self.value = value
        self.next_key_val = next_key_val


class CountryState:
    def __init__(self, key_val=None):
        self.key_val = key_val

    def insert_in_head(self, key, value):
        new = Node(key, value)
        if self.key_val is None:
            self.key_val = new

        else:
            new.next_key_val = self.key_val
            self.key_val = new

    def insert_in_tail(self, key, value):
        new = Node(key, value)
        current_pos_key = self.key_val
        if current_pos_key is None:
            self.key_val = new
        else:
            while current_pos_key is not None:
                if current_pos_key.next_key_val is None:
                    current_pos_key.next_key_val = new
                    return
                current_pos_key = current_pos_key.next_key_val

    def delete_by_key(self, data):
        current_pos_key = self.key_val
        if current_pos_key.key == data:
            self.key_val = self.key_val.next_key_val
        else:
            # current_pos_key = current_pos_key.next_key_val
            while current_pos_key.next_key_val is not None:
                if current_pos_key.next_key_val.key == data:
                    current_pos_key.next_key_val = current_pos_key.next_key_val.next_key_val
                    return
                current_pos_key = current_pos_key.next_key_val
            return


    def print_all(self):
        current_pos_key = self.key_val
        s = ''
        while current_pos_key is not None:
            s += f'{current_pos_key.key}: {current_pos_key.value}\n'
            current_pos_key = current_pos_key.next_key_val
        return s

    def search_by_key(self, data):
        current_pos_key = self.key_val
        while current_pos_key:
            if current_pos_key.key == data:
                return current_pos_key.value
            current_pos_key = current_pos_key.next_key_val

    def search_by_value(self, data):
        current_pos_value = self.key_val
        while current_pos_value:
            if current_pos_value.value == data:
                return current_pos_value.key
            current_pos_value = current_pos_value.next_key_val

    def edit_value(self, key, data):
        current_pos_key = self.key_val
        while current_pos_key:
            if current_pos_key.key == key:
                current_pos_key.value = data
                return
            current_pos_key = current_pos_key.next_key_val

    def ser_files(self):
        s = self.print_all()
        with open('filePickle', 'wb') as file:
            pickle.dump(s, file)

    def des_files(self):
        with open('filePickle', 'rb') as file:
            return pickle.load(file)

dic = CountryState()
dic.insert_in_head('Россия', 'Москва')
dic.insert_in_head('Казахстан', 'Астана')
dic.insert_in_head('Словакия', 'Братислава')
dic.insert_in_head('Австрия', 'Вена')
dic.insert_in_tail('Чехия', 'Прага')
dic.insert_in_tail('Великобритания', 'Лондон')
dic.delete_by_key('Россия')
dic.delete_by_key('Великобритания')
dic.edit_value('Казахстан', 'Нурсултан')
print(dic.print_all())
print()
dic.ser_files()
print(dic.des_files())
# print(dic.search_by_key('Лягушка'))
# print(dic.search_by_value('Хрю'))