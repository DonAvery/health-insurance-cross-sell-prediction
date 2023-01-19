#!/usr/bin/env python
# coding: utf-8

import requests

host = "churn-serving-env.eba-m6viypea.us-east-1.elasticbeanstalk.com"
url = f'http://{host}/predict'

customer_id = 'xyz-123'
customer = {
  "id": 61311,
  "gender": "male",
  "age": 68,
  "driving_license": 1,
  "region_code": 28.0,
  "previously_insured": 1,
  "vehicle_age": "1-2 year",
  "vehicle_damage": "no",
  "annual_premium": 32788.0,
  "policy_sales_channel": 26.0,
  "vintage": 31
}

response = requests.post(url, json=customer).json()
print(response)


if response['response'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)
