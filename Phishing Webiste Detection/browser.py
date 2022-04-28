import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from testURL import *


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl('https://google.com'))
    self.setCentralWidget(self.browser)
    self.showMaximized()

    navbar = QToolBar()
    self.addToolBar(navbar)

    back_btn = QAction('<-', self)
    back_btn.triggered.connect(self.browser.back)
    navbar.addAction(back_btn)

    fwd_btn = QAction('->', self)
    fwd_btn.triggered.connect(self.browser.forward)
    navbar.addAction(fwd_btn)

    home_btn = QAction('H', self)
    home_btn.triggered.connect(self.nav_home)
    navbar.addAction(home_btn)

    self.url_bar = QLineEdit()
    self.url_bar.returnPressed.connect(self.nav_url)
    navbar.addWidget(self.url_bar)

    go_btn = QAction('GO', self)
    go_btn.triggered.connect(self.nav_url)
    navbar.addAction(go_btn)
    
  def nav_home(self):
    self.browser.setUrl(QUrl("http://google.com"))

  def nav_url(self):
    url = self.url_bar.text()
    if url.startswith("www."):
      url = "https://"+url
    elif not url.startswith("http"):
      url = "https://www."+url
    try:
      out = test(url)
    except:
      out = 'benign'
    if out == 'benign':
      self.browser.setUrl(QUrl(url))
    else:
      with open('index.html') as f:
        html = f.read()
      self.browser.setHtml(html)

app = QApplication(sys.argv)
QApplication.setApplicationName("Test Browser")
window = MainWindow()
app.exec()