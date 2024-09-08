import pickle
import json

# class Auto:
#     def __init__(self, mileage, max_speed, year_of_purchase):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.year_of_purchase = year_of_purchase
#
#     def days_of_using(self):
#         num_of_days = self.mileage / self.max_speed
#         return num_of_days #В среднем машина использовалась {num_of_days} раз
#
#     def frequency_of_use(self):
#         num_of_days = self.mileage / self.max_speed
#         days = (2024 - self.year_of_purchase) * 365
#         return days / num_of_days #Машина использовалась раз в {days / num_of_days} сутки
#
#     def ret_all(self):
#         s = {
#             'mileage': self.mileage,
#             'max_speed': self.max_speed,
#             'year_of_purchase': self.year_of_purchase,
#             'days_of_using': self.days_of_using(),
#             'frequency_of_use': self.frequency_of_use()
#         }
#         return s
#
#     def ser_files_pickle(self):
#         s = self.ret_all()
#         with open('forDeSerAuto.txt', 'wb') as file:
#             pickle.dump(s, file)
#
#
#     def des_files_pickle(self):
#         with open('forDeSerAuto.txt', 'rb') as file:
#             s = pickle.load(file)
#         return s
#
#     def ser_files_json(self, obj):
#         with open('autoJSON.json', 'w', encoding='utf-8') as file:
#             json.dump(obj, file, default=lambda obj: obj.__dict__, indent=1, ensure_ascii=False)
#
#     def des_files_json(self):
#         with open('autoJSON.json', 'r') as file:
#             s = json.load(file)
#         return s



# sportCar = Auto(200000, 400, 2022)
# print(sportCar.days_of_using())
# print(sportCar.frequency_of_use())
# print('\n')
# sportCar.ser_files_pickle()
# print(sportCar.des_files_pickle(), 'pickle')
# sportCar.ser_files_json(sportCar)
# print(sportCar.des_files_json(), 'json')













# class Book:
#     def __init__(self, name, year, num_of_words, speed_of_reading):
#         self.name = name
#         self.year = year
#         self.num_of_words = num_of_words
#         self.speed_of_reading = speed_of_reading
#
#     def time_of_reading(self):
#         return self.num_of_words // self.speed_of_reading
#
#     def years_old(self):
#         return 2024 - self.year
#
#     def ret_all(self):
#         s = {
#             'name': self.name,
#             'year': self.year,
#             'num_of_words': self.num_of_words,
#             'time_of_reading': self.time_of_reading(),
#             'years_old': self.years_old()
#         }
#         return s
#
#     def ser_files_pickle(self):
#         s = self.ret_all()
#         with open('bookPickle.txt', 'wb') as file:
#             pickle.dump(s, file, pickle.HIGHEST_PROTOCOL)
#
#     def des_files_pickle(self):
#         with open('bookPickle.txt', 'rb') as file:
#             s = pickle.load(file)
#         return s
#
# class BookEncoder(json.JSONEncoder):
#     def default(self, obj):
#         return {
#             'Name': obj.name,
#             'Year': obj.year,
#             'Number of words': obj.num_of_words,
#             'Speed of reading': obj.speed_of_reading,
#             'Methods': {
#                 'Time of reading': obj.time_of_reading(),
#                 'Years old': obj.years_old()
#             }
#         }
#
#
#
#
# book = Book('Маленький принц', 1982, 12343, 200)
# print(book.time_of_reading())
# print(book.years_old())
# book.ser_files_pickle()
# print(book.des_files_pickle())
# with open('bookJSON.txt', 'w', encoding='utf-8') as file:
#     json.dump(book, file, cls=BookEncoder, ensure_ascii=False, indent=2)
#
# with open('bookJSON.txt', 'r', encoding='utf-8') as file:
#     py_data = json.load(file)
# print(py_data)











class Stadium:
    def __init__(self, year_of_construction, km, speed_kmh):
        self.year_of_construction = year_of_construction
        self.km = km
        self.speed_kmh = speed_kmh

    def years_old(self):
        return 2024 - self.year_of_construction

    def time_to_run(self):
        return self.km / self.speed_kmh

    def ret_all(self):
        s = {
            'year_of_construction': self.year_of_construction,
            'km': self.km,
            'speed_kmh': self.speed_kmh,
            'Methods': {
                'years_old': self.years_old(),
                'time_to_run': self.time_to_run()
            }
        }
        return s

    def ser_files_pickle(self):
        s = self.ret_all()
        with open('stadiumPickle.txt', 'wb') as file:
            pickle.dump(s, file)

    def des_files_pickle(self):
        with open('stadiumPickle.txt', 'rb') as file:
            data = pickle.load(file)
            return data

st = Stadium(2000, 5, 2)

class JSONDataAdapter:
    @staticmethod
    def to_json(obj):
        if isinstance(obj, Stadium):
            return json.dumps({
                'year_of_construction': obj.year_of_construction,
                'km': obj.km,
                'speed_kmh': obj.speed_kmh,
                'Methods': {
                    'years_old': obj.years_old(),
                    'time_to_run': obj.time_to_run()
                }
            })

    @staticmethod
    def from_json(obj):
        obj_dict = json.loads(obj)
        return obj_dict


st.ser_files_pickle()
print(st.des_files_pickle(), 'из файла pickle')

st_one = JSONDataAdapter.to_json(st)
print(st_one)
st_obj = JSONDataAdapter.from_json(st_one)
print(st_obj, 'из строки')

with open('stadiumJSON.txt', 'w', encoding='utf-8') as file:
    file.write(st_one)

with open('stadiumJSON.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data, 'из файла')