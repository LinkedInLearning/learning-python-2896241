#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is same as y"
    else:
        result = "x is greater than y"
    print(result)

    # conditional statements let you use "a if C else b"
    result = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(result)

    # Python does not have support for higher-order conditionals
    # like "switch-case" in other languages


if __name__ == "__main__":
    main()
