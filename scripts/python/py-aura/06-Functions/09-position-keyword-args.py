def dump_student_details_1(name, age, marks):
    print ("name :%s, age :%d, marks :%d" % (name, age, marks))

def dump_student_details_2(name, age, marks=100):
    print ("name :%s, age :%d, marks :%d" % (name, age, marks))

def dump_student_details_3(name, age=1, marks=100):
    print ("name :%s, age :%d, marks :%d" % (name, age, marks))

def dump_student_details_4(message, *values):  # The only difference
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

        values_str = [str(x) for x in values]
        print(message, values_str)

def main():
    dump_student_details_1("Aura", 2, 90)
    dump_student_details_2("Aura", 2)
    dump_student_details_3("Aura")
    dump_student_details_3("Aura", marks=80, age=3)
    dump_student_details_3("Aura", marks=80)
    dump_student_details_3(name="Aura", marks=80, age=3)
    dump_student_details_4('Aura', 4, 10, 20, 30, 40)
    return

if (__name__ == "__main__"):
    main()
