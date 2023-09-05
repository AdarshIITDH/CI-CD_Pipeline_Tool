Create a complete CI-CD pipeline using bash, python and crontabs. The list of tasks is specified below: 

**Task 1: Set Up a Simple HTML Project**

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

**Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx**

Installing the nginx on ubuntu

```
apt update
apt install ngnix
systemctl status ngnix
```

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/a1d2c822-6c09-4c69-bcee-65ff146bad88)

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/487d3563-3b49-4350-bc15-9996046a82c0)

![image](https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool/assets/60352729/399009df-c728-4a40-9ffc-23aa2ea51cae)


** Task 3: Write a Python Script to Check for New Commits**

 Create a Python script to check for new commits using the GitHub API.

 Note: Make sure that you dont paste the api token in a file that get pushed to github by any means.








