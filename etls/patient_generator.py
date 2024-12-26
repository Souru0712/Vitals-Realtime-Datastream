import random as r  #randomizer
import datetime  #for calculating current age

def generate_patient(bp_state, o2_state, temp_state, gluc_state):  #generate patient based on key attributes
    dob = dob_generator()
    date_attributes = dob.split("/")
    #mm-dd-yyyy

    delta_y = int(datetime.datetime.today().year) - int(date_attributes[2])
    delta_m = int(datetime.datetime.today().month) - int(date_attributes[0])
    delta_d = int(datetime.datetime.today().day) - int(date_attributes[1])

    #if birthday has not passed in the curr year, subtract 1
    if (delta_m <= 0):
        if (delta_d <= 0):
            age = delta_y - 1
        else:
            age = delta_y
    else:
        age = delta_y

    patient = {'First_name': first_name_generator(),
               'Last_name': last_name_generator(),
               'Date_of_birth': dob,
               'Age': age,
               'Phone_number': phone_generator(),
               'SSN': ssn_generator(),
               'Systolic(BP)': sys_generator(bp_state),
               'Diastolic(BP)': dia_generator(bp_state),
               'Oxygen_saturation': o2_generator(o2_state),
               'Heart_rate': hr_generator(age),
               'Respiratory_rate': rr_generator(age),
               'Temperature': temp_generator(temp_state),
               'Glucose_levels': glucose_generator(gluc_state)}

    return patient


def first_name_generator():
    first_name = ['Liam', 'Noah', 'James', 'Elijah', 'Kevin', 'Jason', 'Lucas', 'John',
                  'Tommy', 'Mustafa', 'Katherine', 'Jessica', 'David', 'Harri', 'Hamza', 'Vivian', 'Josh', 'Logan',
                  'Velma', 'Duncan', 'Douglas', 'Betty', 'Harold', 'Samuel', 'Connor', 'Oscar', 'Dorothy', 'Thea',
                  'Simon', 'Megan', 'Kelly', 'Athena', 'Isabelle', 'Jenny', 'Sally', 'Ernest', 'Jennifer', 'William',
                  'Carlos', 'Ada', 'Bella', 'Cathy', 'Stacey', 'Hershel', 'Johnnie', 'Barbara', 'Felton', 'Carrol',
                  'Wes', 'Andre', 'Ilene', 'Waldo', 'Brandi', 'Dexter', 'Tonia', 'Jordan', 'Raymond', 'Judson', 'Cara',
                  'Jerald']

    return r.choice(first_name)


def last_name_generator():
    last_name = ['Smith', 'Johnson', 'Brown', 'Chen', 'Lin', 'Zhang', 'Jones', 'Miller', 'Davis', 'Gomez', 'Martinez',
                 'Hernandez', 'Gonzales', 'Wilson', 'Thomas', 'Taylor', 'Jackson', 'Martin', 'Garcia', 'Lopez',
                 'Anderson', 'Moore', 'Lee', 'Thompson', 'White', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Young',
                 'Allen', 'Holt', 'Adkins', 'Lyons', 'Leblanc', 'Huynh', 'Mullins', 'Mays', 'Potter', 'Navarro',
                 'Keith', 'Love', 'Murray', 'Simpson', 'Cohen', 'Beard', 'Valencia', 'Hickman', 'Ward', 'Gaines']

    return r.choice(last_name)


def leap_year(year):
    if ((int(year) % 400 == 0) or (int(year) % 100 != 0) and (int(year) % 4 == 0)):  #is a leap year
        return 29
    else:
        return 28


def dob_generator():  #date of birth
    month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    month = r.choice(month_list)
    year = str(r.randint(1949, 2005))
    switch = {
        '01': 31,
        '02': leap_year(year),
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }
    day = r.randint(1, (switch.get(month)))
    if(day < 10):
        day = '0'+str(day)
    else:
        day = str(day)

    date_of_birth = ''.join(month + "/" + day + "/" + year)
    return date_of_birth


