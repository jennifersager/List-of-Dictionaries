import pprint

#1 each line is employee info, name, hourly wage
givendata = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

#2 & 3 sort data and no duplicates
listdict = [] #new list
employee = {} #dictionary

for i in givendata:
    if type(i) == int:
        employee["Employee Info"] = i
    elif type(i) == str:
        employee["Full Name"] = i
    elif type(i) == float:
        employee["Hourly Wage"] = i
    else:
        pass

    if len(employee) == 3: #only 3 items of data per employee
        listdict.append(employee)
        employee = {} #redeclare empty dictionary to start over with next employee
print("*****Employee Data*****")
pprint.pprint(listdict) #print list of dictionaries nicely

#4 add total hourly rate
for i in listdict:
    total = round(i["Hourly Wage"] * 1.3, 2)
    i["Total Hourly Rate"] = total

print("\n")
print("*****Employee Data with Total Hourly Rate*****")
pprint.pprint(listdict)

#5 underpaid list
underpaid_salaries = [] #new underpaid list
underpaid_employee = {} #dictionary for each underpaid employee
for i in listdict:
    if i["Total Hourly Rate"] > 28.15 and i["Total Hourly Rate"] < 30.65: #determine who falls in this category
        underpaid_employee.update({"Employee Info":i["Employee Info"]})
        underpaid_employee.update({"Full Name":i["Full Name"]})
        underpaid_employee.update({"Hourly Wage":i["Hourly Wage"]})
        underpaid_employee.update({"Total Hourly Rate":i["Total Hourly Rate"]})
        underpaid_salaries.append(underpaid_employee) #add employee's data to dictionary then add dictionary to list
        underpaid_employee = {} #redeclare empty dictionary to start over with next underpaid employee
        
print("\n")
print("*****Underpaid Employees*****")
pprint.pprint(underpaid_salaries)

#6 calculating raises
company_raises = [] #new company raises list
raises = {} #dictionary for each employee

for i in listdict:
    if i["Hourly Wage"] > 22 and i["Hourly Wage"] < 24:
        raise_ = i["Hourly Wage"] * 0.05 #calculate raise amount
        newwage = i["Hourly Wage"] + raise_ #add raise to hourly wage
        raises.update({"Full Name":i["Full Name"]}) #add to raises dictionary
        raises.update({"Raise":round(raise_, 2)}) #add to raises dictionary
        raises.update({"New Hourly Wage":round(newwage, 2)}) #add to raises dictionary
        company_raises.append(raises) #add dictionary to company raises list
        
    elif i["Hourly Wage"] > 24 and i["Hourly Wage"] < 26:
        raise_ = i["Hourly Wage"] * 0.04
        newwage = i["Hourly Wage"] + raise_
        raises.update({"Full Name":i["Full Name"]})
        raises.update({"Raise":round(raise_, 2)})
        raises.update({"New Hourly Wage":round(newwage, 2)})
        company_raises.append(raises)
        
    elif i["Hourly Wage"] > 26 and i["Hourly Wage"] < 28:
        raise_ = i["Hourly Wage"] * 0.03
        newwage = i["Hourly Wage"] + raise_
        raises.update({"Full Name":i["Full Name"]})
        raises.update({"Raise":round(raise_, 2)})
        raises.update({"New Hourly Wage":round(newwage, 2)})
        company_raises.append(raises)
        
    else:
        raise_ = i["Hourly Wage"] * 0.02
        newwage = i["Hourly Wage"] + raise_
        raises.update({"Full Name":i["Full Name"]})
        raises.update({"Raise":round(raise_, 2)})
        raises.update({"New Hourly Wage":round(newwage, 2)})
        company_raises.append(raises)
        
    raises = {} #declare empty dictionary to start over with each employee each loop

print("\n")
print("*****Raises*****")
pprint.pprint(company_raises)
