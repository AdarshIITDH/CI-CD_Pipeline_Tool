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

