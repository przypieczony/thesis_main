# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Tue Mar 17 20:30:38 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
import random
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(740, 551)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Inputdata = QtGui.QWidget()
        self.Inputdata.setObjectName(_fromUtf8("Inputdata"))
        self.simulateRadioButton = QtGui.QRadioButton(self.Inputdata)
        self.simulateRadioButton.setGeometry(QtCore.QRect(560, 10, 116, 22))
        self.simulateRadioButton.setStatusTip(_fromUtf8(""))
        self.simulateRadioButton.setCheckable(True)
        self.simulateRadioButton.setChecked(True)
        self.simulateRadioButton.setObjectName(_fromUtf8("simulateRadioButton"))
        self.layoutWidget = QtGui.QWidget(self.Inputdata)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 191, 220))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.sourceAddressField = QtGui.QLineEdit(self.layoutWidget)
        self.sourceAddressField.setStatusTip(_fromUtf8(""))
        self.sourceAddressField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.sourceAddressField.setInputMask(_fromUtf8(""))
        self.sourceAddressField.setText(_fromUtf8("192.168.1.1"))
        self.sourceAddressField.setObjectName(_fromUtf8("sourceAddressField"))
        self.verticalLayout.addWidget(self.sourceAddressField)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.sourcePortField = QtGui.QLineEdit(self.layoutWidget)
        self.sourcePortField.setStatusTip(_fromUtf8(""))
        self.sourcePortField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.sourcePortField.setInputMask(_fromUtf8(""))
        self.sourcePortField.setText(_fromUtf8("6666"))
        self.sourcePortField.setObjectName(_fromUtf8("sourcePortField"))
        self.verticalLayout.addWidget(self.sourcePortField)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.destAddresField = QtGui.QLineEdit(self.layoutWidget)
        self.destAddresField.setStatusTip(_fromUtf8(""))
        self.destAddresField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.destAddresField.setInputMask(_fromUtf8(""))
        self.destAddresField.setText(_fromUtf8("192.168.1.2"))
        self.destAddresField.setObjectName(_fromUtf8("destAddresField"))
        self.verticalLayout.addWidget(self.destAddresField)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.destPortField = QtGui.QLineEdit(self.layoutWidget)
        self.destPortField.setStatusTip(_fromUtf8(""))
        self.destPortField.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.destPortField.setInputMask(_fromUtf8(""))
        self.destPortField.setText(_fromUtf8("6666"))
        self.destPortField.setObjectName(_fromUtf8("destPortField"))
        self.verticalLayout.addWidget(self.destPortField)
        self.layoutWidget1 = QtGui.QWidget(self.Inputdata)
        self.layoutWidget1.setGeometry(QtCore.QRect(460, 390, 211, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clearButton = QtGui.QPushButton(self.layoutWidget1)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.acceptButton = QtGui.QPushButton(self.layoutWidget1)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.horizontalLayout.addWidget(self.acceptButton)
        self.splitter = QtGui.QSplitter(self.Inputdata)
        self.splitter.setGeometry(QtCore.QRect(280, 40, 371, 331))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_5 = QtGui.QLabel(self.splitter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.sipTemplate = QtGui.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.sipTemplate.setFont(font)
        self.sipTemplate.setReadOnly(True)
        self.sipTemplate.setObjectName(_fromUtf8("sipTemplate"))
        self.tabWidget.addTab(self.Inputdata, _fromUtf8(""))
        self.Register = QtGui.QWidget()
        self.Register.setObjectName(_fromUtf8("Register"))
        self.simulateButton = QtGui.QPushButton(self.Register)
        self.simulateButton.setGeometry(QtCore.QRect(610, 410, 98, 27))
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.flowField = QtGui.QTextEdit(self.Register)
        self.flowField.setGeometry(QtCore.QRect(350, 100, 213, 291))
        self.flowField.setReadOnly(True)
        self.flowField.setObjectName(_fromUtf8("flowField"))
        self.flowLabel = QtGui.QLabel(self.Register)
        self.flowLabel.setGeometry(QtCore.QRect(570, 230, 112, 17))
        self.flowLabel.setObjectName(_fromUtf8("flowLabel"))
        self.splitter_2 = QtGui.QSplitter(self.Register)
        self.splitter_2.setGeometry(QtCore.QRect(30, 130, 291, 271))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.labelCurrentMessage = QtGui.QLabel(self.splitter_2)
        self.labelCurrentMessage.setObjectName(_fromUtf8("labelCurrentMessage"))
        self.currentMessageField = QtGui.QTextEdit(self.splitter_2)
        self.currentMessageField.setReadOnly(True)
        self.currentMessageField.setObjectName(_fromUtf8("currentMessageField"))
        self.widget = QtGui.QWidget(self.Register)
        self.widget.setGeometry(QtCore.QRect(40, 20, 611, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.phone = QtGui.QLabel(self.widget)
        self.phone.setText(_fromUtf8(""))
        self.phone.setPixmap(QtGui.QPixmap(_fromUtf8("img/phone.jpg")))
        self.phone.setScaledContents(True)
        self.phone.setObjectName(_fromUtf8("phone"))
        self.horizontalLayout_3.addWidget(self.phone)
        self.horizontalSlider = QtGui.QSlider(self.widget)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setAcceptDrops(False)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_3.addWidget(self.horizontalSlider)
        self.server = QtGui.QLabel(self.widget)
        self.server.setText(_fromUtf8(""))
        self.server.setPixmap(QtGui.QPixmap(_fromUtf8("img/sip proxy server.jpg")))
        self.server.setScaledContents(True)
        self.server.setObjectName(_fromUtf8("server"))
        self.horizontalLayout_3.addWidget(self.server)
        self.tabWidget.addTab(self.Register, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_template = QtGui.QAction(MainWindow)
        self.actionAdd_template.setObjectName(_fromUtf8("actionAdd_template"))
        self.menuFile.addAction(self.actionAdd_template)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.template_vars = {}

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sourceAddressField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sourcePortField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destAddresField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.destPortField.clear)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sipTemplate.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        MainWindow.setStatusTip(_translate("MainWindow", "Ready", None))
        self.simulateRadioButton.setText(_translate("MainWindow", "Simulation", None))
        self.label.setText(_translate("MainWindow", "Enter source address:", None))
        self.sourceAddressField.setPlaceholderText(_translate("MainWindow", "e. g.192.168.100.1", None))
        self.label_2.setText(_translate("MainWindow", "Enter source port:", None))
        self.sourcePortField.setPlaceholderText(_translate("MainWindow", "e.g. 5060", None))
        self.label_3.setText(_translate("MainWindow", "Enter destiantion address:", None))
        self.destAddresField.setPlaceholderText(_translate("MainWindow", "e. g.192.168.100.2", None))
        self.label_4.setText(_translate("MainWindow", "Enter destination port:", None))
        self.destPortField.setPlaceholderText(_translate("MainWindow", "e.g. 5060", None))
        self.clearButton.setText(_translate("MainWindow", "Clear", None))
        self.acceptButton.setText(_translate("MainWindow", "Accept", None))
        self.label_5.setText(_translate("MainWindow", "SIP Template", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inputdata), _translate("MainWindow", "Input data", None))
        self.simulateButton.setText(_translate("MainWindow", "Simulate", None))
        self.flowLabel.setText(_translate("MainWindow", "Connection flow", None))
        self.labelCurrentMessage.setText(_translate("MainWindow", "Current message", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Register), _translate("MainWindow", "Register", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuExit.setTitle(_translate("MainWindow", "Exit", None))
        self.actionAdd_template.setText(_translate("MainWindow", "Add template", None))

        self.acceptButton.clicked.connect(self.getParameters)
        self.simulateButton.clicked.connect(self.startRegister)
 

    def getParameters(self):
        """This function captures input parameters and shows message template"""
 
        self.sourceAddress = str(self.sourceAddressField.text())
        self.destAddress = str(self.destAddresField.text())
        if self.sourceAddress != self.destAddress:
            try:
                socket.inet_aton(self.sourceAddress)
                socket.inet_aton(self.destAddress)
            except socket.error:
                self.statusbar.showMessage('Error! Wrong ip address')
        else:
            self.statusbar.showMessage('Error! ip addresses are the same')
        try:
            self.sourcePort = int(self.sourcePortField.text())
            self.destPort = int(self.destPortField.text())
        except ValueError:
            self.statusbar.showMessage('Error! Empty port number, choose between 1024-65535')
        if (self.sourcePort < 1024 or self.sourcePort > 65535) or \
            (self.destPort < 1024 or self.destPort > 65535):
            self.statusbar.showMessage('Error! Wrong port number, choose between 1024-65535')
 
        if self.simulateRadioButton.isChecked():
            random_loopback = "127.{}.{}.{}".format(random.randint(1,255), \
                random.randint(1,255), random.randint(1,255))
            self.sourceAddress = random_loopback
            self.destAddress = "127.0.0.1"

        self.template_vars = {
        "source_ip": self.sourceAddress,
        "source_port": self.sourcePort,
        "dest_ip": self.destAddress,
        "dest_port": self.destPort
        }

        self.sipTemplate.insertPlainText(self.printTemplate(self.template_vars))
        self.createSockets(self.template_vars) #This is awful, it should be relocated outside this function

    def printTemplate(self, template_vars):
        """Method to print text into text box"""

        template = """OPTIONS sip:%(dest_ip)s:%(dest_port)s SIP/2.0
        Via: SIP/2.0/UDP %(source_ip)s:%(source_port)s
        Max-Forwards: 70
        From: "fake" <sip:fake@%(source_ip)s>
        To: <sip:%(dest_ip)s:%(dest_port)s>
        Contact: <sip:fake@%(source_ip)s:%(source_port)s>
        Call-ID: fake-id@%(source_ip)s
        User-Agent: SIPPing
        Date: Wed, 24 Apr 2013 20:35:23 GMT
        Allow: INVITE, ACK, CANCEL, OPTIONS, BYE, REFER, SUBSCRIBE, NOTIFY, INFO, PUBLISH
        Supported: replaces, timer"""

        for k in template_vars.keys():
            if k.startswith("."):
                template_vars[k[1:]] = eval(template_vars[k])
        try:
            ret = template % template_vars #replaces %(<variable>)s by template_vars
        except KeyError, e:
            sys.stderr.write("ERROR: missing template variable. %s\n" % e)
            sys.exit(-1)
        except Exception, e:
            sys.stderr.write("ERROR: error in template processing. %s\n" % e)
            sys.exit(-1)
        return ret
     
    def createSockets(self, template_vars):
        #import pdb; pdb.set_trace()
        try:
            self.sending_sock = self.open_sock(self.template_vars["source_ip"], self.template_vars["source_port"])
            self.receiving_sock = self.open_sock(self.template_vars["dest_ip"], self.template_vars["dest_port"])
            self.statusbar.showMessage('Parameters saved')
        except Exception, e:
            self.statusbar.showMessage('Error! cannot open socket.', e)

    def open_sock(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            sock.setblocking(0)
        except Exception, e:
            sys.stderr.write("ERROR: cannot create socket. %s\n" % e)
            sys.exit(-1)
        try:
            sock.seckopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.seckopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
            pass
        sock.bind((ip, port))
        sock.settimeout(10)
        return sock

    def startRegister(self, message):
        """Register case scenario"""
        #function which sends particular message
        #function that 
        #try:
        #    for req in gen_request(template_vars):


    def gen_request(template_vars):
        """Generates request message"""

        try:
            f = open(options.request_template)
            file_request = f.read()
            f.close()
            request = render_template(file_request, template_vars)
        except Exception, e:
            sys.stderr.write("ERROR: cannot open file %s. %s\n" % (options.request_template, e))
            sys.exit(-1)    
        try:
            req = Request(request)
        except SipUnpackError, e:
            sys.stderr.write("ERROR: malformed SIP Request. %s\n" % e)
            sys.exit(-1)
        
        if "cseq" not in req.headers:
            req.headers["cseq"] = "%d %s" % (i, req.method)
        yield str(req)


    def main():
        # usage = """%prog [OPTIONS]"""
        # opt = optparse.OptionParser(usage=usage)
 
        # opt.add_option('-c', dest='count', type='int', default=sys.maxint,
        #                        help='Total number of queries to send')
 
        # opt.add_option('-i', dest='wait', type='float', default=1,
        #                        help='Specify packet send interval time in seconds')
        
        # opt.add_option('-T', dest='timeout', type='float', default=1,
        #                        help='Specify receiving timeout in seconds')
 
        # opt.add_option('-v', dest='var', type='string', default=[""], action='append',
        #                        help='add a template variable in format varname:value')
 
        # opt.add_option('-V', dest='verbose', default=False, action='store_true',
        #                        help='be verbose dumping full requests / responses')
 
        # opt.add_option('-q', dest='quiet', default=False, action='store_true',
        #                        help='be quiet and never print any report')
 
        # opt.add_option('-a', dest='aggressive', default=False, action='store_true',
        #                        help='aggressive mode: ignore any response')
 
        # opt.add_option('-S', dest='sourceAddress', type='string', default="0.0.0.0",
        #                        help='Specify ip address to bind for sending and receiving UDP datagrams')
 
        # opt.add_option('-P', dest='source_port', type='int', default=5060,
        #                        help='Specify the port number to use as a source port in UDP datagrams')
 
        # opt.add_option('-d', dest='dest_ip', type='string', default=None,
        #                        help='*mandatory* Specify the destination ip address')
 
        # opt.add_option('-p', dest='dest_port', type='int', default=5060,
        #                        help='*mandatory* Specify the destination port number')
 
        # opt.add_option('-r', dest='request_template', type='string', default=None,
        #                        help='Specify the request template file')
 
        # opt.add_option('-t', dest='print_template', action="store_true", default=False, 
        #                         help='print the default request template')
        
        # opt.add_option('-m', dest='modules', type='string', default=[], action='append',
        #                        help='load additionals Python modules used in Python interpreted template variables')
        
        # opt.add_option('-O', dest='out_regex', type='string', default="",
        #                        help='regex to apply to response received, (default \'(.*\n)*\')')
 
        # opt.add_option('-R', dest='out_replace', type='string', default="",
        #         help='print this replace string applied to the response')
 
        # opt.add_option('-x', dest='simulate', action="store_true", default=False,
        #                        help='simulates ip addresses')
 
        # options, args = opt.parse_args(sys.argv[1:])
        
        # if options.print_template:
        #     sys.stderr.write("%s\n" % def_request)
        #     sys.exit()
        
        # for m in options.modules:
        #     globals()[m] = __import__(m)
        

 
        # first var is empty by default. It has to be analyzed deeper
        # for v in options.var[1:]:
        #     try:
        #         key = v.split(":")[0]
        #         val = ":".join(v.split(":")[1:])
        #         template_vars.update({key: val})
        #     except IndexError:
        #         sys.stderr.write("ERROR: variables must be in format name:value. %s\n" % v)
        #         opt.print_help()
        #         sys.exit() 
            
        if options.verbose:
            sys.stderr.write("=======================================\n")
            sys.stderr.write("I'm using these variables in templates: \n")
            sys.stderr.write("=======================================\n")
            for k in template_vars:
                sys.stderr.write("%s: %s\n" % (k, template_vars[k]))
            sys.stderr.write("=======================================\n\n")
 
        count = options.count
        
 
        sent = rcvd = ok_recvd = notify_recvd = 0 
        
        try:
            for req in gen_request(template_vars, options):
                try:
                    sip_req = Request(req)
                    #Add Content-Lenght if missing
                    if "content-length" not in sip_req.headers:
                        sip_req.headers["content-length"] = len(sip_req.body)
                    
                    try:    
                        sending_sock.sendto(str(sip_req),(options.dest_ip, options.dest_port))
                    except Exception, e:
                        sys.stderr.write("ERROR: cannot send packet to %s:%d. %s\n" % (options.dest_ip, options.dest_port, e))
                    if not options.quiet:
                        sys.stderr.write("sent Request %s to %s:%d cseq=%s len=%d\n" % (sip_req.method, template_vars['dest_ip'], options.dest_port, sip_req.headers['cseq'].split()[0], len(str(sip_req))))
                        if options.verbose:
                            sys.stderr.write("\n=== Full Request sent ===\n\n")
                            sys.stderr.write("%s\n" % sip_req)
                    sent += 1
                    
 
                    if not options.aggressive:
                        #import pdb; pdb.set_trace()
                        read = [receiving_sock]
                        inputready,outputready,exceptready = select.select(read,[],[],options.timeout)
                    
                        for s in inputready:
                            if s == receiving_sock:
                                buf = None
                                buf = receiving_sock.recvfrom(0xffff)
                                print_reply(buf, template_vars, options.out_regex, options.out_replace, verbose=options.verbose, quiet=options.quiet)
                                rcvd += 1
        
                except socket.timeout:
                    pass
                time.sleep(options.wait)
        except KeyboardInterrupt:
            pass
 
        if not options.quiet:
            sys.stderr.write('\n--- statistics ---\n')
            sys.stderr.write('%d packets transmitted, %d packets received, %.1f%% packet loss\n' % (sent, rcvd, (float(sent - rcvd) / sent) * 100))
 
 
# class MyPopup(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)

#     def paintEvent(self, e):
#         dc = QPainter(self)
#         dc.drawLine(0, 0, 100, 100)
#         dc.drawLine(100, 0, 0, 100) 

#     def doit(self):
#         print "Opening a new popup window..."
#         self.w = MyPopup()
#         self.w.setGeometry(QRect(100, 100, 400, 200))
#         self.w.show()
 
if __name__ == "__main__":
#try:
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
#except BaseException:
    #raw_input("Ups.. Something unexpected happened, press any key to shutdown...")
    sys.exit(app.exec_())
 

