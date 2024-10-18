import boto3
from st2common.runners.base_action import Action

class StopEC2Instance(Action):
    def run(self, instance_id):
        ec2_client = boto3.client('ec2')
        ec2_client.stop_instances(InstanceIds=[instance_id])
        return True
