num1 = int(input("Masukkan angka :"))
num2 = int(input("Masukkan angka :"))

try:
    result = num1/num2
    print("Result : ", result)
except ZeroDivisionError:
    print("Undefined")
except TypeError:
    print("Must Number")
except Exception:
    print("Error")