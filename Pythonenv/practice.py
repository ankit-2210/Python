import requests
from bs4 import BeautifulSoup


def print_secret_message(doc_url: str):
    response = requests.get(doc_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    lines = [line.strip() for line in soup.get_text("\n").splitlines()]
    lines = [line for line in lines if line]

    data = []
    i = 0

    while i < len(lines) and not lines[i].isdigit():
        i += 1

    while i + 2 < len(lines):
        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])

            data.append((x, y, char))
            i += 3

        except ValueError:
            i += 1

    if not data:
        print("No valid coordinate data found.")
        return

    print(data)

    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, y, _ in data)
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, char in data:
        grid[y][x] = char
    for row in grid:
        print("".join(row))


# print_secret_message(
#     "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
# )

print_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)
