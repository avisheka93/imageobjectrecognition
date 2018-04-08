#Using bash shell.
#!/bin/sh
echo "Spinning an EC2 Instance"
aws ec2 run-instances --image-id ami-d874e0a0 --count 1 --instance-type t2.micro --key-name certprep --security-group-ids sg-e44fa39e \
--subnet-id subnet-d0c1628b --region us-west-2 --user-data file://UserDataScript.txt
