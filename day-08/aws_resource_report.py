#connect to your aws account
#list ec2 instance
#list s3 buckets
#saves the ouput in json file
#use classes and functions
#use cli arguments
import boto3
import json
import argparse
import pdb
class AWSResource:
    def __init__(self):
        self.args = self.myArgparser()

    def myArgparser(self):
        analyzer= argparse.ArgumentParser(prog="aws_resource_report.py",description="Fetch AWS resources and generate a report.",
                                    usage="python aws_resource_report.py service-name <ec2/s3> region <us-east-1> --output-file report.json")
        analyzer.add_argument("service_name", help="AWS service name to fetch resources from. (ec2/s3) (Required)")
        analyzer.add_argument("region_name", help="AWS region name. (us-east-1) (Required)")
        analyzer.add_argument("--output_file", help="Path to save the resource report in json format")   
        args=analyzer.parse_args()
        return args

    def getConnection(self):
        try:
            if self.args.service_name == "ec2":
                ec2 = boto3.client(self.args.service_name, region_name= self.args.region_name)
                data=self.list_ec2_instances(ec2)
                self.write_file(data)
                return 
            elif self.args.service_name== "s3":
                s3= boto3.client(self.args.service_name, region_name= self.args.region_name)
                data=self.list_s3_buckets(s3)
                self.write_file(data)
                return 
            else:
                print("Unsupported service. Please use 'ec2' or 's3'.")
                return
        
        except Exception as e:
            print(f"Error connecting to AWS: {e}")
        
    def list_s3_buckets(self,s3):
        try:
            bucket_names = []
            response = s3.list_buckets()
            for bucket in response["Buckets"]:
                bucket_names.append(bucket["Name"])
                print(bucket["Name"])
            return bucket_names
        
        except Exception as e:
            print(f"Error fetching S3 buckets: {e}")
            return []
    
    def list_ec2_instances(self,ec2):
        try:
            instance_details=[]
            response = ec2.describe_instances()
            if response['Reservations']==[]:
                    print("No EC2 instances found.")
                    return []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    print(f"ID : {instance['InstanceId']}\tStatus : {instance['State']['Name']}")
                    instance_details.append({
                        "InstanceId": instance['InstanceId'],
                        "State": instance['State']['Name']
                    })
            return instance_details

        except Exception as e:
            print(f"Error fetching EC2 instances: {e}")
            return []
        
    def write_file(self,data):
        try:
            with open("report.json","w") as f:
                json.dump(data,f,indent=2)
        
        except Exception as e:
            print(f"Error writing to file: {e}")
        
if __name__ == "__main__":
    r1= AWSResource()
    con= r1.getConnection()
    