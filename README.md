# aws-scripts

## aws-ip-parser.py:

Script used to pull information about AWS's IP Ranges per service and region.

### Requirements:
- python3

### Usage:
```
$ ./aws_ip_parser.py -h
usage: aws_ip_parser.py [-h] [-s SERVICE] [-r REGION] [-d]

Script to pull IP info for AWS services

optional arguments:
  -h, --help            show this help message and exit
  -s SERVICE, --service SERVICE
                        The service you want to look up
  -r REGION, --region REGION
                        The region you want to look up
  -d, --display         Dump out available regions and services
$
```

### Example:
```
$ ./aws_ip_parser.py -s EC2_INSTANCE_CONNECT -r us-east-1
18.206.107.24/29
$
```
