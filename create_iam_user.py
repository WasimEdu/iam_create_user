# Created by:- Wasim

# Importing required modules
import boto3
import random
import string


# loging to aws console to IAM user console
aws_console = boto3.session.Session(profile_name = "default")
iam_console = aws_console.client("iam")


# generating random password
length = int(input("Enter the length: "))
chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

pwd = "".join([random.choice(chars) for i in range(length)])


def create_iam_user(name, pwd):
    try:
      
      # creating user
       response = iam_console.create_user(
           UserName= name,    
       )

      # creating loging profile aka: password
       login_create = iam_console.create_login_profile(
            UserName=name,
            Password=pwd,
            PasswordResetRequired=True, #Forcing to change password when loging for first time
        )
       

       user = response['User']

      # printing needed outputs
       print("User have been Created! \n")
       print("UserName:- " , user['UserName'])
       print("UserId:- ", user['UserId'])
       print("Password is:- ", pwd)  #this will print the password as well but don't use it for security 
       print("UserARN:- ", user['Arn'])

    except iam_console.exceptions.EntityAlreadyExistsException:
       print(f"user {name} already exists")

    except Exception as e:
       print(f"Error creating user: {e}")


# creating policy [So new user can loging and change password]
def create_policy(policy_name, policy_document):
    try:   

        create_policy = iam_console.create_policy(
            PolicyName = policy_name,
            PolicyDocument = policy_document,
        )

        arn = create_policy['Policy']

        print("Policy arn:- ", arn['Arn'])

    except Exception as e:
        print(f"Error creating policy: {e}")


# Attaching the policy we created to user 
def attach_policy(name, policy_arn):
    
    # loolping because in this script we attaching 2 policies
    for policy_arn in policy_arn:
    
      try: 

          attach_policy = iam_console.attach_user_policy(
              UserName=name,
              PolicyArn=policy_arn,
              
          )
      except Exception as e:
          print(f"Error creating policy: {e}")


# the policy name 
policy_name = 'IAMUserManagementPolicy'

# policy json code
policy_document = '''{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateUser",
        "iam:CreateLoginProfile",
        "iam:ChangePassword"
      ],
      "Resource": "*"
    }
  ]
}'''

# asking for user name 
name = input("Enter User Name: ")

create_iam_user(name, pwd)

# use the policy maker only for one time after once policy is created just ATTACH it with any user using ARN mention down
# if u make this everytime will show error [comment it out] 
policy_arn = create_policy(policy_name, policy_document)

# for IAMUserManagementPolicy don't create everytime use as shown down after created once 
# 2 polies 2nd one provieds full access to EC2 instance
policy_arn = [ # multiple policies
    'arn:aws:iam::864981749658:policy/IAMUserManagementPolicy', # This is the policy we creating above use this everytime after created once
    'arn:aws:iam::aws:policy/AmazonEC2FullAccess', #{EC2 Instance permission}  A policy which exist in aws [just attaching it]
]

attach_policy(name, policy_arn)


