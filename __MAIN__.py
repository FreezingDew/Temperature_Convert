def c_to_f(value):
    return (value * 1.8) + 32


def f_to_c(value):

    return (value - 32) / 1.8


while True:

    user_sel = input("Hi, Enter the wanted input method. Celsius or Fahrenheit(C/F):")
    if "c" in user_sel.lower():

        user_in = input("Degrees Celsius: ")
        if user_in == [0-9] or "," not in user_in:
            print("In Fahrenheit: " + str(round(c_to_f(float(user_in)), 1)))  # string>float>Fahrenheit>rounded>string

            input("Press key to do another one...")
            continue
        else:
            print("Sorry, Must be a number. And if it is a decimal value, it should be divided with a '.'(dot)")

    elif "f" in user_sel.lower():

        user_in = input("Degrees Fahrenheit: ")
        if user_in == [0-9] or "," not in user_in:
            print("In Celsius: " + str(round(f_to_c(float(user_in)), 1)))  # string>float>Celsius>rounded>string

            input("Press key to do another one...")
            continue

        else:
            print("Sorry, Must be a number. And if it is a decimal value, it should be divided with a '.'(dot)")

    else:
        print("Sorry, only 'C' or 'F' is available :(")
        continue
