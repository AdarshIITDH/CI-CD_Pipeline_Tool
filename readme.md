Create a complete CI-CD pipeline using bash, python and crontabs. The list of tasks is specified below: 

# Task 1: Set Up a Simple HTML Project

Create a simple HTML project and push it to a GitHub repository.

```
mkdir CI_CD_Pipeline_Tool && cd CI_CD_Pipeline_Tool
nano index.html
git add .
git commit -m "step-1"
git remote add origin git@github.com:AdarshIITDH/CI-CD_Pipeline_Tool.git
git branch -M main
git push -u origin main 
```
![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/60bd342f-256b-4b3a-9274-7eff28e427bb)

# Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx

Installing the nginx on ubuntu

```
apt update
apt install ngnix
systemctl status ngnix
```

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/a1d2c822-6c09-4c69-bcee-65ff146bad88)

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/487d3563-3b49-4350-bc15-9996046a82c0)

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/399009df-c728-4a40-9ffc-23aa2ea51cae)


# Task 3: Write a Python Script to Check for New Commits

 Create a Python script to check for new commits using the GitHub API.

 Note: Make sure that you dont paste the api token in a file that get pushed to github by any means.

 checkout the check_commits.py for usage of github api
 https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/blob/main/check_commit.py

Store the credientials in credintials.py
https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/blob/main/credentials.py

# Task 4: Write a Bash Script to Deploy the Code

  Create a bash script to clone the latest code and restart Nginx.
  
  https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/blob/main/deploy.sh

Note: Make sure the scripts have executable permission

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/929449ac-1736-4528-92a3-ee010ecb5647)

# Task 5: Set Up a Cron Job to Run the Python Script

Create a cron job to run the Python script at regular intervals.

Method 1

use a bash script in cron job to run the python script that will use the github api for new commit is there is a new commit then copy the desired file in nginx directory.

```
Crontab -e
*/15 * * * *  /path/to/deploy_final.py
```

Method 2

Directly run the python script in the ccron job

```
Crontab -e
*/15 * * * * /usr/bin/python3 /path/to/check_commit.py
```

Note: this make the python script to run in every 15 min

#  Task 6: Test the Setup 

Make a new commit to the GitHub repository and check that the changes are automatically deployed.

Before doing any change in backend nginx page 

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/00b823c8-eaac-463e-a7ff-0f73856adfba)

Made some changes like added a new project4 edited the email, LinkedIn and GitHub URLs

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/53bd4393-c2f3-4251-9ee8-f334bcdd32b9)

```
git status
git add index.html
git commit -m "step6"
git push origin main
```

After 15 min the nginx page automatically changed.

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/f0b40739-4d4b-4cbb-86cd-0e4be41da115)













