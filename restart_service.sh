#!/bin/bash
sudo systemctl restart rqworker@{1..6}.service
sudo systemctl restart era5_filewatcher.service