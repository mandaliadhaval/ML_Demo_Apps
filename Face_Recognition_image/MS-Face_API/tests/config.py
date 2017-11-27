# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:22:01 2017

@author: dhavalma
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: config.sample.py
Description: unittest configuration for Python SDK of the Cognitive Face API.
- Copy `config.sample.py` to `config.py`.
- Assign the `KEY` with a valid Subscription Key.
"""

# Subscription Key for calling the Cognitive Face API.
KEY = 'efb47541d86b4786a87d8d495aa84b95'

# Base URL for calling the Cognitive Face API.
# default is 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'

# Time (in seconds) for sleep between each call to avoid exceeding quota.
# Default to 3 as free subscription have limit of 20 calls per minute.
TIME_SLEEP = 3