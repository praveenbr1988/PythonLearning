appt_status_list=[]
with open("C:/Users/techi/PycharmProjects/PythonProject/File/appointments.csv",'r') as file:
    next(file) # if the file has header and to skip it, use this else no need
    for line in file:
        appointment_status=line.strip().split(",")[5]
        appt_status_list.append(appointment_status)
    print(appt_status_list)
    appt_status_set=set(appt_status_list)
    print(appt_status_set)

valid_status_set={'Pending', 'Completed'}

#Invalid_status=appt_status_set-valid_status_set
Invalid_status=appt_status_set.difference(valid_status_set)
print(Invalid_status)

#To create an EMpty set , we cannot declare like empty_set={}. It denotes Dictionary. To create empty set, use below
empty_set=set()
print(type(empty_set))

################################################################################################################
