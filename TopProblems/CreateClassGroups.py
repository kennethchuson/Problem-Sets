from __future__ import division



n = 30 

possible_to_choose_member_each_group = [] 

for i in range(1, n + 1):
    calc = n / i
    print(calc) 
    if calc - int(calc) == 0:
        possible_to_choose_member_each_group.append(i)

mapping_total_groups = {}

for i in range(len(possible_to_choose_member_each_group)):
    mapping_total_groups[possible_to_choose_member_each_group[i]] = (n / possible_to_choose_member_each_group[i]) 
        
print("total of all members: ", n) 
print("all possible to create number of members in each group: ", possible_to_choose_member_each_group)
print("all possible of total number of groups: ", mapping_total_groups)
