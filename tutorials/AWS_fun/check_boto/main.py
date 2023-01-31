import json
import logging
import os

import boto3

from functools import wraps
from pprint import pprint

from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)


def draw_line(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print()
        print("-"*50, f.__name__, "-" * 50)
        return f(*args, **kwargs)
    return wrapper

def check_s3_content():
    client = boto3.client("s3")

    bucket = os.getenv('MY_TMP_BUCKET')
    response = client.list_objects(Bucket=bucket)
    for element in response["Contents"]:
        print(element["Key"], element["ETag"])

def create_user(iam_client, new_user_name):
    resp = iam_client.create_user(
        UserName=new_user_name
    )
    # pprint(resp)

def get_users(iam_client):
    users = []
    paginator = iam_client.get_paginator('list_users')
    for resp in paginator.paginate():
        for user in resp['Users']:
            users.append(user['UserName'])
    return users

@draw_line
def check_iam_users(iam_client):
    new_user_name = 'New_tmp_user_123'
    updated_user_name = 'Updated_tmp_user_123'

    users = get_users(iam_client)

    for user in users:
        if user == new_user_name or user == updated_user_name:
            iam_client.delete_user(
                UserName=user
            )

    create_user(iam_client, new_user_name)
    print('1', get_users(iam_client))
    iam_client.update_user(
        UserName=new_user_name,
        NewUserName=updated_user_name
    )
    print('2', get_users(iam_client))
    iam_client.delete_user(
        UserName=updated_user_name
    )
    print('3', get_users(iam_client))

@draw_line
def check_policies(iam_client, user):
    resp = iam_client.list_policies(
        Scope="Local"
    )

    s3_put_policy_arn = ''
    for i, policy in enumerate(resp['Policies']):
        print(f"{i:<5}:: ", policy['PolicyName'], policy['Path'], policy['PolicyId'])
        if 'putObjectS3' in policy['Arn']:
            s3_put_policy_arn = policy['Arn']
    print("\n\n\n")
    resp = iam_client.get_policy(
        PolicyArn=s3_put_policy_arn
    )
    pprint(resp["Policy"])

    iam = boto3.resource('iam')
    policy_resource = iam.Policy(s3_put_policy_arn)
    print(policy_resource)
    print(list(policy_resource.attached_groups.all()))
    print(list(policy_resource.attached_roles.all()))
    print(list(policy_resource.attached_users.all()))



    paginator = iam_client.get_paginator('list_user_policies')
    for resp in paginator.paginate(UserName=user):
        for policy in resp["PolicyNames"]:
            print(policy)

    user_as_resource = iam.User(user)
    subresources = user_as_resource.get_available_subresources()
    print("check user resources")

    pprint(f"{list(user_as_resource.attached_policies.all())}")
    pprint(f"{list(user_as_resource.groups.all())}")
    pprint(f"{list(user_as_resource.mfa_devices.all())}")
    pprint(f"{list(user_as_resource.policies.all())}")
    pprint(f"{list(user_as_resource.signing_certificates.all())}")
    pprint(f"{list(user_as_resource.access_keys.all())}")

    for policy in user_as_resource.policies.all():
        print(policy. policy.arn)

def check_iam(user:str):
    client = boto3.client('iam')

    check_iam_users(client)

    check_policies(client, user)

def main() -> None:
    print(f'Hello main from : {__file__}')
    load_dotenv()
    user_var_name = 'AWS_USER'
    user = os.getenv(user_var_name)
    if user is not None:
        check_iam(user=user)
    else:
        logging.warning(f"No env var {user_var_name} defined in env.")

if __name__ == '__main__':
    main()