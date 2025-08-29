g = input("Enter the gender: ").lower()
hg = float(input("Enter hemoglobin level: "))

if g == "female":
    if hg < 117:
        print("Hemoglobin value is LOW!")
    elif hg <= 155:
        print("Hemoglobin value is NORMAL.")
    else:
        print("Hemoglobin value is HIGH.")

if g == "male":
    if hg < 134:
        print("Hemoglobin level is LOW!")
    elif hg <= 167:
        print("Hemoglobin level is NORMAL")
    else:
        print("Hemoglobin level is HIGH!!!")



