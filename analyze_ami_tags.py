#!/usr/bin/env python3
import boto3
import sys
import pprint

''' TODO:
- Pass in values for region and use both us-west-2 and us-east-1 by default, ami image owners
- Test this using awscli-saml
- Determine the best output format for reporting the information -> csv, json?
- Add robust error handling
'''

def valid_tags(tags_dict):
  # returns a tuple -> boolean (true = pass), list of tuples (tags that fail criteria -e.g. don't exist, bad info)
  result = False
  bad_tags_list = [('lob','does not exist')]

  ## Needs to iterate through the required tags, and criteria to populate the return tuple
  # e.g. for tag,val in required_tags: eval each one, populate bad_tags_list, and flip result to False if needed

  return  result, bad_tags_list


def main():
  ec2 = boto3.resource('ec2') # can call this with a specific region e.g. boto3.resource('ec2', region_name='us-west-2')
  client = boto3.client('ec2')
  # can set Owners as a list of ids, to only return those AMIs
  #response = client.describe_images(Owners=['782511650046', '057670693668'])
  response = client.describe_images(Owners=['self'])
  images =  response['Images']
  amis = []

  #pprint.pprint(images)

  for image in images:
    ami = {'ImageId': image['ImageId'],
           'OwnerId': image['OwnerId'],
           'Tags': image['Tags'],
           'Name': image['Name']
          } 
    amis.append(ami)

  pprint.pprint(amis)

  print(valid_tags(amis[0]))


if __name__ == "__main__":
  main()
