# -*- coding: utf-8 -*-
# Copyright 2015 Alex Woroschilow (alex.woroschilow@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import hexdi

from .service import Finder
from .workspace.settings import SettingsWidget


@hexdi.permanent('plugin.service.disc')
class ServiceFinder(Finder):
    pass


@hexdi.permanent('workspace.disc')
class SettingsWidgetInstance(SettingsWidget):
    pass