# geiger-counter
Small script for measuring dose rate in microsievert per hour with RadiationD-v1.1(CAJOE)

This script works with tinkerboard after installing and loading the relevant GPIO library from ASUS support

It will also work with raspberry pi if you load the raspberry pi GPIO library

It uses prometheus so you will also need to setup a prometheus server localy, more information can be found in https://prometheus.io/. After you install prometheus you will need to create a prometheus.yml configuration file to configure the server. You may find the prometheus.yml provided here helpful

Finally you need to create a grafana account and use the grafana_configuration.json to create the graphs shown bellow

![Alt text](https://github.com/sedzinfo/geiger-counter/blob/main/grafana.png)
