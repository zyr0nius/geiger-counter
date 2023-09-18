# geiger-counter
Small script for measuring dose rate in microsievert per hour with RadiationD-v1.1(CAJOE)

This script works with tinkerboard after installing and loading the relevant GPIO library https://tinker-board.asus.com/doc_tb.html#gpio

It will also work with raspberry pi if you load the raspberry pi GPIO library

It uses prometheus so you will also need to setup a prometheus server localy, more information can be found in https://prometheus.io/. After installing prometheus you will need to edit the prometheus.yml configuration file to configure the server. You may find the prometheus.yml provided here helpful

using the command crontab -e the prometheus server loads on startup automatically, just copy and paste the command bellow after substituding the prometheus directory with the directory you installed prometheus

```
@reboot sudo /home/linaro/prometheus-2.45.0.linux-armv7/prometheus --config.file=/home/linaro/prometheus-2.45.0.linux-armv7/prometheus.yml --storage.tsdb.retention.time=5y &
```

Finally you need to create a grafana account and use the grafana_configuration.json to create the graphs shown bellow

![Alt text](https://github.com/sedzinfo/geiger-counter/blob/main/grafana.png)
