# geiger-counter
Small script for measuring dose rate in microsievert per hour with RadiationD-v1.1(CAJOE)

This script works with tinkerboard after installing and loading the relevant GPIO library https://tinker-board.asus.com/doc_tb.html#gpio

```
sudo apt-get update
sudo apt-get install python-dev python3-dev
git clone http://github.com/TinkerBoard/gpio_lib_python.git
cd gpio_lib_python/
sudo python setup.py
sudo python3 setup.py install
```

It will also work with raspberry pi if you load the raspberry pi GPIO library

It uses prometheus so you will also need to setup a prometheus server localy, more information can be found in https://prometheus.io/. After installing prometheus you will need to edit the prometheus.yml configuration file to configure the server. You may find the prometheus.yml provided here helpful

using the command crontab -e the prometheus server loads on startup automatically, just copy and paste the command bellow after substituding the prometheus directory with the directory you installed prometheus

```
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

@reboot sudo /home/linaro/prometheus-2.45.0.linux-armv7/prometheus --config.file=/home/linaro/prometheus-2.45.0.linux-armv7/prometheus.yml --storage.tsdb.retention.time=5y &
```

Finally you need to create a grafana account and use the grafana_configuration.json to create the graphs shown bellow

![Alt text](https://github.com/sedzinfo/geiger-counter/blob/main/grafana.png)
