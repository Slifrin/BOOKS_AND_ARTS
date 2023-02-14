import boto3

from pprint import pprint



def main() -> None:
    print(f'Hello main from : {__file__}')
    sts_client = boto3.client("sts")

    assumed_role = sts_client.assume_role(
        RoleArn="",
        RoleSessionName="AssumeRoleSession1"
    )

    credential = assumed_role["Credentials"]
    pprint(credential)



if __name__ == '__main__':
    main()