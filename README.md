### packtpub_checker

I proudly present packtpub_checker script, which can be used to set as a windows scheduled task
to scrap packtpub.com free learning offers page in order to send its content about free book by email.

## Usage

Application usage:

```python check_packt.py [-u url_to_packtpub_free_offer] [-s sender] [-r recipient_1] [-r recipient_2] ...```

If any of those optional arguments is missing, script tries to derive any missing parameters from config.py file.

## Schedule as a windows task

As an example, in order to schedule the task to run daily at 15:00, you need to run the following command in cmd with administrator privileges.

```schtasks /create /sc DAILY /tn packtpub_checker /tr "dir:\path\to\python\python.exe dir:\path\to\app\check_packt.py [script_parameters]" /st 15:00```

In order to check the usage of schtasks, go [there](https://technet.microsoft.com/en-us/library/cc725744.aspx)