import unittest
from ec2_crash_sensor import EC2CrashSensor

class TestEC2CrashSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EC2CrashSensor()

    def test_poll(self):
        event = {
            'MetricAlarms': [
                {
                    'StateValue': 'ALARM',
                    'Dimensions': [{'Name': 'InstanceId', 'Value': 'i-0123456789abcdef0'}]
                }
            ]
        }

        self.sensor.client.describe_alarms = lambda: event
        
        self.sensor.poll()

if __name__ == '__main__':
    unittest.main()
