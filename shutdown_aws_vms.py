#!/usr/bin/env python

# Created on 2017-10-14
# 
# @author: Mostafa Mostafa
# @copyright: This is a community script, anyone can use it.
# @version: 1.0.0
# 
# PRE-REQUISTES:
#    To run the script, you need to install pexpect and AWS-cli, just type:
#        - pip install pexpect
#        - pip install --upgrade --user awscli
#
#    This script is tested on Linux and MAC OS, but not on windows.
#
# USAGE: 
#     python import_ami_to_ec2.py
#     CLI argument to run the script is:
#        - python shutdown_aws_vms.py <access_key> <secret_key> <region_name> <stop/start>
#        - For example: 
#          python shutdown_aws_vms.py AKIAIBCC77SSX6P2U4BQ oJd211dwswuJgs8KIHd7j211dws+211dws+2v6rs us-west-2 stop
#          python shutdown_aws_vms.py AKIAIBCC77SSX6P2U4BQ oJd211dwswuJgs8KIHd7j211dws+211dws+2v6rs us-west-2 start
#
# Script Summary:
#     This script starts or stops the instances in a certain region
#
# Script Details:
#     1) Verifies AWS is installed on the running machine
#     2) Configures aws configure command
#     3) stop or start the instances
#

############################################# 
# Import required libraries
############################################# 
import pexpect, os, sys, time, argparse


############################################# 
# Start script
############################################# 
### start main function
def main():
    # add cli options (email, github, interval) 
    parser = argparse.ArgumentParser()
    parser.add_argument("access_key", default="", type=str,
                        help="Enter your AWS Access Key")
    parser.add_argument("secret_key", default="", type=str,
                        help="Enter your AWS Secret Key")
    parser.add_argument("region_name", default="us-west-2", type=str,
                        help="Enter your AWS S3 Region")
    parser.add_argument("stop_start", default="", type=str,
                        help="Enter start or stop")
    args = parser.parse_args()
    #print(args)

    #save cli variables
    access_key = args.access_key                   
    secret_key = args.secret_key
    region_name = args.region_name
    stop_start = args.stop_start

    # check aws is installed correctly 
    print '1) Verify AWS installation'
    try:
        output = pexpect.run('aws --version')
        if not "aws-cli" in output:
            print 'ERROR: AWS is not installed in this machine. Please install AWS-CLI.'
            print '      For information regarding this procedure, refer to the current AWS official documentation at: '
            print '      http://docs.aws.amazon.com/cli/latest/userguide/installing.html#install-bundle-other-os'
            sys.exit()
    except:
        sys.exit()

    #check if enviroment variables are set correctly
    if not "LC_ALL" in os.environ:
        os.environ["LC_ALL"] = "en_US.UTF-8"
        #os.environ["LC_CTYPE"] = "UTF-8"
        #os.environ["LANG"] = "en_US"
  
    print '2) Configure AWS CLI by execute aws configure'
    child = pexpect.spawn ('aws configure')
    #child.interact()
    child.expect ('AWS Access Key ID')
    child.sendline ('%s' % access_key)
    child.expect ('AWS Secret Access Key')
    child.sendline ('%s' % secret_key)
    child.expect ('Default region name')
    child.sendline ('%s' % region_name)
    child.expect ('Default output format')
    child.sendline ('json')
    child.expect (pexpect.EOF)
    #print child.before, child.after
    
    if "stop" == stop_start:
        print '3) Stop instances'
        cmd = """aws ec2 describe-instances --region us-west-2 --filter Name=instance-state-name,Values=running --query 'Reservations[].Instances[].InstanceId' --output text"""
        output = pexpect.run('%s ' % cmd)
        print output
        os.system('%s | xargs aws ec2 stop-instances --region us-west-2 --instance-ids' % cmd)
        #sys.exit()

    if "start" == stop_start:
        print '3) Start instances'
        cmd = """aws ec2 describe-instances --region us-west-2 --filter Name=instance-state-name,Values=stopped --query 'Reservations[].Instances[].InstanceId' --output text"""
        output = pexpect.run('%s ' % cmd)
        print output
        os.system('%s | xargs aws ec2 start-instances --region us-west-2 --instance-ids' % cmd)
        #sys.exit()
        
    
    print '***********************************************************'
    print '***                   Script complete                   ***'
    print '***********************************************************'


if __name__ == "__main__":
   main()
