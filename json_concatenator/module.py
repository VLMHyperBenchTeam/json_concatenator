import os
import json


class JSON_concat():

    def __init__(self, input_json_list,
                 config_path='config_json_out.json'):
        self.input_json_list = input_json_list
        self.query_json = self.__init_config(config_path)
        #self.output_json = self._make_json_out(self.input_json_list)

    def __init_config(self, config_path) -> dict:
        """Config for output json initialisation function"""

        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as file:
                config_json_out = json.load(file)
        else:
            config_json_out = {
                # 'page_total': 'Количество страниц в файле',
                # 'has_passport_rf': 'Наличие российского паспорта',
                # 'document_number': 'Исх. номер',
                # 'doc_type': 'Тип документа',
                # 'corr_type': 'Тип корреспондента',
                'date_of_birth': 'Дату рождения клиента',
                'fio': 'ФИО клиента',
                # 'issuing_fio': 'ФИО корреспондента',
                # 'client_INN': 'ИНН клиента',
                # 'corr_INN': 'ИНН корреспондента',
                # 'corr_address': 'Адрес корреспондента',
                # 'document_topic': 'Тема документа',

            }

        return config_json_out

    def make_json_out(self) -> dict:
        """Output json initialisation function"""

        json_out = {}
        for query in self.query_json:
            json_out[query] = []
            for input_json in self.input_json_list:
                if query in input_json.keys():
                    # if query in json_out.keys():
                    json_out[query].append(input_json[query])

        return json_out
    