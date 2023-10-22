import re

import openpyxl

R_FAULT_rabbit = re.compile(r"^R-FAULT rabbitmq", flags=re.I|re.M)
S_FAULT_rabbit = re.compile(r"^S-FAULT rabbit", flags=re.I|re.M)
execution_error = re.compile(r"(to execute|выполнен|запис|публикац)", flags=re.I|re.M)
validation_error = re.compile(r"(invalid|valid|валидац|отсутствует|подписание по старому)", flags=re.I|re.M)
failed_exception_handle = re.compile(r"(error|exception|unhandled|failed|ошибк)", flags=re.I|re.M)
database_error = re.compile(r"(database|query|select|insert|sql|WHERE)", flags=re.I|re.M)
file_handle_error = re.compile(r"(file)", flags=re.I|re.M)
timeout_error = re.compile(r"(timeout|timed)", flags=re.I|re.M)
already_error = re.compile(r"(already)", flags=re.I|re.M)
verify_error = re.compile(r"(verify)", flags=re.I|re.M)
query_error = re.compile(r"(to get|to send|to set|не загрузил|запрос|обращен|опрос|скачать|получен)", flags=re.I|re.M)
parsing_error = re.compile(r"parse", flags=re.I|re.M)
process_error = re.compile(r"(process|обработ)", flags=re.I|re.M)
import_error = re.compile(r"(import|импорт)", flags=re.I|re.M)
not_found_error = re.compile(r"not found|не найден", flags=re.I|re.M)
access_error = re.compile(r"доступ|не разрешен", flags=re.I|re.M)
auth_error = re.compile(r"авторизац", flags=re.I|re.M)
actual_error = re.compile(r"актуализ", flags=re.I|re.M)
index_error = re.compile(r"индекс", flags=re.I|re.M)

error_patterns = {
    S_FAULT_rabbit: "ошибка работы с контрактом rabbitmq",
    R_FAULT_rabbit: "ошибка запроса rabbitmq",
    database_error: "ошибка с работой базы данных",
    execution_error: "ошибка выполнения",
    validation_error: "ошибка валидации",
    process_error: "ошибка обработки",
    file_handle_error: "ошибка работы с файлами",
    index_error: "ошибка индексации",
    actual_error: "ошибка актуализации",
    auth_error: "ошибка авторизации",
    timeout_error: "ошибка ожидания",
    already_error: "операция уже выполнена",
    verify_error: "ошибка верификации",
    parsing_error: "ошибка парсинга",
    access_error: "ошибка доступа",
    import_error: "ошибка импорта",
    not_found_error: "not found",
    query_error: "ошибка запроса",
    failed_exception_handle: "ошибка обработки исключений",

}

def classify_error(error_log):
    
    for pattern, classification in error_patterns.items():

        if pattern.search(error_log):
            return classification
        
    return "ошибка обработки исключений"




error_logs = openpyxl.load_workbook("logs.xlsx")
output_results = openpyxl.Workbook()
output_ws = output_results.active

output_ws.append(["id", "create_date", "log", "classification"])


raw_logs_list = error_logs.active

# log = "fdsafdfad to get"

# print(query_error.search(log))

for ind, row in enumerate(raw_logs_list.values):
    if ind == 0:
        continue

    classification = classify_error(row[2])

    output_ws.append([*row, classification])

output_results.save("output.xlsx")