import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from graphwindow import GraphWindow

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project' )

    # create widget
    w = GraphWindow()
    w.setWindowTitle( 'Events' )
    #w.show()
    w.showFullScreen() 

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application

    #sys.exit( app.exec_() )
    app.exec_()
    app.deleteLater()
    sys.exit()

