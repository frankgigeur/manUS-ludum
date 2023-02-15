# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 Multimedia Camera Example"""

import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget)
from PySide6.QtMultimedia import (QCamera, QMediaCaptureSession, QMediaDevices)
from PySide6.QtMultimediaWidgets import QVideoWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._capture_session = None
        self._camera = None
        self._camera_info = None

        available_cameras = QMediaDevices.videoInputs()
        if available_cameras:
            self._camera_info = available_cameras[0]
            self._camera = QCamera(self._camera_info)
            self._capture_session = QMediaCaptureSession()
            self._capture_session.setCamera(self._camera)

        self._tab_widget = QTabWidget()
        self.setCentralWidget(self._tab_widget)

        self._camera_viewfinder = QVideoWidget()
        self._tab_widget.addTab(self._camera_viewfinder, "Viewfinder")

        if self._camera:
            name = self._camera_info.description()
            self.setWindowTitle(f"PySide6 Camera Example ({name})")
            self._capture_session.setVideoOutput(self._camera_viewfinder)
            self._camera.start()
        else:
            self.setWindowTitle("PySide6 Camera Example")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3, available_geometry.height() / 2)
    main_win.show()
    sys.exit(app.exec())
