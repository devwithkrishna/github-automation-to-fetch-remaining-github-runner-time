# github-automation-to-fetch-remaining-github-runne-time
An automation to pull github free runner time remaining for my account and mail it to admins weekly

## Reference
[get-github-actions-billing-for-an-organization](https://docs.github.com/en/rest/billing/billing?apiVersion=2022-11-28#get-github-actions-billing-for-an-organization)

# What does this repo do

```
This repo uses github rest api to pull billing details for github org and user account. this iswritten to json files.
Later these json files are dropped as an email using sendgrid to ownerof account. Email consists of multiple json atachments
```

# Credentials used for authorization

| credential                         | purpose                                                                | check              |
|------------------------------------|------------------------------------------------------------------------|--------------------|
| fine grained personal access token | this is used for all purpose like listing repos, github app detailsetc | :heavy_check_mark: |
| sendgrid api key | this is used for amiling purpose to auth with sendgrid | :heavy_check_mark: |


# SendGrid 

```
SendGrid is a cloud-based service that provides email delivery and management for businesses. Sendgrid is used to send email
using its python SDK - sendgrids
```

# parameters 

| input name      | type | description                                            | required |
|-----------------|------|--------------------------------------------------------|----------|
| organization    | string | Github organizarion name. Default - `devwithkrishna`   | :heavy_check_mark: |
| account_name    | string | GitHub account name. Default - `githubofkrishnadhas`   | :heavy_check_mark: |

# Files
* send_email.py --> sends a single file attachment with email
* send_email_using_sendgrid.py --> sends multiple json files in a single email.
* github_billing.py --> this will pull billing details using github rest api
* email_template.html --> email html template