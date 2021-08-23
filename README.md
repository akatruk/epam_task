[![Build Status](https://github.com/cloud-bulldozer/kube-burner/workflows/Go/badge.svg?branch=master)](https://github.com/cloud-bulldozer/kube-burner/actions?query=workflow%3AGo)
[![Go Report Card](https://goreportcard.com/badge/github.com/cloud-bulldozer/kube-burner)](https://goreportcard.com/report/github.com/cloud-bulldozer/kube-burner)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

API https://covidtracker.bsg.ox.ac.uk/about-api 
    https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2020-01-01/2020-05-01

show_result.py
read from API -> insert to file -> load to database PostgreSQL -> run Flask with selected table 'scripts/increment_data_load.sql'

test_show_result.py
unittest: check to database PostgreSQL connectivity

docker build -f dockerfile -t show_result .
docker run -d -p 80:80 errbx/epum_task004:latest --name idle --network="host"

