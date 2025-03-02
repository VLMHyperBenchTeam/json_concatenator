from json_concatenator.module import JSON_concat

test_list = [
            {
            "type": "СТРАХОВОЕ СВИДЕТЕЛЬСТВО ОБЯЗАТЕЛЬНОГО ПЕНСИОННОГО СТРАХОВАНИЯ",
            "country": "Российская Федерация",
            "snils_number": "586-339-042 28",
            "fio": "СУББОТИНА АЛЛА РУБЕНОВНА",
            "date_of_birth": "29.09.2015",
            "place_of_birth": "П. КУЩЕВСКАЯ ЕВРЕЙСКАЯ АО",
            "gender": "Женский",
            "registration_date": "28.01.2007"
            },
            {
            "type":"Паспорт",
            "country": "Российская Федерация",
            "issuing_authority": "Управление МВД России по г. Кашира Московская область",
            "date_of_issue": "04.09.2024",
            "document_number": "851-364",
            "fio": "МИХАЙЛОВА НАТАЛЬЯ ЛЕОНИДОВНА",
            "gender": "Жен.",
            "date_of_birth": "22.06.1999",
            "place_of_birth": "Г. ПЕРЕСВЕТ МОСКОВСКАЯ ОБЛАСТЬ",
            "passport_image": "1"
            },
    ]

test = JSON_concat(test_list).make_json_out()
print(test)