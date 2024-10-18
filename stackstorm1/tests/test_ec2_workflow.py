import unittest
from actions.launch_large_ec2 import LaunchLargeEC2

class TestEC2Workflow(unittest.TestCase):
    def test_launch_large_ec2(self):
        action = LaunchLargeEC2()
        result = action.run(image_id="ami-12345", instance_type="t2.large")
        self.assertTrue(result)
