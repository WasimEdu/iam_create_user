# IAM User Management Script

**Author:** Wasim

## Overview

This script automates the process of creating an IAM user in AWS, generating a random password, creating a policy to allow the user to log in and change their password, and attaching that policy to the user. The script uses the `boto3` library to interact with the AWS IAM service.

<!-- **Author:** Wasim -->

## Prerequisites

- **Python 3**: Make sure you have Python 3 installed on your system.
- **Boto3**: AWS SDK for Python. Install it using `pip install boto3`.
- **AWS Credentials**: Ensure you have AWS credentials configured (e.g., using AWS CLI or environment variables) with sufficient permissions to create IAM users and policies.

## How It Works

1. **Initialize AWS Session**: Connects to AWS IAM using the default profile.
2. **Generate Random Password**: Prompts for the length of the password and generates a random password using letters, digits, and punctuation.
3. **Create IAM User**: Creates an IAM user with the provided username and generated password.
4. **Create Policy**: Defines and creates a policy that allows the new user to create other users, create login profiles, and change passwords.
5. **Attach Policy**: Attaches the created policy to the newly created user and also attaching policy to give full access to EC2 instance (You can use anything).

## Usage

1. **Setup AWS Credentials**:
   Ensure that your AWS credentials are set up. You can configure them using the AWS CLI:
   ```sh
   aws configure
