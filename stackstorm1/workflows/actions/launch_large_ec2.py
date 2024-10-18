from st2common.runners.base_action import Action
import boto3

class LaunchLargeEC2(Action):
    def run(self, image_id, key_name, security_group_ids, subnet_id):
        ec2_client = boto3.client('ec2')

        response = ec2_client.run_instances(
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1,
            ImageId=image_id,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            SubnetId=subnet_id,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'Large-EC2-Replacement'}]
            }]
        )
        return response['Instances'][0]['InstanceId']
