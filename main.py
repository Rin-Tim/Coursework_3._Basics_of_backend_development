from backend.utils import last_executed_five, operation_from_and_to, data_fix


def main():
    a = last_executed_five()
    for i in a:
        print(f"""{data_fix(i)} {i['description']}
{operation_from_and_to(i)}
{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n""")


main()
