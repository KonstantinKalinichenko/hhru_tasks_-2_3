def solve(input_string: str):
    punctuation = "!-,.?"
    splitted = input_string.split()
    lowered = list(map(str.lower, splitted))
    clean = {i.strip(punctuation) for i in lowered}
    clean.discard('')
    return str(len(clean))


if __name__ == "__main__":
    input_string = input()
    result = solve(input_string)
    print(result)