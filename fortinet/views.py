from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .parimiko_client import ParamikoClient
from .fortinet_util import FortinetUtil

import logging
LOG_FILENAME = '/var/log/fortis-django.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger(__name__)
# Create your views here.

def sendFortinetCommand(request):
	logger.info('================================== [REQUEST] =====================================')
	logger.info(request)

	hostname = request.GET.get('hostname')
	port = int(request.GET.get('port'))
	username = request.GET.get('username')
	password = request.GET.get('password')
	command = request.GET.get('command')

	client = ParamikoClient()
	response = client.sendFortinetCommand(hostname, port, username, password, command)
	logger.info(JsonResponse(response))
	return JsonResponse(response)

def index(request):
        print 123 
	logger.debug('debug-Something went wrong!')
	logger.info('info-Something went wrong!')

	logger.error('error-Something went wrong!')
        print 456
        return JsonResponse({'foo':'bar'})

def testFortinet(request):
	logger.info('================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        response = client.testFortinet()
        print response
        return JsonResponse(response)

def showUserDeviceByUserDevice(request):
	logger.info('================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['deviceName'] = request.GET.get('deviceName')

        response = client.showUserDeviceByUserDevice(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)

def showUserDeviceGroupByUserDeviceGroup(request):
	logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

	# Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['groupName'] = request.GET.get('groupName')

        response = client.showUserDeviceGroupByUserDeviceGroup(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)

def reenableSystemInterface(request):
	logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

	 # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

	response = client.reenableSystemInterface(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)

def unselectConfigUserDeviceGroups(request):
	logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()

         # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['deviceName'] = request.GET.get('deviceName')
        checkResult['message']['groupName'] = request.GET.get('groupName')

	response = client.unselectConfigUserDeviceGroups(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)

def appendConfigUserDeviceGroups(request):
	logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()

	 # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

	checkResult['message']['deviceName'] = request.GET.get('deviceName')
        checkResult['message']['groupName'] = request.GET.get('groupName')

	response = client.appendConfigUserDeviceGroups(checkResult['message'])
	logger.info(JsonResponse(response))
        return JsonResponse(response)

def showConfigUserDeviceGroups(request):
        return JsonResponse({"123":"abc"})

def deleteConfigUserDevice(request):
	logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()
	
	# Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['deviceName'] = request.GET.get('deviceName')

        response = client.deleteConfigUserDevice(checkResult['message'])
	logger.info(JsonResponse(response))
        return JsonResponse(response)

def editConfigUserDevice(request):
        logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['deviceName'] = request.GET.get('deviceName')
        checkResult['message']['macAddress'] = request.GET.get('macAddress')

        response = client.editConfigUserDevice(checkResult['message'])

        logger.info(JsonResponse(response))

        return JsonResponse(response)

def showUserDevices(request):
        logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult['message'])

        response = client.showUserDevices()
	logger.info(JsonResponse(response))
        return JsonResponse(response)

def getSystemStatus(request):
	logger.info('===================================== [REQUEST] =====================================')
	logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

	response = client.getSystemStatus(checkResult['message'])
	logger.info(JsonResponse(response))
        return JsonResponse(response)

def editConfigUserLocal(request):
        logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

	checkResult['message']['account'] = request.GET.get('account')
        checkResult['message']['userPassword'] = request.GET.get('userPassword')

        response = client.editConfigUserLocal(checkResult['message'])

        logger.info(JsonResponse(response))
        return JsonResponse(response)

def deleteConfigUserLocal(request):
        logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['account'] = request.GET.get('account')

        response = client.deleteConfigUserLocal(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)

def editConfigUserGroup(request):
        logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

	checkResult['message']['account'] = request.GET.get('account')
        checkResult['message']['userGroup'] = request.GET.get('userGroup')

        response = client.editConfigUserGroup(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)

def appendConfigUserGroup(request):
        logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

         # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['memberName'] = request.GET.get('memberName')
        checkResult['message']['groupName'] = request.GET.get('groupName')

        response = client.appendConfigUserGroup(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)


def unselectConfigUserGroup(request):
        logger.info('===================================== [REQUEST] =====================================')
        logger.info(request)
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

         # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['memberName'] = request.GET.get('memberName')
        checkResult['message']['groupName'] = request.GET.get('groupName')

        response = client.unselectConfigUserGroup(checkResult['message'])
        logger.info(JsonResponse(response))
        return JsonResponse(response)
