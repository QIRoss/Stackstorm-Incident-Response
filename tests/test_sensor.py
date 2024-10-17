import unittest
from ec2_crash_sensor import EC2CrashSensor

class TestEC2CrashSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EC2CrashSensor()

    def test_poll(self):
        # Simulate a crash event
        event = {
            'MetricAlarms': [
                {
                    'StateValue': 'ALARM',
                    'Dimensions': [{'Name': 'InstanceId', 'Value': 'i-0123456789abcdef0'}]
                }
            ]
        }

        # Mock the CloudWatch API response
        self.sensor.client.describe_alarms = lambda: event
        
        # Trigger poll and check if sensor dispatches correctly
        self.sensor.poll()
        # Add assertions to check the correct event was dispatched

if __name__ == '__main__':
    unittest.main()
