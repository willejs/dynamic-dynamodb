# -*- coding: utf-8 -*-
""" DynamicDynamoDBDaemon implementation

APACHE LICENSE 2.0
Copyright 2013 Sebastian Dahlgren

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from daemon import Daemon
from dynamic_dynamodb import DynamicDynamoDB


class DynamicDynamoDBDaemon(Daemon):
    """ Daemon class """
    def run(self, *args, **kwargs):
        """ Run the daemon """
        dynamic_dynamodb = DynamicDynamoDB(*args, **kwargs)
        dynamic_dynamodb.run()