# # Q1. Swap the case of the string without using swapcase
# # inbuilt method for string
#
# # Input:- Programming Aasan Hai
# # Output:- pROGRAMMING aASAN hAI
#
# # sentence = "Programming Aasan Hai"
# # output = ""   # empty string
# # for letter in sentence:
# #     if letter == letter.lower():
# #         output = output + letter.upper()
# #     else:
# #         output= output + letter.lower()
# #
# # print(output)
#
#
# # Q2. Print the list of all unique ip addresses?
# #
# # Input = [
# # "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
# # "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
# # "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
# # "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
# # "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
# # "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
# # "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
# # "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
# # ]
# # #
# # # Output:- ["10.168.155.2","10.168.156.2","10.168.151.2"
# # #            "10.168.155.22","10.168.167.2",
# # #            "10.168.179.28","10.168.155.31" ]
# # unique_ips = []
# # for char in Input:
# #    after_split = char.split("server/")[1]
# #    last_split = after_split.split("/")
# #    unique_ips.append(last_split[0])
# # print(list(set(unique_ips)))
#
#
# email = "manushukla@gmail.com"
# ph = "935447898"
# # encrypted_email =""
# # encrypted_ph = ""
# # new_email = str(email).split("@")[0]
# # domain = str(email).split("@")[1]
# #
# # if len(new_email)>0 and len(domain)>0:
# #     for i in range(len(new_email)):
# #         if i == 0 :
# #             encrypted_email = new_email[i]
# #         elif i < (len(new_email)-2):
# #             encrypted_email += new_email[i].replace(new_email[i],"*")
# #         else:
# #             encrypted_email += new_email[i]
# # else :
# #     encrypted_email = new_email
# # print (f"{encrypted_email}@{domain}")
#
# encrypted_ph = (ph[0]+ '*' * (len(ph)-2) + ph[-2:])
# print(encrypted_ph)
# new_email = email.split('@')[0]
# encrypted_mail = (email[0] + '*' * (len(new_email)-3) + new_email[-2:])
# print(encrypted_mail)

