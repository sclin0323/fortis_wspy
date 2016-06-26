from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'testFortinet/$', views.testFortinet, name='testFortinet'),

    url(r'showConfigUserDeviceGroups/$', views.showConfigUserDeviceGroups, name='showConfigUserDeviceGroups'),

    url(r'appendConfigUserDeviceGroups/$', views.appendConfigUserDeviceGroups, name='appendConfigUserDeviceGroups'),

    url(r'unselectConfigUserDeviceGroups/$', views.unselectConfigUserDeviceGroups, name='unselectConfigUserDeviceGroups'),

    url(r'editConfigUserDevice/$', views.editConfigUserDevice, name='editConfigUserDevice'),

    url(r'deleteConfigUserDevice/$', views.deleteConfigUserDevice, name='deleteConfigUserDevice'),

    url(r'getSystemStatus/$', views.getSystemStatus, name='getSystemStatus'),

    url(r'showUserDevices/$', views.showUserDevices, name='showUserDevices')
]
