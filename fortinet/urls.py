from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'sendFortinetCommand/$', views.sendFortinetCommand, name='sendFortinetCommand'),

    url(r'testFortinet/$', views.testFortinet, name='testFortinet'),

    url(r'reenableSystemInterface/$', views.reenableSystemInterface, name='reenableSystemInterface'),

    url(r'showConfigUserDeviceGroups/$', views.showConfigUserDeviceGroups, name='showConfigUserDeviceGroups'),

    url(r'appendConfigUserDeviceGroups/$', views.appendConfigUserDeviceGroups, name='appendConfigUserDeviceGroups'),

    url(r'unselectConfigUserDeviceGroups/$', views.unselectConfigUserDeviceGroups, name='unselectConfigUserDeviceGroups'),

    url(r'editConfigUserDevice/$', views.editConfigUserDevice, name='editConfigUserDevice'),

    url(r'deleteConfigUserDevice/$', views.deleteConfigUserDevice, name='deleteConfigUserDevice'),

    url(r'getSystemStatus/$', views.getSystemStatus, name='getSystemStatus'),

    url(r'showUserDevices/$', views.showUserDevices, name='showUserDevices'),

    url(r'showUserDeviceByUserDevice/$', views.showUserDeviceByUserDevice, name='showUserDeviceByUserDevice'),

    url(r'showUserDeviceGroupByUserDeviceGroup/$', views.showUserDeviceGroupByUserDeviceGroup, name='showUserDeviceGroupByUserDeviceGroup'),

    url(r'editConfigUserLocal/$', views.editConfigUserLocal, name='editConfigUserLocal'),

    url(r'deleteConfigUserLocal/$', views.deleteConfigUserLocal, name='deleteConfigUserLocal'),   

    url(r'editConfigUserGroup/$', views.editConfigUserGroup, name='editConfigUserGroup'),

    url(r'appendConfigUserGroup/$', views.appendConfigUserGroup, name='appendConfigUserGroup'),

    url(r'unselectConfigUserGroup/$', views.unselectConfigUserGroup, name='unselectConfigUserGroup')
]
