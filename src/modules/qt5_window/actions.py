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
import os
import shutil

import inject
from PyQt5 import QtWidgets

from .gui.box import MessageBox
from .singleshot import SingleShot


class ModuleActions(object):
    singleshot = SingleShot()

    @inject.params(config='config')
    def resizeActionEvent(self, event=None, config=None):
        config.set('window.width', event.size().width())
        config.set('window.height', event.size().height())
        return event.accept()

    @inject.params(config='config')
    def on_window_resize(self, event=None, config=None):
        config.set('window.width', '%s' % event.size().width())
        config.set('window.height', '%s' % event.size().height())
        return event.accept()

    @inject.params(window='window')
    def _dialog_script_missed(self, message=None, window=None):
        message = "<h2>Optimisation script not found:</h2> <p>{}</p><br/>".format(message)
        return MessageBox.question(window, 'Execution script not found', message, MessageBox.Ok)

    @inject.params(window='window')
    def _dialog_script_error(self, message=None, window=None):
        message = "<h2>Can not execute optimisation script:</h2> <p>{}</p><br/>".format(message)
        return MessageBox.question(window, 'Can not execute optimisation script', message, MessageBox.Ok)

    @inject.params(window='window')
    def _dialog_script_execute(self, file=None, window=None):
        """

        :param file:
        :param window:
        :return:
        """
        if file is None or not len(file): return None

        message_content = open(file, 'r').read()
        message_content = message_content.replace("\n", "<br/>")
        message = "<h2>Execute optimisation script?</h2> <p>{}</p><br/>".format(message_content)
        result = MessageBox(window, 'Execute optimisation script?', message, MessageBox.Ok, MessageBox.Cancel)
        return result.exec_()

    def on_schema_apply(self, event=None):

        single_shot, errors = self.singleshot.script_apply("/tmp/performance-tuner/apply.sh")
        if errors is not None and len(errors):
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("<br/>".join(errors))

        if not len(single_shot) or not os.path.exists(single_shot):
            return self._dialog_script_missed(single_shot)

        if self._dialog_script_execute(single_shot) == QtWidgets.QMessageBox.Cancel:
            return shutil.rmtree(os.path.dirname(single_shot))

        try:
            os.system('pkexec sh {} '.format(single_shot))
            return shutil.rmtree(os.path.dirname(single_shot), ignore_errors=True)
        except Exception as ex:
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("{}".format(ex))

    def on_schema_cleanup(self, event=None):

        single_shot, errors = self.singleshot.script_cleanup("/tmp/performance-tuner/cleanup.sh")
        if errors is not None and len(errors):
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("<br/>".join(errors))

        if len(single_shot) and not os.path.exists(single_shot):
            return self._dialog_script_missed(single_shot)

        if self._dialog_script_execute(single_shot) == QtWidgets.QMessageBox.Cancel:
            return shutil.rmtree(os.path.dirname(single_shot))

        try:
            os.system('pkexec sh {} '.format(single_shot))
            return shutil.rmtree(os.path.dirname(single_shot))
        except Exception as ex:
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("{}".format(ex))

    def on_schema_performance(self, event=None):

        single_shot, errors = self.singleshot.script_performance("/tmp/performance-tuner/performance.sh")
        if errors is not None and len(errors):
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("<br/>".join(errors))

        if len(single_shot) and not os.path.exists(single_shot):
            return self._dialog_script_missed(single_shot)

        if self._dialog_script_execute(single_shot) == QtWidgets.QMessageBox.Cancel:
            return shutil.rmtree(os.path.dirname(single_shot))

        try:
            os.system('pkexec sh {} '.format(single_shot))
            return shutil.rmtree(os.path.dirname(single_shot))
        except Exception as ex:
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("{}".format(ex))

    def on_schema_powersave(self, event=None):

        single_shot, errors = self.singleshot.script_powersave("/tmp/performance-tuner/powersave.sh")
        if errors is not None and len(errors):
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("<br/>".join(errors))

        if len(single_shot) and not os.path.exists(single_shot):
            return self._dialog_script_missed(single_shot)

        if self._dialog_script_execute(single_shot) == QtWidgets.QMessageBox.Cancel:
            return shutil.rmtree(os.path.dirname(single_shot))

        try:
            os.system('pkexec sh {} '.format(single_shot))
            return shutil.rmtree(os.path.dirname(single_shot))
        except Exception as ex:
            shutil.rmtree(os.path.dirname(single_shot))
            return self._dialog_script_error("{}".format(ex))