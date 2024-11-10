def only_text(text: str) -> str:
    return input(text)

def only_number(text: str) -> int:
    value: str = input(text)
    if not value.isnumeric():
        return "El valor no es valido"
    return int(value)