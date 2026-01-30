"""
Camping Items
Gaven Huynh
Replace Camping Items
n/a
1/29/2026
"""
from Lab3_ghuynh_add import items_list

items_list[4] = "Binoculars"

index_rep = items_list.index("Binoculars")

print ("Before Binoculars:", items_list[:index_rep])
print ("Binoculars:", items_list[index_rep])
print ("After Binoculars:", items_list[index_rep+1:])