from sys import argv

argv.pop(0)

match len(argv[:4]):
    case 4:
        argv.pop(2)
    case 6:
        argv.pop(2)
    case _:
        raise ValueError("Invalid number of arguments!")

for index, arg in enumerate(argv[1:]):
    try:
        int(float(arg))
    except ValueError:
        raise ValueError("Invalid arguments!")

dimension: str = argv[0]
x: int = int(float(argv[1]))
z: int = int(float(argv[2]))


match dimension:
    case "nether":
        x //= 8
        z //= 8
    case "overworld":
        x *= 8
        z *= 8
    case _:
        raise ValueError("Invalid dimension!")

print(f"{x = }\n{z = }")
