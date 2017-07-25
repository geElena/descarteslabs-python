#!/usr/bin/env python
# Copyright 2017 Descartes Labs.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import json

import descarteslabs as dl


def notification_handler(args):
    notification = dl.notification

    if args.url:
        notification.url = args.url

    if args.command == 'identify':
        result = notification.identify()
        print(result)

    if args.command == 'notify':

        with open(args.argument) as fp:

            data = json.load(fp)

            notification.notify(data)

            print('notification sent!')
