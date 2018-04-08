#Using bash shell.
#!/bin/sh
echo "Spinning an EC2 Instance"
aws ec2 run-instances --image-id ami-d874e0a0 --count 1 --instance-type t2.micro --key-name  --security-group-ids  \
--subnet-id  --region  --user-data file://UserDataScript.txt
