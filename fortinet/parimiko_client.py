import paramiko
import logging
LOG_FILENAME = '/var/log/fortis-django.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ParamikoClient:

	def sendFortinetCommand(self, hostname, port, username, password, command):
		ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostname, port=port, username=username, password=password, timeout=3.0)
		stdin, stdout, stderr = ssh.exec_command(command)
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

		return {"status": True, "data" : result } 

        def test(self):
                print 'test....'
                return 'data..................'

        def testFortinet(self):
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname='192.168.99.254', port=22, username='sclin0323@gmail.com', password='0970866777', timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user device \n edit test1 \n set mac 12:34:56:00:00:00 \n next \n end \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def showUserDeviceByUserDevice(self, fortinetParameters):
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                deviceName = fortinetParameters['deviceName']

		ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n show user device '+deviceName+' \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def showUserDeviceGroupByUserDeviceGroup(self, fortinetParameters):
		hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
		groupName = fortinetParameters['groupName']

		ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n show user device-group '+groupName+' \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def reenableSystemInterface(self, fortinetParameters):
		hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']

		ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

		stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config system interface \n edit port34 \n set device-identification disable \n set device-identification enable \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def unselectConfigUserDeviceGroups(self, fortinetParameters):
		hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                deviceName = fortinetParameters['deviceName']
                groupName = fortinetParameters['groupName']

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user device-group \n edit '+groupName+' \n unselect member '+deviceName+' \n next \n end \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }
		

        def deleteConfigUserDevice(self, fortinetParameters):
		hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                deviceName = fortinetParameters['deviceName']

		ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user device \n delete '+deviceName+' \n end \n end \n exit')
                result = []
                for line in stdout:
                        result.append(line)
		ssh.close()

                return {"status": True, "data" : result }

	# Add
	def appendConfigUserDeviceGroups(self, fortinetParameters):
		print fortinetParameters
		hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                deviceName = fortinetParameters['deviceName']
                groupName = fortinetParameters['groupName']

		ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)
	
		stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user device-group \n edit '+groupName+' \n append member '+deviceName+' \n next \n end \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	# Add Update
        def editConfigUserDevice(self, fortinetParameters):
                print fortinetParameters
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                deviceName = fortinetParameters['deviceName']
                macAddress = fortinetParameters['macAddress']

		ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user device \n edit '+deviceName+' \n set mac '+macAddress+' \n next \n end \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def editConfigUserLocal(self, fortinetParameters):
		print fortinetParameters
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                account = fortinetParameters['account']
                userPassword = fortinetParameters['userPassword']

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)


                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user local \n edit '+account+' \n set type password \n set passwd '+userPassword+' \n next \n end \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def deleteConfigUserLocal(self, fortinetParameters):
                print fortinetParameters
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                account = fortinetParameters['account']

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)


                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user local \n delete '+account+' \n end \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def editConfigUserGroup(self, fortinetParameters):
                print fortinetParameters
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                account = fortinetParameters['account']
                userGroup = fortinetParameters['userGroup']

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user group \n edit '+userGroup+' \n append member '+account+' \n next \n end \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

        def showConfigUserDevices(self, fortinetParameters):
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n conf user device \n show \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }


        def getSystemStatus(self, fortinetParameters):
                        hostName = fortinetParameters['ip']
                        port = int(fortinetParameters['port'])
                        userName = fortinetParameters['userName']
                        password = fortinetParameters['password']

			ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)
                        stdin, stdout, stderr = ssh.exec_command('get system status')

                        result = []
                        for line in stdout:
                                result.append(line)
                        ssh.close()

                        return {"status": True, "data" : result }


	# Add
        def appendConfigUserGroup(self, fortinetParameters):
                print fortinetParameters
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']

                memberName = fortinetParameters['memberName']
                groupName = fortinetParameters['groupName']

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user group \n edit '+groupName+' \n append member '+memberName+' \n next \n end \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	def unselectConfigUserGroup(self, fortinetParameters):
                hostName = fortinetParameters['ip']
                port = int(fortinetParameters['port'])
                userName = fortinetParameters['userName']
                password = fortinetParameters['password']
                memberName = fortinetParameters['memberName']
                groupName = fortinetParameters['groupName']

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostName, port=port, username=userName, password=password, timeout=3.0)

                stdin, stdout, stderr = ssh.exec_command('conf vdom \n edit wireless-0 \n config user group \n edit '+groupName+' \n unselect member '+memberName+' \n next \n end \n end \n exit \n')
                result = []
                for line in stdout:
                        result.append(line)
                ssh.close()

                return {"status": True, "data" : result }

	
