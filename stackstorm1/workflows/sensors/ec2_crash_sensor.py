from st2reactor.sensor.base import PollingSensor
import boto3

class EC2CrashSensor(PollingSensor):
    def setup(self):
        self.client = boto3.client('cloudwatch')

    def poll(self):
        alarms = self.client.describe_alarms(
            AlarmNames=['Your-EC2-Crash-Alarm']
        )
        for alarm in alarms['MetricAlarms']:
            if alarm['StateValue'] == 'ALARM':
                self._dispatch_trigger(
                    trigger="aws.ec2.crash",
                    payload={
                        'instance_id': alarm['Dimensions'][0]['Value'],
                        'state': alarm['StateValue']
                    }
                )
    
    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
