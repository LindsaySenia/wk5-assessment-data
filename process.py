log_file = open("um-server-01.txt")
# This is opening the txt file within the python file so the code we write can access the data storted here, like it would with a csv file. It also sets the txt file equal to a variable (log_file) so it can be called upon or passed into functions


def sales_reports(log_file):
# # This is creating a function called sales_report, where a variable is passed in (log_file is just a placeholder here, but indicates we will likely be passing in that txt file).
    for line in log_file:
#     # each line in the file is parsed seperately
        line = line.rstrip()
#         # The whitespace and linebreak is removed from the end of each line
        day = line[0:3]
#         # This creates a variable 'day' which is equal to the 0 index and is 3 letters long?
        if day == "Mon":
#         # If the day is equal to 'Tue'
            print(line)   
#             # Then the line is printed (like console.log in JS)




sales_reports(log_file)
# Invoking the sales_reports function passing in the log_file

# def lotsa_melons(log_file):
#     for line in log_file:
#         line = line.rstrip()
#         quantity = line[2:2]
#         if int(quantity) > 10:
#             print(line)
            
#     lotsa_melons(log_file)