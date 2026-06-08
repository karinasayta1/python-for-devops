import boto3

def list_ec2_instances():
    try:
        ec2 = boto3.client("ec2", region_name= "us-east-1")
        instance_details=[]
        response = ec2.describe_instances()
        if response['Reservations']==[]:
                print("No EC2 instances found.")
                return []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                #print(f"ID : {instance['InstanceId']}\tStatus : {instance['State']['Name']}")
                instance_details.append({
                    "InstanceId": instance['InstanceId'],
                    "State": instance['State']['Name']
                })
        return instance_details

    except Exception as e:
        print(f"Error fetching EC2 instances: {e}")
        return []
    

