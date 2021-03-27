from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class CategoryApiView(APIView):
    def post(self,request):
        data = request.data
        print(data)
        category = data['category']
        if category == 'Maths':
            return Response({
            'success':True,
            'result': {
                'category' : "Nice.Here are some courses you can choose in this stream. Select the one which appeals to you the most.  [[EXT:BUTTON|Engineering|Architecture|Aviation|Physics|Merchant Navy|National Defence|Ethical Hecking|Forensic Science|Computer Application & IT|Research and Teaching]]",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
    #     elif :
    #         return Response({
    #         'success':True,
    #         'result': {
    #             'subjectChooser' : "That's great!!! Please enter your favourite subject? [[EXT:BUTTON|PCM|PCB|Commerce|Arts|Sports]]",
    #             },
    #             'resetList' : [],
    #             'errorMessageKey' : 'Error_Response'
    # })
        else:
            return Response({
            'success':True,
            'result': {
                'category' : "",
                },
                'resetList' : ["category"],
                'errorMessageKey' : 'Apologies, We are not able to fetch the desired result'
    })


class subCategoryApiView(APIView):
    def post(self,request):
        data = request.data
        print(data)
        subcategory = data['subcategory']
        print(subcategory)
        if subcategory == 'Engineering':
            print(subcategory)
            return Response({
            'success':True,
            'result': {
                'subcategory' : "Engineering is the most popular career option amongst PCM students. To become an engineer a student needs to pursue B.Tech/B.E. degree. There are many colleges offering B.tech degree. The most renowned and popular institute is Indian Institute of Technology. \nTo get this degree you need to give entrance exams like – IIT JEE Mains & Advanced, BITSAT, etc.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif subcategory == 'Architecture':
            return Response({
            'success':True,
            'result': {
                'subcategory' : "Architecture is the second most popular career option for Mathematics students. The degree required to become an architect is B.Arch. There are multiple colleges that offer this degree like IITs, NITs, CEPT, etc. You can opt for a career in Interior Design, Industrial Design, Urban Design, Landscape Architecture, etc. \nThe required entrance exams are NATA, AAT, etc.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif subcategory == 'Aviation':
            return Response({
            'success':True,
            'result': {
                'subcategory': "If you want to become a commercial pilot, then aviation is the right option for you. Other option like Aircraft Maintenance Engineer is also a good scope when you get into aviation. There are many aviation institutes in India that offer aviation-related degree & training.\nPilot Aptitude Test (WOMBAT) is a way to get into this field.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif subcategory == 'Merchant Navy':
            return Response({
            'success':True,
            'result': {
                'subcategory': "International trade, cargo, if these terms get your attention then the merchant navy is perfect for you. This is one of the most exciting fields for mathematics graduates. You can work in various departments of a merchant ship, like, deck, architecture, the engine, catering, etc. Colleges like Indian Maritime University, International Maritime Institute, International Maritime Academy, etc, provide degrees like HND, Marine Engineering, Bachelor of Science in Nautical Technology, etc. Required entrance exam - AIMNET.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })

        elif subcategory == 'National Defence':
            return Response({
            'success':True,
            'result': {
                'subcategory': "If you want to be a part of the Indian Navy, Indian Air Force, Indian Army, then you can opt for this option. National Defence Academy conducts an NDA exam that offers admission to a fulltime residential undergraduate program, where cadets are given a bachelor’s degree in various fields.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif subcategory == 'Ethical Hacking':
            return Response({
            'success':True,
            'result': {
                'subcategory': "Ethical hacking is gaining popularity amongst students these days. Ethical Hackers are responsible to check the security of the computer system and find fault in defence systems. They are responsible for the network security of a company or institute from cyber-attacks. You can pursure various career options like Security Consultant, Network Security Administrator, Network Security Engineer, Penetration Tester. To get into this career you will require certain certifications like Indian School of Ethical Hacking (ISOEH), Ankit Fadia Certified Ethical Hacker, NIIT Ethical Hacking, etc.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif subcategory == 'Forensic Science':
            return Response({
            'success':True,
            'result': {
                'subcategory': "Do you like investigating? Then this new field of Forensic science is the option for you. It is an applied field that requires knowledge of various science-related streams. You can become a Crime Scene Investigator, Forensic Ballistics Expert, Forensic Scientist, Digital Forensics Expert, etc.\n\n There are multiple institutes that offer a degree in forensic science (*mostly at PG level).",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif subcategory == 'Computer Application & IT':
            return Response({
            'success':True,
            'result': {
                'subcategory': "This field has multiple opportunities for students who have an interest in computers. Career options like Software Developer, System Analyst, Web Designer, App Developer, Network Administrator, Database Administrator, etc. The degree required for this career option are B.E./B.Tech in Computer Application & Information technology, BSIT or BCA.\n\nThere are multiple colleges and institutes that offer these courses and conduct entrance exam for admission into them.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif subcategory == 'Research and Teaching':
            return Response({
            'success':True,
            'result': {
                'subcategory': "You can also pursue a career in research and teaching field. After completing your bachelor’s degree, you will require a master’s degree for this option. There are many national level exams you can give to get into master’s courses like CSIR NET, IIT JAM. You can also go for Doctoral courses after your post-graduation.",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })



        else:
            return Response({
            'success':True,
            'result': {
                'subcategory' : "",
                },
                'resetList' : ["subcategory"],
                'errorMessageKey' : 'Apologies, We are not able to fetch the desired result'
    })