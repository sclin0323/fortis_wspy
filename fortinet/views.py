from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .parimiko_client import ParamikoClient
from .fortinet_util import FortinetUtil

import json

# Create your views here.

def index(request):
        client = ParamikoClient()
        content = client.test()
        print content

        print request.GET['message123']
        return JsonResponse({'foo':'bar'})

def testFortinet(request):
        client = ParamikoClient()
        response = client.testFortinet()
        print response
        return JsonResponse(response)

def unselectConfigUserDeviceGroups(request):
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()

         # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['deviceName'] = request.GET.get('deviceName')
        checkResult['message']['groupName'] = request.GET.get('groupName')

	response = client.unselectConfigUserDeviceGroups(checkResult['message'])
        print '[RESPONSE] ', response
        return JsonResponse(response)

def appendConfigUserDeviceGroups(request):
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()

	 # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

	checkResult['message']['deviceName'] = request.GET.get('deviceName')
        checkResult['message']['groupName'] = request.GET.get('groupName')

	response = client.appendConfigUserDeviceGroups(checkResult['message'])
        print '[RESPONSE] ', response
        return JsonResponse(response)

def showConfigUserDeviceGroups(request):
        return JsonResponse({"123":"abc"})

def deleteConfigUserDevice(request):
	client = ParamikoClient()
        fortinetUtil = FortinetUtil()
	
	# Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['deviceName'] = request.GET.get('deviceName')

        response = client.deleteConfigUserDevice(checkResult['message'])
	print '[RESPONSE] ', response
        return JsonResponse(response)

def editConfigUserDevice(request):
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

        checkResult['message']['deviceName'] = request.GET.get('deviceName')
        checkResult['message']['macAddress'] = request.GET.get('macAddress')

        response = client.editConfigUserDevice(checkResult['message'])

        print '[RESPONSE] ', response

        return JsonResponse(response)

def showUserDevices(request):
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult['message'])

        response = client.showUserDevices()

        return JsonResponse(response)

def getSystemStatus(request):
        client = ParamikoClient()
        fortinetUtil = FortinetUtil()

        # Check Fortinet Parameters 
        checkResult = fortinetUtil.checkFortinetParameters(request)
        if checkResult['status'] == False:
                return JsonResponse(checkResult)

	response = client.getSystemStatus(checkResult['message'])
        print '[RESPONSE] ', response

        return JsonResponse(response)
