import sqlite3

class dbhandler:

    def __init__(self,name_dictionary,dictionary) -> None:
        self.__connection = sqlite3.connect("dictionary.db")
        self.__name_dictionary = name_dictionary
        self.__dictionary = dictionary

    def download_list(self):

        try:

            insert_command_dictionary = "insert into dictionary values('{}');".format(str(self.__name_dictionary))
            self.__connection.execute(insert_command_dictionary)

            with open(self.__dictionary,"r") as file_dictionary:
                content = file_dictionary.readlines()

                for value in content:
                    insert_command_dictionary_record = "insert into content(name_dictionary,value) values('{}','{}');".format(str(self.__name_dictionary),str(value.rstrip()))
                    self.__connection.execute(insert_command_dictionary_record)

            self.__connection.commit()
        except Exception as exception:
            print(exception)