# importing modules
import boto3

# open aws console
aws_console = boto3.session.Session(profile_name = "default")

# open iam console as client
iam_console = aws_console.client('iam')

# saving response
response = iam_console.list_users()

# printing users name 
# Reffer to this documentation to learn more https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_users.html

for users in response['Users']:
    print(users['UserName'])