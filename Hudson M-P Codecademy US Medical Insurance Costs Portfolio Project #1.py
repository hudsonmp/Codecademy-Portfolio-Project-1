#%% md
# # U.S. Medical Insurance Costs
#%% md
# # We want to analyze the number of smokers by agre group using the provided data set
# 
#%%
import csv
with open('insurance.csv', 'r') as insurance_data:
    insurance_data_list = []
    insurance_data = csv.reader(insurance_data)
    for row in insurance_data:
        insurance_data_list.append(row)
# Creates a nested list of each of the rows and appends them to the insurance_data_list
print(insurance_data_list)

#%%
insurance_data_keys = insurance_data_list[0]
print(insurance_data_keys)
#Isolate age, smoking, and charges variables to analyze the age group that smokes the most and how much their average insurance cost is
#%% md
# ### There seems to be a problem with the below code due to the way that the nested lists aren't seperated. Fix tomorrow!
#%%
new_keys = [insurance_data_list[0][0], insurance_data_list[0][4],insurance_data_list[0][6]]
print(new_keys)
new_values = []
##### I had to use ChatGPT to review the format of doing this, because I used if statements which yielded nested strings that weren't seperated by ','s
for sublist in insurance_data_list[1:]:
    values = [sublist[0], sublist[4], sublist[-1]]
    new_values.append(values)
print(new_values)
#%%

def convert_to_number_data():
    for value in new_values:
        if value[1] == 'yes':
            value[1] = 1
        elif value[1] == 'no':
            value[1] = 0
        else:
            pass
    return new_values
convert_to_number_data()
print(new_values)

        

#%%
## Use a for loop to cycle through index values of the keys and then use that to make dictionaries from each new list of values.
int_list = [float(i) for value in new_values for i in value]
nested_int_list = [int_list[i : i +3] for i in range(0, len(int_list), 3)]
print(nested_int_list)
new_dict = {key: [] for key in new_keys}
### Used the assistance of ChatGPT 
for sublist in nested_int_list:
    for index in range(len(new_keys)):
        new_dict[new_keys[index]].append(sublist[index])
        ### Used the assistance of ChatGPT 
print(new_dict)

#%% md
# Now that I have my data organized into a dictionary, I'm able to analyze the data and look at some investigative questions. First, I'd like to find the average and the total number of smokers.
#%% md
# 
#%%
def average_age_finder(list):
    total_age = sum(nested_int_list[i][0] for i in range(len(nested_int_list)))
    average_age = total_age / len(nested_int_list)
    return round(average_age, 2)
print("The average age in this dataset is {} years old.".format(average_age_finder(nested_int_list)))



            

#%%
def age_group_and_cost(list):
    sorted_keys = [i for i in range(10, 70, 10)]
    sorted_age_dictionary = {key: [] for key in sorted_keys}
    for slist in nested_int_list:
            if 10 <= slist[0] < 20:
                sorted_age_dictionary[sorted_keys[0]].append(slist[0])
            if 20 <= slist[0] < 30:
                sorted_age_dictionary[sorted_keys[1]].append(slist[0])
            if 30 <= slist[0] < 40:
                sorted_age_dictionary[sorted_keys[2]].append(slist[0])
            if 40 <= slist[0] < 50:
                sorted_age_dictionary[sorted_keys[3]].append(slist[0])
            if 50 <= slist[0] < 60:
                sorted_age_dictionary[sorted_keys[4]].append(slist[0])
            if 60 <= slist[0] < 70:
                sorted_age_dictionary[sorted_keys[5]].append(slist[0])
    return(sorted_age_dictionary)
sorted_age_dictionary = age_group_and_cost(nested_int_list)

### I'd like to count the number of people in each age group, and perhaps redo the dictionary so that it includes smoking and total cost information.
def count_ages(sorted_age_dictionary):
    for i in range(10,70, 10):
        print('The {}\'s age group has {} people'.format(i, len(sorted_age_dictionary[i])))
number_of_ages = count_ages(sorted_age_dictionary)
length = 0
length_dict = {}
for i in range(10,70, 10):
    if len(sorted_age_dictionary[i]) > length:
        length = len(sorted_age_dictionary[i])
        length_dict[length] = i
        
    else:
        pass
print("The age group that has the greatest number of people is the {}\'s age group. They have {} people in this data set".format(length_dict[length] ,length))



with open('protfolio Medical Project Codecademy.rtf', 'w') as blank_doc:
    blank_doc.write('We\'ve determined that the 20\'s age group has the highest number of people in this data set.\n')
    blank_doc.write('We\'ve determined that the average age in this data set is roughly 39 years old.')
print(age_group_and_cost(nested_int_list))

#%%

#%%
