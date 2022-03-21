# 1. AWS EC2 Server Installation (in the AWS management console) 

# Go to Services - EC2
# Click on Launch instance
# Choose Ubuntu Server 18.04 as your OS and click on Select
# Choose the t2.micro instance and click on Next:Configure Instance Details
# Click on Next: Add Storage
# Choose 20GB of storage under Size(GiB)
# Click on Next: Add Tags
# Click on Next: Configure Security Group
# Click on Add Rule
# Select HTTP under Type and Anywhere under Source
# Select SSH, port 22, and own ip 
# For outbound (all)  
# Click on Review and Launch
# Review your settings and click on Launch
# In the pop up window select Create a new key pair and give the key the name aws_key
# Download the key
# Click on Launch instances

# Make sure that you know the server connection details:

# public hostname/ ip-address
# server username (ubuntu)
# private keyfile (aws_key.pem)


# 2. Metabase installation on EC2 Server (in a terminal window)

# navigate to the folder where your private keyfile is stored: 
cd ~/.ssh

# change the permissions of the keyfile:
chmod 600 ~/.ssh/aws_key.pem

# log into the server via ssh (for authentication question, answer: yes):
ssh -i ~/.shh/aws_key.pem ubuntu@<hostname> 

# update packages
sudo apt-get update -y
sudo apt-get upgrade -y

#download metabase installer
sudo wget https://downloads.metabase.com/v0.42.2/metabase.jar

# install java
sudo apt-get install -y openjdk-11-jre-headless

# update again
sudo apt-get update -y
sudo apt-get upgrade -y

# start metabase server in the background, (no hangup), on port 80 instead of 3000 
sudo nohup java -jar -DMB_JETTY_PORT=80 metabase.jar & 

# If everything worked correctly, 
# you should see some message about 
# nohup: ignoring input and appending output to 'nohup.out' 
# along with the shell job ID (surrounded with brackets) and process ID. 
# At this point you can hit ENTER and let the Metabase program initialize 
# and run in the background.

# metabase should be visibel by typing in the hostname/ip of the ec2-server in the browser