def phone_generator():  #phone number
    phone = list("000-000-0000")
    area_codes = [205, 251, 256, 334, 659, 938, 907, 480, 520, 602, 623, 928,
                  327, 479, 501, 870, 209, 213, 279, 310, 323, 341, 350, 369, 408, 415, 424, 442, 510, 530, 559, 562,
                  619, 626, 628, 650, 657, 661, 669, 707, 714, 747, 760, 805, 818, 820, 831, 840, 858, 909, 916, 925,
                  949, 951, 303, 719, 720, 970, 983, 203, 475, 860, 959, 302, 239, 305, 321, 324, 352, 386, 407, 448,
                  561, 645, 656, 689, 727, 728, 754, 772, 786, 813, 850, 863, 904, 941, 954, 229, 404, 470, 478, 678,
                  706, 762, 770, 912, 943, 808, 208, 986, 217, 224, 309, 312, 331, 447, 464, 618, 630, 708, 730, 773,
                  779, 815, 847, 861, 872, 219, 260, 317, 463, 574, 765, 812, 930, 319, 515, 563, 641, 712, 316, 620,
                  785, 913, 270, 364, 502, 606, 859, 225, 318, 337, 504, 985, 207, 227, 240, 301, 410, 443, 667, 339,
                  351, 413, 508, 617, 774, 781, 857, 978, 231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989,
                  218, 320, 507, 612, 651, 763, 952, 228, 601, 662, 769, 235, 314, 417, 557, 573, 636, 660, 816, 975,
                  406, 308, 402, 531, 702, 725, 775, 603, 201, 551, 609, 640, 732, 848, 856, 862, 908, 973, 505, 575,
                  212, 315, 329, 332, 347, 363, 516, 518, 585, 607, 624, 631, 646, 680, 716, 718, 838, 845, 914, 917,
                  929, 934, 252, 336, 472, 704, 743, 828, 910, 919, 980, 984, 701, 216, 220, 234, 283, 326, 330, 380,
                  419, 436, 440, 513, 567, 614, 740, 937, 405, 539, 572, 580, 918, 458, 503, 541, 971, 215, 223, 267,
                  272, 412, 445, 484, 570, 582, 610, 717, 724, 814, 835, 878, 401, 803, 839, 843, 854, 864, 605, 423,
                  615, 629, 731, 865, 901, 931, 210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713,
                  726, 737, 806, 817, 830, 832, 903, 915, 936, 940, 945, 956, 972, 979, 385, 435, 801, 802, 276, 434,
                  540, 571, 686, 703, 757, 804, 826, 948, 206, 253, 360, 425, 509, 564, 202, 771, 304, 681, 262, 274,
                  353, 414, 534, 608, 715, 920, 307]

    for i in range(4, 7):
        phone[i] = str(r.randint(0, 9))
    for i in range(8, 12):
        phone[i] = str(r.randint(0, 9))

    area_code = str(r.choice(area_codes))
    telephone_and_line = ''
    for i in range(3, 12):
        telephone_and_line += phone[i]

    phone = ''.join(area_code + telephone_and_line)
    return phone


def ssn_generator():  #social security

    ssn = list("000-00-0000")
    for i in range(0, 3):
        ssn[i] = str(r.randint(0, 9))
    for i in range(4, 6):
        ssn[i] = str(r.randint(0, 9))
    for i in range(7, 11):
        ssn[i] = str(r.randint(0, 9))

    ssn = ''.join(ssn)
    return ssn


def sys_generator(state):  #Blood Pressure
    if (state == 'n'):
        systolic = r.randint(100, 120)
    elif (state == 'e'):
        systolic = r.randint(120, 129)
    elif (state == 'h1'):
        systolic = r.randint(130, 139)
    else:
        systolic = r.randint(140, 180)

    return systolic


def dia_generator(state):
    if (state == 'n'):
        diastolic = r.randint(67, 79)
    elif (state == 'e'):
        diastolic = r.randint(67, 79)
    elif (state == 'h1'):
        diastolic = r.randint(80, 90)
    else:
        diastolic = r.randint(90, 120)

    return diastolic

    # print("Blood Pressure: Sys - " + str(systolic) + ". Dia - " + str(diastolic))
    # if (systolic >= 120):
    #     print("Warning!! Elevated blood pressures have been detected")
    # else:
    #     print("Normal blood pressure")


def o2_generator(state):  # Oxygen saturation (SpO2) (Multiple sources have different category thresholds)
    #thresholds are determined by args

    if (state == 'n'):
        Oxygen_saturation = r.randint(95, 100)
    elif (state == 'h1'):  #hypoxia1
        Oxygen_saturation = r.randint(90, 94)
    elif (state == 'h2'):  #hypoxia2
        Oxygen_saturation = r.randint(85, 89)
    else:  #hypoxia3
        Oxygen_saturation = r.randint(67, 84)

    return Oxygen_saturation


