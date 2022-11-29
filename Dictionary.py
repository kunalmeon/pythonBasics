#!/usr/bin/env python
# coding: utf-8

# In[ ]:


newEmployInformation={
    'name':"Karan Budha Air",
    "address":"4 Kelvin Road Bedfrod Park",
    "Contact Number":+610415230979,
    'education':['slc','+2','bachelor','masters']
}
for key,value in newEmployInformation.items():
    print(f"the key is:{key} and value is: {value}")
education=newEmployInformation['education']
for educationLevel in education:
    print(educationLevel)
print(f"The name of new Employee is {newEmployInformation['Contact Number']}")

