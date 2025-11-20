def calculate_total(price: float, qty: int) -> float:
    return price * qty

# mypy flag error: Function is missing a return type annotation (no-untyped-def)
# def calculate_total_mypy(price: float, qty: int):
#     return price * qty

if __name__ == "__main__":
    print("Running with type hints")
    print(calculate_total(10.0, 2))
    # print("Running without type hints")
    # print(calculate_total_mypy(10.0, 2))
