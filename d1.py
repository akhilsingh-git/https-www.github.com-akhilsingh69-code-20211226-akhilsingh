import csv

class Body_Mass_Index:
    bmi_category ={ 'UW' :'Underweight',
                    'NW': 'Normal Weight',
                    'OW': 'Over Weight',
                    'MO': 'Moderately obese',
                    'SO': 'Severly obese',
                    'VSO': 'Very Severly obese',
                   }

    health_risk = {
                    'MR':'Malnutrition Risk',
                    'LR': 'Low Risk',
                    'ER': 'Enhanced Risk',
                    'MRS': 'Medium Risk',
                    'HR': 'High Risk',
                    'VHR': 'Very High Risk',
    }


def reader_contents():
    list_of_line = []
    with open('weight-height.csv') as file:
        alllines = csv.reader(file)
        for line in alllines:
            list_of_line.append(line)
        return list_of_line


def finalizedata_with_bmi(alldata):
    line_count = 0
    notValidData = []
    validData = []
    for line in alldata:
        if line_count == 0:
            line_count = 1
        elif line[0].isalpha() == True and line[1].isnumeric() == True and line[2].isnumeric() == True :
            bmi = calculate_bmi(line)
            validData.append(line+bmi)
            line_count +=1
        else:
            notValidData.append(line)
            line_count +=1
    
    return validData


def calculate_bmi(data):
    BMI_category= None
    Health_risk= None
    BMI_range = None
    x =int(data[1])
    y = int(data[2])
    bmi = y/((x/100)**2)
    if bmi <= 18.4 :
        BMI_category = Body_Mass_Index.bmi_category.get('UW')
        BMI_range = bmi
        Health_risk = Body_Mass_Index.health_risk.get('MR')
    elif bmi >=18.5 and bmi <= 24.9:
        BMI_category = Body_Mass_Index.bmi_category.get('NW')
        BMI_range = bmi
        Health_risk = Body_Mass_Index.health_risk.get('LR')
    elif bmi >=25 and bmi <= 29.9:
        BMI_category = Body_Mass_Index.bmi_category.get("OW")
        BMI_range = bmi
        Health_risk = Body_Mass_Index.health_risk.get('ER')
    elif bmi >=30 and bmi <= 34.9:
        BMI_category = Body_Mass_Index.bmi_category.get("MO")
        BMI_range = bmi
        Health_risk = Body_Mass_Index.health_risk.get('MRS')
    elif bmi >= 35 and bmi <= 39.9:
        BMI_category = Body_Mass_Index.bmi_category.get("SO")
        BMI_range = bmi
        Health_risk = Body_Mass_Index.health_risk.get('HR')
    elif bmi > 40:
        BMI_category = Body_Mass_Index.bmi_category.get("VSO")
        BMI_range = bmi
        Health_risk = Body_Mass_Index.health_risk.get('VHR')
    bmi_list =[BMI_category,BMI_range,Health_risk]
    return bmi_list


def writing_csv(data):
    with open('OutputBMI.csv', 'w',newline='') as file:
        csv_data = csv.writer(file, delimiter=',')
        csv_data.writerow(['Gender', 'Height', 'Weight', 'BMI_category', 'BMI_range', 'Health_risk'])
        for line in data:
            # printing(line)
            csv_data.writerows([line])
    return 'CSV File is added as OutputBMI.CSV'


if __name__ == '__main__':
    contents = reader_contents()
    # printing the (result)
    final_data = finalizedata_with_bmi(contents)
    # print('finish data with BMI-->',finaldata)
    result = writing_csv(final_data)
    print(result)
