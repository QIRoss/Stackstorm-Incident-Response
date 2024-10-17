# Stackstorm Incident Response

Studies based in day 47-48 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 41–50: Reliability Engineering

Day 47–48: Automate incident response using StackStorm for common operational scenarios.

## Project Overview

This repository contains a StackStorm-based workflow to automatically replace a crashed medium EC2 instance with a large EC2 instance. It monitors the instance status using AWS CloudWatch and automates the incident response.

### Project Structure

- **workflows/**: Contains the StackStorm workflow and related scripts.
- **tests/**: Unit tests to validate the actions and sensors.
- **configs/**: Configuration files for StackStorm and AWS.
- **docs/**: Documentation for the workflow, including diagrams.

### Requirements
- StackStorm installed
- AWS CLI configured
- Boto3 Python SDK for AWS
- Python 3.x
- Docker (optional)

### Setup Instructions

1. Install StackStorm: [StackStorm installation guide](https://docs.stackstorm.com/install/index.html)
2. Set up AWS credentials in `configs/aws_config.json`.
3. Configure StackStorm with the provided configuration in `configs/st2_config.yaml`.
4. Deploy the workflow: 

```
st2 run workflows.automate_ec2_replacement
```

## How to Use

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"