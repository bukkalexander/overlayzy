from PyQt5 import QtWidgets, QtCore, QtGui
import image_blurring
import win32api

i = 0
class TransparentOverlay(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        
        self.detection = image_blurring.Detection(20,435,1040,490,"bullet 1")

        # Initial central rectangle properties
        self.centerWidth = self.geometry().width() // 2
        self.centerHeight = self.geometry().height() // 2

        # Set up a timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.onTimeout)
        fps = 5
        ms_per_update = int(1000/fps)
        self.timer.start(ms_per_update)  # Trigger every 1000 milliseconds (1 second)

    def initUI(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Make the window's background transparent
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setGeometry(QtWidgets.QApplication.desktop().availableGeometry())  # Fullscreen overlay
        self.show()

    def onTimeout(self):
        # Update properties for demonstration. This could be any logic you need.
        mouse_position = get_mouse_position()
        print(f"mouse position: x={mouse_position.x}, y={mouse_position.y}")
        self.detection = image_blurring.get_detection(mouse_position)

        self.centerWidth = max(100, (self.centerWidth - 10) % self.geometry().width())
        self.centerHeight = max(100, (self.centerHeight - 10) % self.geometry().height())
        global i
        print(f"{i}")
        i += 1
        # Trigger a repaint
        self.update()

    def paintEvent(self, event):

        if not self.detection: 
            return
        
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.NoPen)
        
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))  # Semi-transparent black
        painter.setBrush(brush)
        
        screenRect = self.geometry()
        
        # Central transparent area dimensions
        #centerX = (screenRect.width() - self.centerWidth) // 2
        #centerY = (screenRect.height() - self.centerHeight) // 2
        


        # Draw the four rectangles
        #top
        painter.drawRect(0, 0, screenRect.width(), self.detection.top)
        #bottom
        painter.drawRect(0, self.detection.bottom, screenRect.width(), screenRect.height()-self.detection.bottom)
        #left
        painter.drawRect(0, self.detection.top, self.detection.left, self.detection.height)
        #right
        painter.drawRect(self.detection.right, self.detection.top, screenRect.width()-self.detection.right, self.detection.height)
        
        #painter.drawRect(0, centerY + self.centerHeight, screenRect.width(), centerY)
        #painter.drawRect(0, centerY, centerX, self.centerHeight)
        #painter.drawRect(centerX + self.centerWidth, centerY, centerX, self.centerHeight)

def get_mouse_position():
    position = win32api.GetCursorPos()
    return image_blurring.Point(x=position[0], y=position[1])

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = TransparentOverlay()
    sys.exit(app.exec_())