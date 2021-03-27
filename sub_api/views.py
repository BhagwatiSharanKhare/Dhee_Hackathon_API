from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class SubjectApiView(APIView):
    def post(self,request):
        data = request.data
        print(data)
        highestEducation = data['highestEducation']
        if(highestEducation == '9th' or highestEducation == '10th'):
            return Response({
            'success':True,
            'result': {
                'subjectChooser' : "That's great!!! Please enter your favourite subject? [[EXT:BUTTON|Maths|Biology|Chemistry|Physics|Computer Science|Economics|English|Geography|History|Civics|Sports]]",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif(highestEducation == '11th' or highestEducation == '12th'):
            return Response({
            'success':True,
            'result': {
                'subjectChooser' : "That's great!!! Please enter your favourite subject? [[EXT:BUTTON|PCM|PCB|Commerce|Arts|Sports]]",
                },
                'resetList' : [],
                'errorMessageKey' : 'Error_Response'
    })
        else:
            return Response({
            'success':True,
            'result': {
                'subjectChooser' : "",
                },
                'resetList' : ["highestEducation"],
                'errorMessageKey' : ''
    })
