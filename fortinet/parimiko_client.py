import paramiko
import logging

class ParamikoClient:

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
