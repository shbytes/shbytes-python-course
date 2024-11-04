import csv

# Sample data: list of dictionaries
data = [{"Course": "Data Science","Duration": "6 months","Industry": "Technology"},
{"Course": "Power BI","Duration": "2 months","Industry": "Business Analytics"},
{"Course": "Cloud Computing","Duration": "5 months","Industry": "Cloud Services"}
]

field_names = ["Course", "Duration", "Industry"]
file_name = "output.csv"
# Writing to CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

print("Data written successfully to file", file_name)

print("\n........................................\n")

# [
#     {
#         "id": 1,
#         "name": "John Doe",
#         "age": 28,
#         "city": "New York",
#         "email": "john.doe@example.com",
#         "is_active": true,
#         "hobbies": ["reading", "swimming", "gaming"],
#         "address": {
#             "street": "123 Main St",
#             "zip": "10001"
#         }
#     },
#     {
#         "id": 2,
#         "name": "Anna Smith",
#         "age": 22,
#         "city": "London",
#         "email": "anna.smith@example.com",
#         "is_active": false,
#         "hobbies": ["traveling", "cooking"],
#         "address": {
#             "street": "456 Oak St",
#             "zip": "SW1A 1AA"
#         }
#     },
#     {
#         "id": 3,
#         "name": "Mike Johnson",
#         "age": 32,
#         "city": "San Francisco",
#         "email": "mike.johnson@example.com",
#         "is_active": true,
#         "hobbies": ["cycling", "photography"],
#         "address": {
#             "street": "789 Pine St",
#             "zip": "94103"
#         }
#     }
# ]
