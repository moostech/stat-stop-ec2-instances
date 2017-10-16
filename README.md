Are you board from manually starting and stopping your AWS instances? If your answers is yes, don't worry. Here is a small script that I wrote that will help you overcome this little.

Here is the python script details:
  1. Verifies AWS is installed on the running machine
  2. Configures “aws configure” command to connect to your AWS account
  3. Check the script cli options to see when you want to stop or start your instances

Prepare your environment:
Before you run the script, you should have Python, pexpect, and AWS CLI installed. If pexpect and AWS cli are not installed, just type:

    pip install pexpect
    pip install –upgrade –user awscli

Quick Start
To use the script, type the script name and pass the aws parameters.
Mandatory parameters are:

    access_key                Enter your AWS Access Key (i.e., BKIAIB6QLXA536P2U4BQ)
    secret_key                 Enter your AWS Secret Key (i.e., oJdKhwd204uJgP0+2v96TDV6rs)
    region_name            Enter your AWS S3 Region (i.e., us-west-2)
    stop/start                   Enter start or stop

Note: For AWS root account credentials, you get credentials, such as access keys or key pairs, from the Security Credentials page in the AWS Management Console. For more information, please go to AWS webpage: http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html
Here is an example of how to run it:

    python shutdown_aws_vms.py AKIAIBCC77S4BQ oJd211dwsHd7j211dws+211dws+2v6rs us-west-2 stop
