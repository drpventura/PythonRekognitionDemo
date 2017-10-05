import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

# imgurl = 'http://media.comicbook.com/uploads1/2015/07/fox-comic-con-panel-144933.jpg'
imgurl = 'https://blog.njsnet.co/content/images/2017/02/trumprecognition.png'

imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.detect_faces(Image={'Bytes': imgbytes},
                              Attributes=['ALL'])

# pprint(rekresp)

numfaces = len(rekresp['FaceDetails'])
print('Found', numfaces, end='')
if numfaces == 1:
    print(' face:')
else:
    print(' faces:')

for facedeets in rekresp['FaceDetails']:

    # construct a printf (almost) style format string for printing the info
    fmtstr = '{gender} age {lowage}-{highage},'

    # mustache and beard detection
    if facedeets['Mustache']['Value'] and facedeets['Beard']['Value']:
        fmtstr += ' with beard and mustache,'
    elif facedeets['Mustache']['Value']:
        fmtstr += ' with mustache,'
    elif facedeets['Beard']['Value']:
        fmtstr += ' with beard,'

    # sunglasses/eyeglasses detection
    if facedeets['Sunglasses']['Value']:
        fmtstr += ' wearing sunglasses,'
    elif facedeets['Eyeglasses']['Value']:
        fmtstr += ' wearing glasses,'

    fmtstr += ' looks {emotion}'

    print(
        fmtstr.format(
            gender=facedeets['Gender']['Value'],
            lowage=facedeets['AgeRange']['Low'],
            highage=facedeets['AgeRange']['High'],
            emotion=facedeets['Emotions'][0]['Type'].lower()
        )
    )


