# def convert(str1):
#     if str1[:-2] == "AM" and str1[:2]== "12":
#         return str1[:-2]
#     elif str1[:-2] == "PM" and str1[:2]=="24":
#         return str1[:-2]
#     else:
#         return str(int(str1[:2]) + 12) + str1 [2:11]
# print(convert(input("")))







# def convert_time(s):
#     list1=["01","02","03","04","05","06","07","08","09","10","11","12"]
#     list2=[13,14,15,16,17,18,19,20,21,22,23,24]
#     l=s[0:2]
#     m=s[2:10]
#     if "pm" in s:
#             i=0
#             while i<len(list1):
#                 if list1[i]==l:
#                     print(str(list2[i])+m)
#                 i=i+1
#     else:
#         print(s)
# convert_time(input().lower())