def hr_generator(age):  # Heart rates
    if (age <= 20 and age < 30):
        heart_rate = r.randint(100, 170)
    elif (30 <= age and age < 35):
        heart_rate = r.randint(95, 162)
    elif (35 <= age and age < 40):
        heart_rate = r.randint(93, 157)
    elif (40 <= age and age < 45):
        heart_rate = r.randint(90, 153)
    elif (45 <= age and age < 50):
        heart_rate = r.randint(88, 149)
    elif (50 <= age and age < 55):
        heart_rate = r.randint(85, 145)
    elif (55 <= age and age < 60):
        heart_rate = r.randint(83, 140)
    elif (60 <= age and age < 65):
        heart_rate = r.randint(80, 136)
    elif (65 <= age and age < 70):
        heart_rate = r.randint(78, 132)
    else:
        heart_rate = r.randint(75, 128)

    return heart_rate


def rr_generator(age):  # Respiratory rate
    if (age <= 1):
        respiratory_rate = r.randint(30, 40)
    elif (1 < age and age <= 5):
        respiratory_rate = r.randint(20, 40)
    elif (5 < age and age <= 10):
        respiratory_rate = r.randint(15, 25)
    elif (10 < age and age <= 18):
        respiratory_rate = r.randint(15, 20)
    elif (18 < age and age <= 70):
        respiratory_rate = r.randint(12, 20)
    elif (70 < age):
        respiratory_rate = r.randint(15, 20)

    return respiratory_rate


def temp_generator(state):  # Temperature
    if (state == 'n'):
        temperature = r.uniform(98.6, 100.4)
    elif (state == 'low'):
        temperature = r.uniform(100.5, 102.2)
    elif (state == 'mid'):
        temperature = r.uniform(102.2, 104.0)
    elif (state == 'high'):
        temperature = r.uniform(104.1, 106.0)
    else:
        temperature = r.uniform(106, 108)

    return round(temperature, 1)  #round to 1 decimal place


def glucose_generator(state):  # Glucose levels: mg/dL
    #resting
    if (state == 'o'):
        glucose_level = r.randint(65, 97)
    elif (state == 'n'):
        glucose_level = r.randint(101, 115)
    elif (state == 'e'):
        glucose_level = r.randint(118, 133)
    elif (state == 'd'):
        glucose_level = r.randint(136, 151)
    else:
        glucose_level = r.randint(154, 168)

    return glucose_level


#enter 4 parameters for generate_patients():
    #bp_state (n, h1, h2, or none)
    #o2_state (n, h1, h2, or none)
    #temp_state (n, low, mid, high, none)
    #gluc_state (o, n, e, d)

# bp_inp = input("Please enter a blood pressure state: \n"
#                "'n' for normal.\n"
#                "'h1' for hypertension I.\n"
#                "'h2' for hypertension II.\n"
#                "Or leave blank for extreme.\n")
# o2_inp = input("Please enter a oxygen saturation state: \n"
#                "'n' for normal.\n"
#                "'h1' for hypoxia I.\n"
#                "'h2' for hypoxia II.\n"
#                "Or leave blank for extreme.\n")
# temp_inp = input("Please enter a temperature state: \n"
#                "'n' for normal.\n"
#                "'low' for low fever.\n"
#                "'mid' for medium fever.\n"
#                "'high' for high fever.\n"
#                "Or leave blank for extreme.\n")
# gluc_inp = input("Please enter a blood pressure state: \n"
#                "'o' for optimal.\n"
#                "'n' for normal.\n"
#                "'e' for elevated or prediabetic.\n"
#                "'d' for diabetic.\n")
#
# patient = generate_patient(bp_inp,o2_inp, temp_inp,gluc_inp)
# print()
# print("The pressure readings were: \n"
#       +str(patient.get("Systolic(BP)")) +" Sys\n"
#       +str(patient.get("Diastolic(BP)")) +" Dia\n")
# print("The oxygen saturation readings were: \n"
#       +str(patient.get("Oxygen_saturation"))+"%\n")
# print("The temperature readings were: \n"
#       +str(patient.get("Temperature"))+" F\n")
# print("The glucose level readings were: \n"
#       +str(patient.get("Glucose_levels")) +" mg/dL\n")
# print(patient)