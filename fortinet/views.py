from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .parimiko_client import ParamikoClient
from .fortinet_util import FortinetUtil

#import logging
#logging.basicConfig()
#logger = logging.getLogger(__name__)
import logging
LOG_FILENAME = '/var/log/fortis-django.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
        print 123 
	logger.debug('debug-Something went wrong!')
	logger.info('info-Something went wrong!')

	logger.error('error-Something went wrong!')
        print 456
        return JsonResponse({'foo':'bar'})

def testFortinet(request):
        client = ParamikoClient()
        response = client.testFortinet()
        print response
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
