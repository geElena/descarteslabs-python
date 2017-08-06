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

import os
from .service import Service


class Notification(Service):
    TIMEOUT = (9.5, 360)
    """Notification service"""

    def __init__(self, url=None, token=None, maxsize=10, ttl=600):
        """The parent Service class implements authentication and exponential
        backoff/retry. Override the url parameter to use a different instance
        of the backing service.
        """
        if url is None:
            url = os.environ.get("DESCARTESLABS_NOTIFY_URL",
                                 "https://platform-services-dev.descarteslabs.com/notification/dev")

        Service.__init__(self, url, token)

    def identify(self):
        r = self.session.get('/identify/')
        return r.cookies['sessionid']

    def upload(self, name, data):
        r = self.session.post('/upload/%s/' % name, json=data)
        return r.json()

    def file(self, file_id=None, filename=None, extension=None):
        params = {}
        if file_id:
            params['file_id'] = file_id
        if filename:
            params['filename'] = filename
        if extension:
            params['extension'] = extension
        r = self.session.get('/file/', params=params)
        return r.json()

    def shape(self, shape_id=None, file_id=None):
        params = {}
        if shape_id:
            params['shape_id'] = shape_id
        if file_id:
            params['file_id'] = file_id
        r = self.session.get('/shape/', params=params)
        return r.json()

    def update(self, shape_id, message=None):
        params = {}
        if message:
            params['message'] = message
        r = self.session.get('/update/%s/' % shape_id, params=params)
        return r.json()

    def delete(self, shape_id):
        r = self.session.get('/delete/%s/' % shape_id)
        return r.json()

    def search(self):
        r = self.session.get('/search/')
        return r.json()