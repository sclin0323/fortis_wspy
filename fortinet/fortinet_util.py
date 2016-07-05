class FortinetUtil:

        def test(self):
                print 'test....'
                return 'data..................'

        def checkFortinetParameters(self, request):
                if not request.GET.get('ip'):
                        return {
                                "status": False,
                                "message": "Can not get parameter: [ip]"
                        }

                if not request.GET.get('port'):
                        return {
                                "status": False,
                                "message": "Can not get parameter: [port]"
                        }

                if not request.GET.get('userName'):
                        return {
                                "status": False,
                                "message": "Can not get parameter: [userName]"
                        }

                if not request.GET.get('password'):
                        return {
                                "status": False,
                                "message": "Can not get parameter: [password]"
                        }

                return {
                        "status": True,
                        "message": {
                                "ip": request.GET.get('ip'),
                                "port": request.GET.get('port'),
                                "userName": request.GET.get('userName'),
                                "password": request.GET.get('password')
                        }
                }
