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

    kwargs = {}

    if args.url:
        notification.url = args.url

    if args.command == 'identify':
        result = notification.identify()
        print(json.dumps(result))

    if args.command == 'upload':
        with open(args.argument) as fp:
            data = json.load(fp)
            notification.upload(args.argument, data=data)
            print('uploaded!')

    if args.command == 'file':
        if args.file_id:
            kwargs['file_id'] = args.file_id
        if args.filename:
            kwargs['filename'] = args.filename
        if args.extension:
            kwargs['extension'] = args.extension
        result = notification.file(**kwargs)
        print(json.dumps(result))

    if args.command == 'shape':
        if args.file_id:
            kwargs['file_id'] = args.file_id
        if args.shape_id:
            kwargs['shape_id'] = args.shape_id
        result = notification.shape(**kwargs)
        print(json.dumps(result))

    if args.command == 'update':
        if args.message:
            kwargs['message'] = args.message
        notification.update(args.argument, **kwargs)
        print('updated!')

    if args.command == 'delete':
        notification.delete(args.argument)
        print('deleted!')
