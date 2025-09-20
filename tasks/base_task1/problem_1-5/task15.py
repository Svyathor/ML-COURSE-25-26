from typing import List


def hello(name: str = None) -> str:
    if name is None or name == "":
        return "Hello!"
    return f"Hello, {name}!"


def int_to_roman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""
    for i in range(len(values)):
        count = num // values[i]
        result += symbols[i] * count
        num -= values[i] * count

    return result


def longest_common_prefix(strs_input: List[str]) -> str:
    if not strs_input:
        return ""

    strs = [s.lstrip() for s in strs_input]

    if not strs or not strs[0]:
        return ""

    prefix = ""
    min_len = min(len(s) for s in strs)

    for i in range(min_len):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break

    return prefix


def primes() -> int:
    yield 2
    candidate = 3
    while True:
        is_prime = True
        for i in range(3, int(candidate**0.5) + 1, 2):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
        candidate += 2


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = None):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def __call__(self, sum_spent: int):
        if sum_spent > self.total_sum:
            raise ValueError("Not enough money to spend " + str(sum_spent) + " dollars.")
        self.total_sum = self.total_sum - sum_spent
        print("You spent " + str(sum_spent) + " dollars.")

    def __str__(self):
        return "To learn the balance call balance."

    @property
    def balance(self):
        if self.balance_limit is not None and self.balance_limit <= 0:
            raise ValueError("Balance check limits exceeded.")
        if self.balance_limit is not None:
            self.balance_limit = self.balance_limit - 1
        return self.total_sum

    def put(self, sum_put: int):
        self.total_sum = self.total_sum + sum_put
        print("You put " + str(sum_put) + " dollars.")

    def __add__(self, other):
        new_total = self.total_sum + other.total_sum
        new_limit = None
        if self.balance_limit is not None and other.balance_limit is not None:
            new_limit = max(self.balance_limit, other.balance_limit)
        elif self.balance_limit is not None:
            new_limit = self.balance_limit
        elif other.balance_limit is not None:
            new_limit = other.balance_limit
        return BankCard(new_total, new_limit)

