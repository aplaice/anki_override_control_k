from aqt.qt import *
from aqt.webview import AnkiWebView

def myEventFilter(self, obj, evt):
    # disable pinch to zoom gesture
    if isinstance(evt, QNativeGestureEvent):
        return True
    elif evt.type() == QEvent.MouseButtonRelease:
        if evt.button() == Qt.MidButton and isLin:
            self.onMiddleClickPaste()
            return True
        return False
    # everything in this function except the next four lines is copied from aqt/webview.py
    elif isinstance(evt, QKeyEvent):
        if (evt.key() == Qt.Key_K) and (evt.modifiers() == Qt.ControlModifier): #and (evt.nativeModifiers() == 4):
            if evt.type() == QEvent.ShortcutOverride:
                return True
    return False

AnkiWebView.eventFilter = myEventFilter
