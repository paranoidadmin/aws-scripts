#!/usr/bin/env python3
import argparse
import json
import requests

# Globals
url = "https://ip-ranges.amazonaws.com/ip-ranges.json"

#Parse the args
parser = argparse.ArgumentParser(description="Script to pull IP info for AWS \
                                              services")
parser.add_argument("-s", "--service", help="The service you want to look up")
parser.add_argument("-r", "--region", help="The region you want to look up")
parser.add_argument("-d", "--display", action='store_true', \
                     help="Dump out available regions and services")
args = parser.parse_args()
service = args.service
region = args.region
display = args.display

# Grab the data
r = requests.get(url)
j = r.json()
data = j.get('prefixes')

# Build out services dict
Services = []
for each in data:
  ser = each['service']
  if ser not in Services:
    Services.append(ser)
Services.sort()

# Build out regions dict
Regions = []
for each in data:
  reg = each['region']
  if reg not in Regions:
    Regions.append(reg)
Regions.sort()

#Logic for Output
# Display mode:
if display:
  print("The Regions that are available are:")
  for i in Regions:
    print(i)
  print("")
  print("The Services that are available are:")
  for i in Services:
    print(i)
  exit()

# Print ips per service and specific region
if service and region:
  Ips = []
  for i in data:
    if i['service'] == service:
      if i['region'] == region:
        ip = i['ip_prefix']
        Ips.append(ip)
  for ip in Ips:
    print(ip)

# Print ips per service regardless of region.
if service and not region:
  Ips = []
  for i in data:
    if i['service'] == service:
      ip = i['ip_prefix']
      Ips.append(ip)
  for ip in Ips:
    print(ip)
