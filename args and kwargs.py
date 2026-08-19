# def final_cart_amount(*args,discount = .5):
#     result = 0
#     for amount in args:
#         result += amount
#     Final_amount = result - (result*discount)
#     return Final_amount
#
#
#
#
# cart_value = final_cart_amount(1,2,3,4,5,6,7,8,9)
# print(cart_value)

#
# def sum(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# Final_sum = sum(1,2,3,4,5)
# print(Final_sum)


#
# def log_extract (**logging):
#     for key,value in logging.items():
#         with open("employees.txt", "a") as file:
#             file.write(f"{key}: {value}\n")
#         print("File created and record written successfully!")

def log_extract(**kwargs):
    # Convert all key-value pairs into a single string separated by commas
    # Example: "status: SUCCESS, message: Data loaded successfully"
    log_line = ", ".join([f"{key}: {value}" for key, value in kwargs.items()])

    with open("execution_logs.txt", "a") as file:
        file.write(log_line + "\n")

    print("Log record written successfully!")


# Test it out
log_extract(status="SUCCESS", message="Data loaded successfully", user="Admin")


Logging = log_extract( status =  "SUCCESS", message =  "Data loaded successfully", error =  "Data failed")


keep this for later