from st2common.runners.base_action import Action
import boto3

class TerminateOldEC2(Action):
    def run(self, instance_id):
        ec2_client = boto3.client('ec2')

        response = ec2_client.terminate_instances(
            InstanceIds=[instance_id]
        )
        return response
