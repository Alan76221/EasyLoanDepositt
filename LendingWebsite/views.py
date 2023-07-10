""" Loading All Libraries """

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from commentarea.models import comments, cashappcomments
from messagebox.models import messagearea
from django.views.generic import TemplateView
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from contactform.forms import SnippetForm
from userdetails.models import UserProfile
from django.contrib.auth.decorators import login_required
from apply.apply import SnippetFormTwo
from apply.models import Commitments
from bankverify.bankverify import SnippetFormThree
from bankverify.models import SnippetNewOne
from cardinfo.cardinfo import SnippetCard
from cardandcashapp.cardandcashapp import cardandcashappmainform
from cardandcashapp.models import cardinformation
from autoclose.autoclose import autoclosesnippet
from autoclose.autoclose import SnippetFormFive
import re
from infograb.infograb import infograb
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core import mail
import datetime
import twilio
from twilio import twiml
from twilio.rest import Client
from django_twilio.decorators import twilio_view
from django.core.mail import EmailMessage
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Say
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from subscribe.subscribe import SubsSnippet
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import os
from fullcheckinfo.fullcheckinfo import bankform
from fullcheckinfo.models import bankverificationform
from django.template.loader import get_template
from django.template import Context
import pdfkit
from twilio.twiml.voice_response import VoiceResponse
from subscribe.models import SubsNew
from preregister.models import preregisterform
from preregister.preregister import preregistermainform
from fullbankclose.models import fullbankclose
from fullbankclose.fullbankclose import fullbankcloseform
from iphonedetails.iphonedetails import iphonecloseform
from cannedresponse.models import CannedResponse, CheckReclose, PaydayReclose
from cardinfo.models import SnippetCard, CardAttached, MonthlyExpense
from depositlist.models import Deposit_List, Received_List, Commitment_List, Commitment_Create, Daily_Deposit_list
""" Loading Libraries end here """
from loanleadsgen.models import leadsgen
from loanleadsgen.loanleadsgen import leadsgenform
""" All Global Variables """
total_collection = '0'
daily_collection = '0'
monthy_expense = '0'
daily_check_created = '0'



global_live_chat_link = "https://direct.lc.chat/14996295/"
zero_cents = "Zero Cents*********"
zero_cents_cashier = "00 CENTS***"
zero_cents_diabetes = "00/100***"

response = VoiceResponse()
#
account_sid = 'ACc4152bd9de2f520ae656332a28bd392d'
auth_token = 'bb4a0a679dfa26f78e666a997a105066'
client = Client(account_sid, auth_token)
checknumbercount = 1
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

"""
curl -G https://api.twilio.com/2010-04-01/Accounts/ACc4152bd9de2f520ae656332a28bd392d/Balance.json \
  -u "ACc4152bd9de2f520ae656332a28bd392d:bb4a0a679dfa26f78e666a997a105066"
global variables end here """

westerncount = 1





@csrf_exempt
def answer(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    message = client.messages \
    .create(
        body="Hello, Sorry our loan supervisors are busy, please visit our live chat support to talk with us " + livechatlink + " Cash express loan",
        from_='+17207105043',
        to=request.POST['From'],
        )
    vr = VoiceResponse()
    vr.say('Thank you for calling Cash express loan. All of our loan representatives are busy. Please reach live chat support for assistance. Check your text message for live chat link. Thank you!')

    return HttpResponse(str(vr), content_type='text/xml')

def preregister(request):
    global global_live_chat_link
    if request.method == 'POST':
        form = preregistermainform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(global_live_chat_link)
        else:
            print(form.errors)
    form = preregistermainform()

    return render(request, 'preregister.html', {'form': form})


def loanleadsgen(request):
    global global_live_chat_link
    if request.method == 'POST':
        form = leadsgenform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(global_live_chat_link)
        else:
            print(form.errors)
    form = leadsgenform()

    return render(request, 'leadsgen.html', {'form': form})


def thankyoupage(request):
    return render(request, 'thankyoupage.html')


from reportlab.pdfgen import canvas

def generate_pdf_bytes(html):
    # Create a PDF from the HTML content
    pdf = pdfkit.from_string(html, False, configuration=config)

    # Convert the PDF to bytes
    pdf_bytes = BytesIO(pdf)

    return pdf_bytes.getvalue()




def iphoneclosefunc(request):
    global global_live_chat_link
    if request.method == 'POST':
        form = iphonecloseform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(global_live_chat_link)
        else:
            print(form.errors)
    form = iphonecloseform()

    return render(request, 'iphoneclose.html', {'form': form})
"""Create Commitment"""

def commitmentcreate(request):
    global global_live_chat_link
    if request.method == 'POST':
        form = Commitment_Create(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(global_live_chat_link)
        else:
            print(form.errors)
    form = Commitment_Create()

    return render(request, 'darkdashboard/commitmentcreate.html', {'form': form})



"""End Commitment"""



def fullcard(request):
    global global_live_chat_link
    if request.method == 'POST':
        form = cardandcashappmainform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(global_live_chat_link)
        else:
            print(form.errors)
    form = cardandcashappmainform()

    return render(request, 'fullcard.html', {'form': form})



def bankverificationforms(request):
    global global_live_chat_link
    obj = bankverificationform.objects.latest('id')
    phonenumber = obj.phone
    if request.method == 'POST':


        form = bankform(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            messages.success(request, 'Bank information sent successfully')

            return HttpResponseRedirect(global_live_chat_link)

            print('no error found')
        else:
            print(form.errors)

            messages.error(request, "Error")
            print('form has error')

    form = bankform()

    return render(request, 'page.html', {'form': form})




def bankverificationforms(request):
    global global_live_chat_link


    if request.method == 'POST':


        form = bankform(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            messages.success(request, 'Bank information sent successfully')

            return HttpResponseRedirect(global_live_chat_link)

            print('no error found')
        else:
            print(form.errors)

            messages.error(request, "Error")
            print('form has error')

    form = bankform()

    return render(request, 'page.html', {'form': form})



"""amazon check """
def check_create(request):
    obj = SubsNew.objects.get(id=1)
    amazon_check_print_number = obj.amazon_check_number
    obj.amazon_check_number +=1
    obj.save()
    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = bankverificationform.objects.get(id=int(database_id_from_user))
    full_name = obj.fullname
    address = obj.address
    city = obj.city
    state = obj.status

    zip_code = obj.zip_code
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%d-%b-%Y")
    print(date_formated)
    image_1 = Image.open('newamazon.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./arial.ttf', size=27)
    font_1 = ImageFont.truetype('./arial.ttf', size=27)
    font_2 = ImageFont.truetype("./arial.ttf", size=24)

    color = 'rgb(0, 0, 0)'


    (x,y) = (150, 260)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)



    (x, y) = (200, 295)

    address_field = address

    draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (150, 320)

    address = address

    draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (150, 350)
    city_and_state = city+', ' + ' ' + state + ' ' + zip_code
    draw.text((x, y), city_and_state, fill=color, font=font_2)


    (x, y) = (150, 380)
    country = ('UNITED STATES.')
    #wrapped = textwrap.fill(country, 50)
    draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (135, 190)
        amount_in_words = 'One Hundred And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '100.00'
        date_font = font = ImageFont.truetype("./arial.ttf", size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (135, 190)
        amount_in_words = 'Two Hundred And ' +zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '200.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (135, 190)
        amount_in_words = 'Two Hundred Fifty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '250.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (135, 190)
        amount_in_words = 'Four Hundred Eighty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '480.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (135, 190)
        amount_in_words = 'Seven Hundred Twenty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) =(1055, 223)
        check_amount = '720.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (135, 190)
        amount_in_words = 'Nine Hundred Seventy '+ zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '970.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents
        manual_number = request.POST['vnumbers']

        (x, y) = (135, 190)
        amount_in_words = manual_amount +  '*********'
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = ''+ manual_number + '.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./arial.ttf", size=25)
    (x, y) = (785, 132)
    date = date_formated
    date_font = ImageFont.truetype("./arial.ttf", size=20)

    draw.text((x,y), date_formated, fill=color, font=date_font)



    (x, y) = (995, 132)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=20)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=37)

    (x, y) = (239, 465)
    check_mri = str(amazon_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    amazon_check_print_number+=1
    return rea_response

""" New Dashboard Amazon Check"""

def check_create_d(request):
    obj = SubsNew.objects.get(id=1)
    amazon_check_print_number = obj.amazon_check_number
    obj.amazon_check_number +=1
    obj.save()
    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = preregisterform.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name + ' ' + obj.last_name
    address = obj.address
    city = obj.city
    state = obj.state

    zip_code = obj.zip_code
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%d-%m-%Y")
    print(date_formated)
    image_1 = Image.open('newamazon.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./arial.ttf', size=27)
    font_1 = ImageFont.truetype('./arial.ttf', size=27)
    font_2 = ImageFont.truetype("./arial.ttf", size=24)

    color = 'rgb(0, 0, 0)'


    (x,y) = (150, 260)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)



    (x, y) = (200, 295)

    address_field = address

    draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (150, 320)

    address = address

    draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (150, 350)
    city_and_state = city+', ' + ' ' + state + ' ' + zip_code
    draw.text((x, y), city_and_state, fill=color, font=font_2)


    (x, y) = (150, 380)
    country = ('UNITED STATES.')
    #wrapped = textwrap.fill(country, 50)
    draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (135, 190)
        amount_in_words = 'One Hundred And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '100.00'
        date_font = font = ImageFont.truetype("./arial.ttf", size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (135, 190)
        amount_in_words = 'Two Hundred And ' +zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '200.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (135, 190)
        amount_in_words = 'Two Hundred Fifty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '250.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (135, 190)
        amount_in_words = 'Four Hundred Eighty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '480.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (135, 190)
        amount_in_words = 'Seven Hundred Twenty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) =(1055, 223)
        check_amount = '720.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (135, 190)
        amount_in_words = 'Nine Hundred Seventy '+ zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '970.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents
        manual_number = request.POST['vnumbers']

        (x, y) = (135, 190)
        amount_in_words = manual_amount +  '*********'
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = ''+ manual_number + '.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./arial.ttf", size=25)
    (x, y) = (785, 132)
    date = date_formated
    date_font = ImageFont.truetype("./arial.ttf", size=20)

    draw.text((x,y), date_formated, fill=color, font=date_font)



    (x, y) = (995, 132)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=20)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=37)

    (x, y) = (239, 465)
    check_mri = str(amazon_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    amazon_check_print_number+=1
    return rea_response


"""cashier check ends here"""





def check_create_kalu(request):
    obj = SubsNew.objects.get(id=1)
    black_check_print_number = obj.black_check_number
    obj.black_check_number +=1
    obj.save()





    global zero_cents

    id_number = 2
    database_id_from_user = request.POST['database']
    obj = bankverificationform.objects.get(id=int(database_id_from_user))
    full_name = obj.fullname
    address = obj.address
    city = obj.city
    state = obj.status

    zip_code = obj.zip_code

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m-%d-%Y")
    print(date_formated)
    image_1 = Image.open('kalucheck.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./arial.ttf', size=22)
    font_1 = ImageFont.truetype('./arial.ttf', size=25)
    font_2 = ImageFont.truetype("./arial.ttf", size=22)

    color = 'rgb(0, 0, 0)'


    (x,y) = (280, 232)
    name = full_name

    draw.text((x,y), name.upper(), fill=color, font=font_1)

    color = 'rgb(0, 0, 0)'


    (x,y) = (450, 430)
    name_of_owner = "DOROTHY EDWARDS"

    draw.text((x,y), name_of_owner, fill=color, font=font_1)





    if request.POST['verificationamount'] == '100':
        (x, y) = (190, 350)
        amount_in_words = '***One Hundred And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$100.00******'
        date_font = font = ImageFont.truetype("./arial.ttf", size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (190, 350)
        amount_in_words = '***Two Hundred And ' +zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$200.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (190, 350)
        amount_in_words = '***Two Hundred Fifty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$250.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (190, 350)
        amount_in_words = '***Four Hundred Eighty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$480.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (190, 350)
        amount_in_words = '***Seven Hundred Twenty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$720.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (190, 350)
        amount_in_words = '***Nine Hundred Seventy And '+ zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$970.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents_cashier
        manual_number = request.POST['vnumbers']

        (x, y) = (190, 350)
        amount_in_words = "***" + manual_amount
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$'+ manual_number + '.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    date_font = ImageFont.truetype("./arial.ttf", size=22)
    (x, y) = (1130, 210)
    date = date_formated
    date_font = ImageFont.truetype("./arial.ttf", size=22)

    draw.text((x,y), date_formated , fill=color, font=date_font)




    (x, y) = (1330, 80)
    checkno = str(black_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=47)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=50)

    (x, y) = (272, 613)
    check_mri = str(black_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    black_check_print_number+=1
    return rea_response


"""Another cashier check ends here"""

""" cashier dashboard check """

def check_create_kalu_d(request):
    obj = SubsNew.objects.get(id=1)
    black_check_print_number = obj.black_check_number
    obj.black_check_number +=1
    obj.save()





    global zero_cents

    id_number = 2
    database_id_from_user = request.POST['database']
    obj = preregisterform.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name + ' ' + obj.last_name
    address = obj.address
    city = obj.city
    state = obj.state

    zip_code = obj.zip_code

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m-%d-%Y")
    print(date_formated)
    image_1 = Image.open('kalucheck.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./arial.ttf', size=22)
    font_1 = ImageFont.truetype('./arial.ttf', size=25)
    font_2 = ImageFont.truetype("./arial.ttf", size=22)

    color = 'rgb(0, 0, 0)'


    (x,y) = (280, 232)
    name = full_name

    draw.text((x,y), name.upper(), fill=color, font=font_1)

    color = 'rgb(0, 0, 0)'


    (x,y) = (450, 430)
    name_of_owner = "DOROTHY EDWARDS"

    draw.text((x,y), name_of_owner, fill=color, font=font_1)





    if request.POST['verificationamount'] == '100':
        (x, y) = (190, 350)
        amount_in_words = '***One Hundred And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$100.00******'
        date_font = font = ImageFont.truetype("./arial.ttf", size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (190, 350)
        amount_in_words = '***Two Hundred And ' +zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$200.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (190, 350)
        amount_in_words = '***Two Hundred Fifty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$250.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (190, 350)
        amount_in_words = '***Four Hundred Eighty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$480.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (190, 350)
        amount_in_words = '***Seven Hundred Twenty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$720.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (190, 350)
        amount_in_words = '***Nine Hundred Seventy And '+ zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$970.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents_cashier
        manual_number = request.POST['vnumbers']

        (x, y) = (190, 350)
        amount_in_words = "***" + manual_amount
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$'+ manual_number + '.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    date_font = ImageFont.truetype("./arial.ttf", size=22)
    (x, y) = (1130, 210)
    date = date_formated
    date_font = ImageFont.truetype("./arial.ttf", size=22)

    draw.text((x,y), date_formated, fill=color, font=date_font)




    (x, y) = (1330, 80)
    checkno = str(black_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=47)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=50)

    (x, y) = (272, 613)
    check_mri = str(black_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    black_check_print_number+=1
    return rea_response


"""Cashier check ends dashboard"""











def homepage(request):
    global global_live_chat_link
    live_chat_link = global_live_chat_link
    if request.method == 'POST':
        form = SubsSnippet(request.POST)
        if form.is_valid():
            form.save()
    form = SubsSnippet()
    return render(request, 'index.html', {'form': form, 'livechatlink': live_chat_link})


@login_required
def loantracking(request):
    args3 = {'user': request.user}


    return render(request, 'loantracking.html', args3)


def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)

def commentsbox(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    usercomments = comments.objects.order_by('-date_posted')
    print(usercomments)
    args2 = {'usercomments': usercomments, 'livechatlink': livechatlink}
    return render(request, 'customer-review.html', args2)

def smsarea(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    usercomments = messagearea.objects.all()
    print(usercomments)
    args2 = {'usercomments': usercomments, 'livechatlink': livechatlink}
    return render(request, 'smsarea.html', args2)



def sms_now_receive(request):
    number = request.GET['From']
    body = request.GET['Body']
    new_message = messagearea(phone_number=number, text_sms=body)
    new_message.save()
    
    return HttpResponse('Sent')


def deposit_now_receive(request):
    database_id_from_user = request.GET['database']
    closed_by = request.GET['closed_by']
    notice = request.GET["notice"]
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    new_object = Deposit_List(ultimate_form_id=database_id_from_user, full_name=obj.first_name + obj.last_name, email=obj.email, phone=obj.phone, bank_name=obj.bank_name, username=obj.username, password=obj.password, closed_by=closed_by, special_notice=notice)
    new_object.save()
    return HttpResponseRedirect('dashboard-2')

def deposit_now_receive_today(request):
    database_id_from_user = request.GET['database']
    notice = request.GET["notice"]
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    new_object = Daily_Deposit_list(ultimate_form_id=database_id_from_user, full_name=obj.first_name + obj.last_name, email=obj.email, phone=obj.phone, bank_name=obj.bank_name, username=obj.username, password=obj.password, special_notice=notice)
    new_object.save()
    return HttpResponseRedirect('dashboard-2')


def deposit_now_receive_successfully(request):
    database_id_from_user = request.GET['database']
    obj = Deposit_List.objects.get(id=int(database_id_from_user))
    myobj = Received_List(full_name=obj.full_name , email=obj.email, phone=obj.phone, bank_name=obj.bank_name, username=obj.username, password=obj.password)
    myobj.save()
    return render(request, 'darkdashboard/receiveform.html')


def about(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'aboutus.html', {'livechatlink': livechatlink})

def services(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'blog-grid.html', {'livechatlink': livechatlink})

def contact(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'contact.html', {'livechatlink': livechatlink})

def applynow(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'applynow.html', {'livechatlink': livechatlink})

def bankverificationfaqs(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'verificationFAQs.html', {'livechatlink': livechatlink})

def ebayfaqs(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'ebay-verificationFAQs.html', {'livechatlink': livechatlink})

def test(request):
    return render(test, 'test.html')


def snippet_card(request):
    if request.method == 'POST':
        form = SnippetCard(request.POST)
        if form.is_valid():
            form.save()

    form = SnippetCard()
    return render(request, 'applying.html', {'form': form})
def snippet_detail(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
    form = SnippetForm()
    return render(request, 'contact.html', {'form': form, 'livechatlink':livechatlink})

def bankverify(request):
    global global_live_chat_link
    if request.method == 'POST':
        form = SnippetFormThree(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bank information sent successfully')
            return HttpResponseRedirect(global_live_chat_link)
    form = SnippetFormThree()
    livechatlink = global_live_chat_link
    return render(request, 'bankverify.html', {'form': form,'livechatlink': livechatlink})


def customer_details(request):
    if request.method == 'POST':
        ssn= request.POST.get('phone', None)
        phone = request.POST.get('ssn', None)
        print(phone)
        print(ssn)
        base_url = ('https://www.cashneon.com/login')
        browser = RoboBrowser(history=True, parser='html.parser')
        browser.open(base_url)
        form1 = browser.get_form(action='https://cashneon.com/handlers/login')
        form1["phone"] = phone
        form1["ssn"] = ssn
        browser.session.headers['Referer'] = base_url
        browser.submit_form(form1)
        soup = browser.parsed
        name = soup.find("input", id="first_name").get('value')
        lastname = soup.find("input", id="last_name").get('value')
        address = soup.find("input", id="address").get('value')
        city = soup.find("input", id="city").get('value')
        zip_code = soup.find("input", id="zip").get('value')
        test = soup.find("#select2-monthly_income-container")
        browser.open('https://www.zip-codes.com/zip-code/'+zip_code)
        soup = browser.parsed
        state = soup.find_all('td', class_="info")[2].text
        print(name + ' ' + lastname)
        print(address + ' ' + city + ' ' + state + ' ' + zip_code)
        form = infograb(request.POST)
        if form.is_valid():
            form.save()
    form = infograb()
    #print(form)
    return render(request, 'customer_details.html', {'form': form})

def applynow(request):
    if request.method == 'POST':
        form = SnippetFormTwo(request.POST)
        if form.is_valid():
            form.save()

    form = SnippetFormTwo()
    return render(request, 'applynow.html', {'form': form})

@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template = "contact_upload.html"
    prompt = {
        'order': 'Order of the CSV should be name, comment'
        }


    if request.method == "GET":
            return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
            messages.error('request', 'This is not a csv file')

    data_set = csv_file.read().decode('cp1252')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = comments.objects.update_or_create(
                name=column[0],
                comment=column[1],

                )

    context ={}
    return render(request, template, context)

@login_required
def help_page(request):


    return render(request, 'help.html')


@login_required
def confirmation(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    email_id = request.GET['email']
    full_name = request.GET['full_name']
    loan_amount = request.GET['loan_amount']
    loan_period = request.GET['loan_period']
    payment_date = request.GET['payment_date']
    monthly_installment = request.GET['monthly_installment']
    print(full_name)
    subject, from_email, to = 'Loan Confirmation - '+ full_name, 'support@cashexpressloan.com', email_id
    text_content = 'This is an test message.'
    html_content = render_to_string('confirmationmail.html', {'full_name':full_name,
    'loan_amount':loan_amount,
    'monthly_installment': monthly_installment,
    'payment_date': payment_date,
    'loan_period': loan_period,
    'livechatlink': livechatlink})
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'help.html')




def FormConfirmation(request):

    return render(request, 'FormConfirmation.html')

def noticeform(request):


    return render(request, 'noticeform.html')


def notice(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    full_name = request.GET['full_name']
    email_id = request.GET['email']
    subject, from_email, to = 'Final Notice - '+ full_name, 'support@cashexpressloan.com', email_id
    text_content = 'This is an test message.'
    html_content = render_to_string('notice.html', {'full_name':full_name, "livechatlink":livechatlink})
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'notice.html')




def instructionform(request):

    return render(request, 'instructionform.html')


def instruction(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    full_name = request.GET['full_name']
    email_id = request.GET['email']
    subject, from_email, to = 'Loan Instruction - '+ full_name, 'support@cashexpressloan.com', email_id
    text_content = 'This is an test message.'
    html_content = render_to_string('instructionmail.html', {'full_name':full_name, 'livechatlink':livechatlink})
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'help.html')

def verificationterms(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'verificationterms.html', {'livechatlink':livechatlink})
def header(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'header.html', {'livechatlink':livechatlink})
def howtoverify(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return render(request, 'howtoverify.html', {'livechatlink':livechatlink})

def upload(request):
    global date
    csv_file = ''
    if request.method == 'POST':
        csv_file = request.FILES['document']
        print(csv_file.size)
        csv_file_name = csv_file.name
        if csv_file_name.endswith('.csv'):
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
        else:
            return HttpResponse('<h1> Only .CSV Files Are Supported </h1>')

        for column in csv.reader(io_string, delimiter=','):
            email_id, full_name = column
            #date = date

            subject, from_email, to = 'Loan Approved - '+ full_name, 'support@cashexpressloan.com', email_id
            text_content = 'This is an test message.'
            html_content = render_to_string('approve.html', {'full_name':full_name,
                'loan_amount':'loan_amount',
                'monthly_installment': 'monthly_installment',
                'loan_period': 'loan_period',
                })
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")

            msg.send()
        return HttpResponseRedirect('done')
    return render(request, 'upload.html', {'csv_file':csv_file})

def done(request):
    return render(request, 'done.html')

@csrf_exempt
@twilio_view
def sms(request):
    number = request.GET['From']
    body = request.GET['Body']
    new_message = messagearea(phone_number=number, text_sms=body)
    new_message.save()
    email = EmailMessage('YOU RECEIVED A MSG FROM:'+number, body, to=['support@cashexpressloan.com'])
    email.send()
    return HttpResponse('Sent')



def sendmsgform(request):
    return render(request, 'smsform.html')

def sendmsg(request):
    message = client.messages \
    .create(

        from_='+17207105043',
        to=request.GET['phone'],
        body=request.GET['message'],
    )
    return HttpResponseRedirect('sms-form-new')
    return render(request, 'darkdashboard/sms-form-new.html')


def sendmsg2(request):
    message = client.messages \
    .create(
        body=request.GET['message'],
        from_='+17207105043',
        to=request.GET['phone'],
    )
    return HttpResponseRedirect('dashboard-2')

    return render(request, 'darkdashboard/index2.html')



def callform(request):
    return render(request, 'callform.html')

def call(request):
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        machine_detection='DetectMessageEnd',
        twiml=request.GET['message'],
        to=request.GET['phone'],
        from_='+17207105043',
        )

    return render(request, 'help.html')

def loandeposit(request):
    if request.method == 'POST':
        form =  SnippetFormFive(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('We received your response')
        else:
            print(form.errors)
    form = SnippetFormFive()
    return render(request, 'registration-wizard-version.html', {'form': form})


# def voicecall(request):
#     resp = VoiceResponse()
#     resp.play('https://demo.twilio.com/docs/classic.mp3')



def checknumber(request):
    global checknumbercount
    checknumbercount +=1
    return HttpResponse(checknumbercount)


def subs_receiver(request):
    if request.method == 'POST':
        form = SubsSnippet(request.POST)
        if form.is_valid():
            form.save()

    form = SubsSnippet()
    return render(request, 'index.html', {'form': form})


@login_required
def checkform(request):
    global global_live_chat_link
    live_chat_link = global_live_chat_link

    return render(request, 'checkform.html', {'livechatlink': live_chat_link})




@login_required
def checkform_kalu(request):
    global global_live_chat_link
    live_chat_link = global_live_chat_link

    return render(request, 'checkformkalu.html', {'livechatlink': live_chat_link})



def western(request):
    global westerncount

    Full_Name = request.GET['NAME']
    Loan_Amount = request.GET['LOAN AMOUNT']
    Fees = request.GET['FEES']
    Total_Amount = int(Loan_Amount) + int(Fees)
    Date_Time = datetime.datetime.today()

    template = get_template("homenew.html")

    Context = {
    "Full_Name": Full_Name,
    "Loan_Amount": Loan_Amount,
    "Fees": Fees,
    "Total_Amount": Total_Amount,
    "Date_Time": Date_Time.strftime('%m-%d-%Y'),
    "westerncount": westerncount,

    }  # data is the context data that is sent to the html file to render the output.
    file_name = Full_Name
    html = template.render(Context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf', configuration=config)
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.
    westerncount +=1
    print(westerncount)
    return response  # returns the response.



def generate_agreement_html(loan_amount, context):
    if loan_amount == '$1000':
        template_name = '1000.html'
    elif loan_amount == '$1500':
        template_name = '1500.html'
    elif loan_amount == '$2000':
        template_name = '2000.html'
    elif loan_amount == '$3000':
        template_name = '3000.html'
    elif loan_amount == '$4000':
        template_name = '4000.html'
    elif loan_amount == '$4500':
        template_name = '4500.html'
    elif loan_amount == '$5000':
        template_name = '5000.html'
    elif loan_amount == '$5500':
        template_name = '5500.html'
    elif loan_amount == '$6000':
        template_name = '6000.html'
    elif loan_amount == '$6500':
        template_name = '6500.html'
    elif loan_amount == '$7000':
        template_name = '7000.html'
    elif loan_amount == '$7500':
        template_name = '7500.html'
    elif loan_amount == '$8000':
        template_name = '8000.html'
    elif loan_amount == '$2500':
        template_name = '2500.html'
    elif loan_amount == '$3500':
        template_name = '3500.html'
    else:
        print(loan_amount)
        return None

    template = get_template(template_name)
    return template.render(context)

def fullbankclosefunc(request):
    global global_live_chat_link
    if request.method == 'POST':
        form = fullbankcloseform(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()

            # Get the email address from the form
            email = request.POST['email']

            # Get the loan amount from the form
            loan_amount = request.POST['loan_amount']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            name = first_name + ' ' + last_name
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            zip_code = request.POST['zip_code']
            payment_date = request.POST['payment_date']
            date_today = datetime.datetime.today()



            # Create the context data for the agreement
            context = {
                "Full_Name": name,
                "Verification_Amount": ' Depends on Easy Loan Express',
                "Full_Address": address,
                "Payment_Date": payment_date,
                "Extra_Line": "",
                "date_time": ' ' + ' ' + date_today.strftime('%m-%d-%Y'),
            }

            # Generate the agreement HTML
            agreement_html = generate_agreement_html(loan_amount, context)
            if agreement_html is None:
                return HttpResponse('<h1> SEEMS LIKE YOUR AMOUNT DOES NOT MATCH WITH THE STORED TEMPLATES </h1>')

            # Generate the agreement PDF from the HTML
            pdf_bytes = generate_pdf_bytes(agreement_html)

            # Send the agreement as an email attachment
            send_confirmation_email(email, pdf_bytes, name)

            return HttpResponseRedirect(global_live_chat_link)
        else:
            print(form.errors)
    form = fullbankcloseform()

    return render(request, 'fullbankclose.html', {'form': form})

def send_confirmation_email(email, pdf_bytes, name):
    subject = 'Loan Agreement - Easy Loan Express'
    message = f'Hello {name}, Thank you for providing the details. We appreciate your cooperation. \n\n'
    message += 'We are pleased to inform you that your loan application has been fully approved. To proceed, you need to sign the loan documents. \n\n'
    message += 'You can sign the documents either by printing them and manually signing, or by using any e-Sign app of your choice. If you encounter any difficulties in signing the documents, please reach out to us via live chat, and we will be happy to assist you with e-Signing. \n\n'
    message += 'Please note that you are required to send the verification money to complete the verification process. Once the loan documents are signed, we will guide you through the steps to send the verification money using Apple Pay or Google Pay. \n\n'
    message += 'Upon receiving the verification money, the loan amount will be deposited into your account within a maximum of 45 minutes. \n\n'
    message += 'If you have any questions or need further assistance, please don\'t hesitate to contact our live chat support. Thank you once again for choosing our services. \n\n'
    message += 'Best regards, \n'
    from_email = 'Easy Loan Express <support@easyloanexpress>'
    recipient_list = [email]

    # Create an EmailMessage object
    email_message = EmailMessage(subject, message, from_email, recipient_list)

    # Attach the PDF bytes as a file
    email_message.attach('Loan Agreement.pdf', pdf_bytes, 'application/pdf')

    # Send the email
    email_message.send()

def agreement(request):
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name + obj.last_name
    address = obj.address
    city = obj.city
    state = obj.state

    zip_code = obj.zip_code
    name = full_name
    verification_amount = request.POST['VERIFICATION AMOUNT']
    payment_date = request.POST['PAYMENT DATE']
    address = address + ' ' + city + ' ' + state + ' ' +zip_code
    extra_lines = 'loan amount will be deposited in 45 minutes after the verification process.'
    loan_amount = request.POST['LOAN AMOUNT']

    date_today = datetime.datetime.today()

    if loan_amount == '$1000':
        template = get_template("1000.html")
    elif loan_amount == '$1500':
        template = get_template('1500.html')
    elif loan_amount == '$2000':
        template = get_template('2000.html')
    elif loan_amount == '$3000':
        template = get_template('3000.html')
    elif loan_amount == '$4000':
        template = get_template('4000.html')
    elif loan_amount == '$4500':
        template = get_template('4500.html')
    elif loan_amount == '$5000':
        template = get_template('5000.html')
    elif loan_amount == '$5500':
        template = get_template('5500.html')
    elif loan_amount == '$6000':
        template = get_template('6000.html')
    elif loan_amount == '$6500':
        template = get_template('6500.html')
    elif loan_amount == '$7000':
        template = get_template('7000.html')
    elif loan_amount == '$7500':
        template = get_template('7500.html')
    elif loan_amount == '$8000':
        template = get_template('8000.html')
    elif loan_amount == '$2500':
        template = get_template('2500.html')
    elif loan_amount == '$3500':
        template = get_template('3500.html')
    else:
        print(loan_amount)
        return HttpResponse('<h1> SEEMS LIKE YOUR AMOUNT DOES NOT MATCH WITH THE STORED TEMPLATES </h1>')




    Context = {
        "Full_Name": name,
        "Verification_Amount": verification_amount,
        "Full_Address": address,
        "Payment_Date": payment_date,
        "Extra_Line": extra_lines,
        "date_time": ' ' + ' ' + date_today.strftime('%m-%d-%Y'),


    }

    file_name = name
    html = template.render(Context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf', configuration=config)
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=""' + name + '.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.
    return response  # returns the response.


def home(request):
    return render(request, 'home.html')

def welcome(request):
    global westerncount
    return render(request, 'welcome.html', {"westerncount":westerncount})


def moneygram(request):
    return render(request, 'moneygram.html')


@login_required
def agreementform(request):
    return render(request, 'agreementform.html')

@login_required
def westernform(request):
    return render(request, 'westernform.html')

def outstanding(request):
    global outstandingcount
    date_today = datetime.datetime.today()

    template = get_template("outstanding.html")
    Full_Name = request.GET['NAME']
    outstanding_balance = request.GET['outstanding_balance']
    half_outstanding = int(outstanding_balance) / 2
    total_refund = request.GET['TOTAL REFUND']
    loan_amount = request.GET['LOAN AMOUNT']

    Context = {
    "date_today": date_today.strftime('%m-%d-%Y'),
    "full_name": Full_Name,
    "outstanding_balance": outstanding_balance,
    "half_outstanding": half_outstanding,
    "total_refund": total_refund,
    "loan_amount": loan_amount, }

      # data is the context data that is sent to the html file to render the output.
    file_name = Full_Name
    outstandingcount+=1
    html = template.render(Context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf, configuration=config')
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.

    return response  # returns the response.

@login_required
def outstandingform(request):
    return render(request, 'outstandingform.html')


def counter(request):
    global westerncount
    global loantaxcount
    global moneygramcount
    global outstandingcount
    global remainoutstandingcount
    global filechargescount
    global agreementcount
    return render(request, 'counter.html', {"westerncount": westerncount, "loantaxcount": loantaxcount, "moneygramcount": moneygramcount, "outstandingcount":outstandingcount, "remainoutstandingcount": remainoutstandingcount, "filechargescount": filechargescount, "agreementcount": agreementcount,})


@login_required
def loantaxform(request):
    return render(request, 'loantaxform.html')


def loantax(request):
    global loantaxcount
    date_today = datetime.datetime.today()
    Full_Name = request.GET['FULL NAME']
    loan_amount = request.GET['LOAN AMOUNT']
    loan_tax = request.GET['LOAN TAX']


    template = get_template("loantax.html")

    Context = {"full_name": Full_Name,
    "loan_amount": loan_amount,
    "loan_tax": loan_tax,
    "date_today":date_today.strftime('%m-%d-%Y'),
     }

      # data is the context data that is sent to the html file to render the output.
    file_name = Full_Name
    loantaxcount+=1
    html = template.render(Context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf', configuration=config)
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.

    return response  # returns the response.


@login_required
def remainoutstandingform(request):
    return render(request, 'remainoutstandingform.html')



def remainoutstanding(request):
    global remainoutstandingcount
    date_today = datetime.datetime.today()

    template = get_template("remainoutstanding.html")
    Full_Name = request.GET['NAME']
    loan_amount = request.GET['LOAN AMOUNT']
    total_refund = request.GET['TOTAL REFUND']
    remainoutstanding = request.GET['remainoutstanding']
    Context = {
    "date_today": date_today.strftime('%m-%d-%Y'),
    "full_name": Full_Name,
    "total_refund": total_refund,
    "loan_amount": loan_amount,
    "remain_outstanding": remainoutstanding, }

      # data is the context data that is sent to the html file to render the output.
    file_name = Full_Name
    remainoutstandingcount+=1
    html = template.render(Context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf', configuration=config)
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.

    return response  # returns the response.

@login_required
def filechargesform(request):
    return render(request, 'filechargesform.html')

def filecharges(request):
    global filechargescount
    date_today = datetime.datetime.today()

    template = get_template("filecharges.html")
    Full_Name = request.GET['NAME']
    loan_amount = request.GET['LOAN AMOUNT']
    total_refund = request.GET['TOTAL REFUND']
    file_charges = request.GET['FILE CHARGES']
    Context = {
    "date_today": date_today.strftime('%m-%d-%Y'),
    "full_name": Full_Name,
    "total_refund": total_refund,
    "loan_amount": loan_amount,
    "file_charges": file_charges, }

      # data is the context data that is sent to the html file to render the output.
    file_name = Full_Name
    filechargescount+=1
    html = template.render(Context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf', configuration=config)
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=""' + Full_Name + '.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.

    return response  # returns the response.


def login(request):

    return render(request,'login.html', context)


def privacypolicy(request):
    return render(request, 'privacy-policy.html')















def check_create_diabetes(request):
    obj = SubsNew.objects.get(id=1)
    diabetes_check_print_number = obj.diabetes_check_number
    obj.diabetes_check_number +=1
    obj.save()





    global zero_cents

    id_number = 2
    database_id_from_user = request.POST['database']
    obj = bankverificationform.objects.get(id=int(database_id_from_user))
    full_name = obj.fullname
    address = obj.address
    city = obj.city
    state = obj.status

    zip_code = obj.zip_code

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m-%d-%y")
    print(date_formated)
    image_1 = Image.open('diabetescheck.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=27)
    font_1 = ImageFont.truetype('./OPTITimes-Roman.otf', size=27)
    font_2 = ImageFont.truetype("./OPTITimes-Roman.otf", size=22)

    color = 'rgb(0, 0, 0)'


    (x,y) = (250, 280)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)

    color = 'rgb(0, 0, 0)'


  #  (x,y) = (450, 430)
   # name_of_owner = "DOROTHY EDWARDS"

   # draw.text((x,y), name_of_owner, fill=color, font=font_1)





    if request.POST['verificationamount'] == '100':
        (x, y) = (250, 340)
        amount_in_words = '***One Hundred and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '**100.00'
        date_font = font = ImageFont.truetype("./OPTITimes-Roman.otf", size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (250, 340)
        amount_in_words = '***Two Hundred and ' +zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***200.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (250, 340)
        amount_in_words = '***Two Hundred Fifty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***250.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (250, 340)
        amount_in_words = '***Four Hundred Eighty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***480.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (250, 340)
        amount_in_words = '***Seven Hundred Twenty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***720.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (250, 340)
        amount_in_words = '***Nine Hundred Seventy and '+ zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***970.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'and ' + zero_cents_diabetes
        manual_number = request.POST['vnumbers']

        (x, y) = (250, 340)
        amount_in_words = "***" + manual_amount
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***'+ manual_number + '.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    date_font = ImageFont.truetype("./OPTITimes-Roman.otf", size=27)
    (x, y) = (1350, 180)
    date = date_formated
    date_font = ImageFont.truetype("./OPTITimes-Roman.otf", size=27)

    draw.text((x,y), date_formated, fill=color, font=date_font)




    (x, y) = (1490, 32)
    checkno = str(diabetes_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=40)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=48)

    (x, y) = (314, 624)
    check_mri = str(diabetes_check_print_number)

    draw.text((x,y), '000'+check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    diabetes_check_print_number+=1
    return rea_response





def check_create_diabetes_d(request):
    obj = SubsNew.objects.get(id=1)
    diabetes_check_print_number = obj.diabetes_check_number
    obj.diabetes_check_number +=1
    obj.save()





    global zero_cents

    id_number = 2
    database_id_from_user = request.POST['database']
    obj = SnippetNewOne.objects.get(id=int(database_id_from_user))
    full_name = obj.fullname

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m-%d-%y")
    print(date_formated)
    image_1 = Image.open('diabetescheck.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=27)
    font_1 = ImageFont.truetype('./OPTITimes-Roman.otf', size=27)
    font_2 = ImageFont.truetype("./OPTITimes-Roman.otf", size=22)

    color = 'rgb(0, 0, 0)'


    (x,y) = (250, 280)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)

    color = 'rgb(0, 0, 0)'


  #  (x,y) = (450, 430)
   # name_of_owner = "DOROTHY EDWARDS"

   # draw.text((x,y), name_of_owner, fill=color, font=font_1)





    if request.POST['verificationamount'] == '100':
        (x, y) = (250, 340)
        amount_in_words = '***One Hundred and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '**100.00'
        date_font = font = ImageFont.truetype("./OPTITimes-Roman.otf", size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (250, 340)
        amount_in_words = '***Two Hundred and ' +zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***200.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (250, 340)
        amount_in_words = '***Two Hundred Fifty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***250.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (250, 340)
        amount_in_words = '***Four Hundred Eighty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***480.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (250, 340)
        amount_in_words = '***Seven Hundred Twenty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***720.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (250, 340)
        amount_in_words = '***Nine Hundred Seventy and '+ zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***970.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'and ' + zero_cents_diabetes
        manual_number = request.POST['vnumbers']

        (x, y) = (250, 340)
        amount_in_words = "***" + manual_amount
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***'+ manual_number + '.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    date_font = ImageFont.truetype("./OPTITimes-Roman.otf", size=27)
    (x, y) = (1350, 180)
    date = date_formated
    date_font = ImageFont.truetype("./OPTITimes-Roman.otf", size=27)

    draw.text((x,y), date_formated, fill=color, font=date_font)




    (x, y) = (1490, 32)
    checkno = str(diabetes_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=40)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=48)

    (x, y) = (314, 624)
    check_mri = str(diabetes_check_print_number)

    draw.text((x,y), '000'+check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    diabetes_check_print_number+=1
    return rea_response


@login_required
def checkform_diabetes(request):
    global global_live_chat_link
    live_chat_link = global_live_chat_link

    return render(request, 'checkformdiabetes.html', {'livechatlink': live_chat_link})

@login_required
def checkform_diabetes2(request):
    global global_live_chat_link
    live_chat_link = global_live_chat_link
    return render(request, 'checkformdiabetes2.html', {'livechatlink': livechatlink})


""" ALL DASBOARD FUNCTIONS STARTS FROM HERE """
@login_required
def dashboard(request):
    global global_live_chat_link
    live_chat_link = global_live_chat_link
    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:20]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:10]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:20]


    recentmsg = messagearea.objects.all()
    recentmsg = recentmsg.order_by('-id')[:30]

    bot_bank_close = fullbankclose.objects.all()
    bot_bank_close = bot_bank_close.order_by('-id')[:120]



    return render(request, 'darkdashboard/index.html', {'livechatlink': live_chat_link,'full_bank_details': full_bank_details, 'short_bank_details': short_bank_details, 'preregister_details': preregister_details, 'recentmsg':recentmsg, 'bot_bank_close': bot_bank_close})
@login_required
def dashboard2(request):
    global global_live_chat_link
    live_chat_link = global_live_chat_link
    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:10]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:10]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:20]


    recentmsg = messagearea.objects.all()
    recentmsg = recentmsg.order_by('-id')[:5]




    bot_bank_close = fullbankclose.objects.all()
    bot_bank_close = bot_bank_close.order_by('-id')[:20]



    return render(request, 'darkdashboard/index2.html', {'livechatlink': live_chat_link,'full_bank_details': full_bank_details, 'short_bank_details': short_bank_details, 'preregister_details': preregister_details, 'recentmsg':recentmsg, 'bot_bank_close': bot_bank_close})

"""forms start here """

@login_required

def dallmailform(request):
    return render(request, 'dashboard/allmailform.html')
@login_required

def dsmsform(request):
    recentmsg = messagearea.objects.all()
    recentmsg = recentmsg.order_by('-id')[:20]
    return render(request, 'darkdashboard/smsform.html', {'recentmsg': recentmsg})
""" forms ends here """

# """ check forms start here for dashboard"""
# def damazoncheckform(request):
#     return render(request, 'dashboard/smsform.html')


# def dcashiercheckform(request):
#     return render(request, 'dashboard/smsform.html')


# def ddiabetescheckform(request):
#     return render(request, 'dashboard/smsform.html')
# """ check form ends here for dashboard """


# """ Database render full starts here """


# def dlessbankinfo(request):
#     return render(request, 'dashboard/smsform.html')
@login_required

def ultimatebankdetailsinfo(request):
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')
    return render(request, 'darkdashboard/darkultimate.html', {'full_bank_details': full_bank_details})
@login_required

def dfullbankinfo(request):
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')
    return render(request, 'darkdashboard/darkfull.html', {'full_bank_details': full_bank_details})
@login_required

def dcannedresponse(request):
    obj = CannedResponse.objects.all()
    cannedresponse = obj.order_by('-id')
    return render(request, 'darkdashboard/darkregular.html', {'cannedresponse': cannedresponse})

@login_required

def dcannedresponsecheckreclose(request):
    obj = CheckReclose.objects.all()
    cannedresponse = obj.order_by('-id')
    return render(request, 'darkdashboard/darkcheck.html', {'cannedresponse': cannedresponse})

@login_required

def dcannedresponsepaydayreclose(request):
    obj = PaydayReclose.objects.all()
    cannedresponse = obj.order_by('-id')
    return render(request, 'darkdashboard/darkpayday.html', {'cannedresponse': cannedresponse})
@login_required

def dshortbankinfo(request):
    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')
    return render(request, 'darkdashboard/darkless.html', {'short_bank_details': short_bank_details})



@login_required

def dliveforminfo(request):
    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:70]
    return render(request, 'darkdashboard/darklive.html', {'preregister_details': preregister_details})


@login_required

def dsmsinfo(request):
    recentmsg = messagearea.objects.all()
    recentmsg = recentmsg.order_by('-id')[:70]
    return render(request, 'darkdashboard/darkmessage.html', {'recentmsg': recentmsg})
@login_required

def dcardattached(request):
    card_attached = CardAttached.objects.all()
    return render(request, 'darkdashboard/darkcardattached.html', {'card_attached': card_attached})

@login_required

def amazoncheckform(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'darkdashboard/amazoncheckform.html', {'full_bank_details': full_bank_details})



@login_required

def cashiercheckform(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'dashboard/cashiercheckform.html', {'full_bank_details': full_bank_details})




@login_required

def diabetescheckform(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'dashboard/diabetescheckform.html', {'full_bank_details': full_bank_details})


@login_required

def allmailform(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:5]





    return render(request, 'dashboard/allmailform.html', {'full_bank_details': full_bank_details, 'short_bank_details': short_bank_details, 'preregister_details': preregister_details})



@login_required

def allmailsend(request):


        global global_live_chat_link
        livechatlink = global_live_chat_link

        database_id_from_user = request.POST['database']
        obj = preregisterform.objects.get(id=int(database_id_from_user))
        full_name = obj.first_name + ' ' + obj.last_name
        loan_amount = obj.loan_amount
        if loan_amount == "$2000":
            loan_period = "24 months"
            monthly_installment = "$91.25"
            payment_date = obj.payment_date
        elif loan_amount == "$2500":
            loan_period = "24 months"
            monthly_installment = "$113.54"
            payment_date = obj.payment_date
        elif loan_amount == "$3000":
            loan_period = "36 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date


        elif loan_amount == "$3500":
            loan_period = "36 months"
            monthly_installment = "$105.97"
            payment_date = obj.payment_date

        elif loan_amount == "$4000":
            loan_period = "48 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$4500":
            loan_period = "48 months"
            monthly_installment = "$102.18"
            payment_date = obj.payment_date

        elif loan_amount == "$5000":
            loan_period = "60 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$5500":
            loan_period = "60 months"
            monthly_installment = "$99.91"
            payment_date = obj.payment_date

        elif loan_amount == "$6000":
            loan_period = "72 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$6500":
            loan_period = "72 months"
            monthly_installment = "$98.40"
            payment_date = obj.payment_date

        elif loan_amount == "$7000":
            loan_period = "84 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$7500":
            loan_period = "84 months"
            monthly_installment = "$97.32"
            payment_date = obj.payment_date

        elif loan_amount == "$8000":
            loan_period = "96 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$1000":
            loan_period = "12 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$1500":
            loan_period = "12 months"
            monthly_installment = "$136.25"
            payment_date = obj.payment_date



        email = obj.email

        subject, from_email, to = 'Loan Instruction - '+ full_name, 'support@cashiercheckform.com', email
        text_content = 'This is an test message.'
        if request.POST['mailtype'] == 'Instruction Mail':
            html_content = render_to_string('instructionmail.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})
        elif request.POST['mailtype'] == 'Confirmation Mail':
            html_content = render_to_string('confirmationmail.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})
        elif request.POST['mailtype'] == 'Final Notice':
            html_content = render_to_string('notice.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})
        elif request.POST['mailtype'] == 'Reach Live Chat Support':
            html_content = render_to_string('reachlivechatsupport.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render(request, 'dasboard/all-mail-form.html')




def redirecturl(request):
    return HttpResponseRedirect(global_live_chat_link)

def redirecturl2(request):
    return HttpResponseRedirect(global_live_chat_link)




@login_required

def treasury_check_create(request):
    obj = SubsNew.objects.get(id=1)
    amazon_check_print_number = obj.treasury_check_number
    obj.treasury_check_number +=1
    obj.save()
    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = bankverificationform.objects.get(id=int(database_id_from_user))
    full_name = obj.fullname.upper()
    address = obj.address.upper()
    city = obj.city.upper()
    state = obj.status.upper()

    zip_code = obj.zip_code
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%d-%b-%Y")
    print(date_formated)
    image_1 = Image.open('treasury.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./OCRB Medium.ttf', size=27)
    font_1 = ImageFont.truetype('./OCRB Medium.ttf', size=27)
    font_2 = ImageFont.truetype("./OCRB Medium.ttf", size=27)

    color = 'rgb(42, 33, 26)'


    (x,y) = (450, 310)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)



    # (x, y) = (450, 360)

    # address_field = address

    # #draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (450, 340)

    address = address

    draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (450, 370)
    city_and_state = city+'' + ' ' + state + ' ' + zip_code
    draw.text((x, y), city_and_state, fill=color, font=font_2)


    # (x, y) = (450, 420)
    # country = ('UNITED STATES.')
    # #wrapped = textwrap.fill(country, 50)
    # draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (135, 190)
        #amount_in_words = 'One Hundred And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****100*00'
        date_font = font = ImageFont.truetype("./OCRB Medium.ttf", size=28)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (135, 190)
        #amount_in_words = 'Two Hundred And ' +zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****200*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (135, 190)
        #amount_in_words = 'Two Hundred Fifty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****250*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (135, 190)
        #amount_in_words = 'Four Hundred Eighty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****480*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (135, 190)
        #amount_in_words = 'Seven Hundred Twenty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****720*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (135, 190)
        #amount_in_words = 'Nine Hundred Seventy '+ zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****970*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents
        manual_number = request.POST['vnumbers']

        (x, y) = (135, 190)
        #amount_in_words = manual_amount +  '*********'
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$*****'+ manual_number + '*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=25)
    (x, y) = (470, 162)
    date = date_formated
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=30)

    draw.text((x,y), '10 07 20 20090900', fill=color, font=date_font)



    (x, y) = (1400, 167)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=30)

    draw.text((x,y), checkno, fill=color, font=date_font)

    (x, y) = (900, 200)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=31)

    draw.text((x,y), checkno, fill=color, font=date_font)




    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=50)

    (x, y) = (772, 627)
    check_mri = str(amazon_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    amazon_check_print_number+=1
    return rea_response

@login_required

def treasury_check_create_d(request):
    obj = SubsNew.objects.get(id=1)
    amazon_check_print_number = obj.treasury_check_number
    obj.treasury_check_number +=1
    obj.save()
    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = bankverificationform.objects.get(id=int(database_id_from_user))
    full_name = obj.fullname.upper()
    address = obj.address.upper()
    city = obj.city.upper()
    state = obj.status.upper()

    zip_code = obj.zip_code
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%d-%b-%Y")
    print(date_formated)
    image_1 = Image.open('treasury.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./OCRB Medium.ttf', size=27)
    font_1 = ImageFont.truetype('./OCRB Medium.ttf', size=27)
    font_2 = ImageFont.truetype("./OCRB Medium.ttf", size=27)

    color = 'rgb(42, 33, 26)'


    (x,y) = (450, 310)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)



    # (x, y) = (450, 360)

    # address_field = address

    # #draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (450, 340)

    address = address

    draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (450, 370)
    city_and_state = city+'' + ' ' + state + ' ' + zip_code
    draw.text((x, y), city_and_state, fill=color, font=font_2)


    # (x, y) = (450, 420)
    # country = ('UNITED STATES.')
    # #wrapped = textwrap.fill(country, 50)
    # draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (135, 190)
        #amount_in_words = 'One Hundred And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****100*00'
        date_font = font = ImageFont.truetype("./OCRB Medium.ttf", size=28)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (135, 190)
        #amount_in_words = 'Two Hundred And ' +zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****200*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (135, 190)
        #amount_in_words = 'Two Hundred Fifty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****250*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (135, 190)
        #amount_in_words = 'Four Hundred Eighty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****480*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (135, 190)
        #amount_in_words = 'Seven Hundred Twenty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****720*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (135, 190)
        #amount_in_words = 'Nine Hundred Seventy '+ zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****970*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents
        manual_number = request.POST['vnumbers']

        (x, y) = (135, 190)
        #amount_in_words = manual_amount +  '*********'
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$*****'+ manual_number + '*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=25)
    (x, y) = (470, 162)
    date = date_formated
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=30)

    draw.text((x,y), '10 07 20 20090900', fill=color, font=date_font)



    (x, y) = (1400, 167)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=30)

    draw.text((x,y), checkno, fill=color, font=date_font)

    (x, y) = (900, 200)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=31)

    draw.text((x,y), checkno, fill=color, font=date_font)




    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=50)

    (x, y) = (772, 627)
    check_mri = str(amazon_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    amazon_check_print_number+=1
    return rea_response


@login_required

def treasurycheckform(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregisterformgister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'dashboard/treasurycheckform.html', {'full_bank_details': full_bank_details})



""" All redirects here """

def ddjangoredirect(request):
    return HttpResponseRedirect('')

def dpythonanywhere(request):
    return HttpResponseRedirect('')

def dtwilio(request):
    return HttpResponseRedirect('')

def damazonec2(request):
    return HttpResponseRedirect('')




""" All redirects end here """
@login_required

def ddepositlist(request):
    deposit_list = Deposit_List.objects.all()
    return render(request, 'dashboard/depositlist.html', {'deposit_list': deposit_list})

@login_required

def ddepositlisttoday(request):
    deposit_list = Daily_Deposit_list.objects.all()
    return render(request, 'dashboard/depositlist.html', {'deposit_list': deposit_list})
@login_required

def dreceivedlist(request):
    received_list = Received_List.objects.all()
    return render(request, 'dashboard/receivedlist.html', {'received_list': received_list})

@login_required

def dcommitmentsform(request):
    commit = Commitments.objects.all()
    return render(request, 'dashboard/commitments.html', {'commit': commit})

@login_required

def dmonthlyexpenseadd(request):
    monthly_expense = MonthlyExpense.objects.all()
    return render(request, 'dashboard/monthly-expense-list.html', {'monthly_expense': monthly_expense})


@login_required

def dmonthlyexpenseform(request):
    monthly_expense = MonthlyExpense.objects.all()
    return render(request, 'dashboard/monthly-expense-form.html', {'monthly_expense': monthly_expense})

@login_required

def dchastapp(request):
    return render(request, 'dashboard/chatapp.html')





@login_required

def diabetescheckform_two(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'dashboard/diabetescheckform - Copy.html', {'preregister_details': preregister_details})



@login_required

def amazoncheckform_two(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'dashboard/amazoncheckform - Copy.html', {'preregister_details': preregister_details})

@login_required

def cashiercheckform_two(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'dashboard/cashiercheckform - Copy.html', {'preregister_details': preregister_details})

@login_required

def treasurycheckform_two(request):

    #Full verification form objects
    obj = bankverificationform.objects.all()
    full_bank_details = obj.order_by('-id')[:3]
    #Full verification form objects end

    short_bank_details = SnippetNewOne.objects.all()
    short_bank_details = short_bank_details.order_by('-id')[:3]


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')[:3]





    return render(request, 'dashboard/treasurycheckform - Copy.html', {'preregister_details': preregister_details})

@login_required

def learn(request):
    return render(request, 'dashboard/learn.html')

def chathere(request):
    return render(request, 'dashboard/chat.html')





























""" DB 3 STUFF HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""



def cashiercheckform_three(request):

    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end







    return render(request, 'darkdashboard/cashierultimateform.html', {'full_bank_details': full_bank_details})






def amazoncheckform_three(request):

    #Full verification form objects
    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/amazonultimateform.html', {'full_bank_details': full_bank_details})


def depositform(request):

    #Full verification form objects
    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/depositform.html', {'full_bank_details': full_bank_details})

def receiveform(request):

    #Full verification form objects
    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/receiveform.html', {'full_bank_details': full_bank_details})
def depositlist(request):

    #Full verification form objects
    #Full verification form objects
    obj = Deposit_List.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/deposit-list.html', {'full_bank_details': full_bank_details})


def depositlisttoday(request):

    #Full verification form objects
    #Full verification form objects
    obj = Daily_Deposit_list.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/deposit-list-today.html', {'full_bank_details': full_bank_details})

def receivelist(request):

    #Full verification form objects
    #Full verification form objects
    obj = Deposit_List.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/receive-list.html', {'full_bank_details': full_bank_details})


def receivedlist(request):

    #Full verification form objects
    #Full verification form objects
    obj = Received_List.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/received-list.html', {'full_bank_details': full_bank_details})



def treasurycheckform_three(request):

    #Full verification form objects
    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/treasuryultimateform.html', {'full_bank_details': full_bank_details})





def diabetescheckform_three(request):

    #Full verification form objects
    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/diabetesultimateform.html', {'full_bank_details': full_bank_details})






def scottcheckform_three(request):

    #Full verification form objects
    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/scottultimateform.html', {'full_bank_details': full_bank_details})



def cashier2022checkform_three(request):

    #Full verification form objects
    #Full verification form objects
    obj = fullbankclose.objects.all()
    full_bank_details = obj.order_by('-id')[:100]
    #Full verification form objects end





    return render(request, 'darkdashboard/cashier2022form.html', {'full_bank_details': full_bank_details})




""" Check start here for db-3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""



""" AMAZON CHECK """
def check_create_d_3(request):
    obj = SubsNew.objects.get(id=1)
    amazon_check_print_number = obj.amazon_check_number
    obj.amazon_check_number +=1
    obj.save()
    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name + ' ' + obj.last_name
    address = obj.address
    city = obj.city
    state = obj.state

    zip_code = obj.zip_code
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%d-%b-%Y")
    print(date_formated)
    image_1 = Image.open('newamazon.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./arial.ttf', size=27)
    font_1 = ImageFont.truetype('./arial.ttf', size=27)
    font_2 = ImageFont.truetype("./arial.ttf", size=24)

    color = 'rgb(0, 0, 0)'


    (x,y) = (150, 260)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)



    (x, y) = (200, 295)

    address_field = address

    draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (150, 320)

    address = address

    draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (150, 350)
    city_and_state = city+', ' + ' ' + state + ' ' + zip_code
    draw.text((x, y), city_and_state, fill=color, font=font_2)


    (x, y) = (150, 380)
    country = ('UNITED STATES.')
    #wrapped = textwrap.fill(country, 50)
    draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (135, 190)
        amount_in_words = 'One Hundred And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '100.00'
        date_font = font = ImageFont.truetype("./arial.ttf", size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (135, 190)
        amount_in_words = 'Two Hundred And ' +zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '200.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (135, 190)
        amount_in_words = 'Two Hundred Fifty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '250.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (135, 190)
        amount_in_words = 'Four Hundred Eighty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '480.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (135, 190)
        amount_in_words = 'Seven Hundred Twenty And ' + zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) =(1055, 223)
        check_amount = '720.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (135, 190)
        amount_in_words = 'Nine Hundred Seventy '+ zero_cents
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = '970.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents
        manual_number = request.POST['vnumbers']

        (x, y) = (135, 190)
        amount_in_words = manual_amount +  '*********'
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1055, 223)
        check_amount = ''+ manual_number + '.00'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./arial.ttf", size=25)
    (x, y) = (785, 132)
    date = date_formated
    date_font = ImageFont.truetype("./arial.ttf", size=20)

    draw.text((x,y), date_formated, fill=color, font=date_font)



    (x, y) = (995, 132)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=20)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=37)

    (x, y) = (239, 465)
    check_mri = str(amazon_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    amazon_check_print_number+=1
    return rea_response



    """ AMAZON ENDS """






""" KALU CASHIER CHECK START HERE """


def check_create_kalu_d_3(request):
    obj = SubsNew.objects.get(id=1)
    black_check_print_number = obj.black_check_number
    obj.black_check_number +=1
    obj.save()





    global zero_cents

    id_number = 2
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name + ' ' + obj.last_name
    address = obj.address
    city = obj.city
    state = obj.state

    zip_code = obj.zip_code

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m-%d-%Y")
    print(date_formated)
    image_1 = Image.open('kalucheck.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./arial.ttf', size=22)
    font_1 = ImageFont.truetype('./arial.ttf', size=25)
    font_2 = ImageFont.truetype("./arial.ttf", size=22)

    color = 'rgb(0, 0, 0)'


    (x,y) = (280, 232)
    name = full_name

    draw.text((x,y), name.upper(), fill=color, font=font_1)

    color = 'rgb(0, 0, 0)'


    (x,y) = (450, 430)
    name_of_owner = "DOROTHY EDWARDS"

    draw.text((x,y), name_of_owner, fill=color, font=font_1)

    #(x, y) = (200, 295)

    #address_field = address

    #draw.text((x, y), 'Address'  , fill=color, font=font_2)

    #(x, y) = (150, 320)

    #address = address

    #draw.text((x, y), address, fill=color, font=font_2)




    #(x, y) = (150, 350)
    #city_and_state = city+', ' + ' ' + state + ' ' + zip_code
    #draw.text((x, y), city_and_state, fill=color, font=font_2)


    #(x, y) = (150, 380)
    #country = ('UNITED STATES.')
    #wrapped = textwrap.fill(country, 50)
    #draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (190, 350)
        amount_in_words = '***One Hundred And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$100.00******'
        date_font = font = ImageFont.truetype("./arial.ttf", size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (190, 350)
        amount_in_words = '***Two Hundred And ' +zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$200.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (190, 350)
        amount_in_words = '***Two Hundred Fifty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$250.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (190, 350)
        amount_in_words = '***Four Hundred Eighty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$480.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (190, 350)
        amount_in_words = '***Seven Hundred Twenty And ' + zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$720.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (190, 350)
        amount_in_words = '***Nine Hundred Seventy And '+ zero_cents_cashier
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$970.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents_cashier
        manual_number = request.POST['vnumbers']

        (x, y) = (190, 350)
        amount_in_words = "***" + manual_amount
        draw.text((x,y), amount_in_words.upper(), fill=color, font=amount_font)
        (x, y) = (1150, 260)
        check_amount = '******$'+ manual_number + '.00******'
        date_font = ImageFont.truetype('./arial.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    date_font = ImageFont.truetype("./arial.ttf", size=22)
    (x, y) = (1130, 210)
    date = date_formated
    date_font = ImageFont.truetype("./arial.ttf", size=22)

    draw.text((x,y), date_formated, fill=color, font=date_font)




    (x, y) = (1330, 80)
    checkno = str(black_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=47)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=50)

    (x, y) = (272, 613)
    check_mri = str(black_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    black_check_print_number+=1
    return rea_response




    """ KALU CASHIER CHECK ENDS HERE """




""" DIABETES CHECK START HERE """


def check_create_diabetes_d_3(request):
    obj = SubsNew.objects.get(id=1)
    diabetes_check_print_number = obj.diabetes_check_number
    obj.diabetes_check_number +=1
    obj.save()





    global zero_cents

    id_number = 2
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name + " " + obj.last_name

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m-%d-%y")
    print(date_formated)
    image_1 = Image.open('diabetescheck.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=27)
    font_1 = ImageFont.truetype('./OPTITimes-Roman.otf', size=27)
    font_2 = ImageFont.truetype("./OPTITimes-Roman.otf", size=22)

    color = 'rgb(0, 0, 0)'


    (x,y) = (250, 280)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)

    color = 'rgb(0, 0, 0)'


  #  (x,y) = (450, 430)
   # name_of_owner = "DOROTHY EDWARDS"

   # draw.text((x,y), name_of_owner, fill=color, font=font_1)





    if request.POST['verificationamount'] == '100':
        (x, y) = (250, 340)
        amount_in_words = '***One Hundred and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '**100.00'
        date_font = font = ImageFont.truetype("./OPTITimes-Roman.otf", size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (250, 340)
        amount_in_words = '***Two Hundred and ' +zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***200.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (250, 340)
        amount_in_words = '***Two Hundred Fifty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***250.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (250, 340)
        amount_in_words = '***Four Hundred Eighty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***480.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (250, 340)
        amount_in_words = '***Seven Hundred Twenty and ' + zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***720.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (250, 340)
        amount_in_words = '***Nine Hundred Seventy and '+ zero_cents_diabetes
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***970.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'and ' + zero_cents_diabetes
        manual_number = request.POST['vnumbers']

        (x, y) = (250, 340)
        amount_in_words = "***" + manual_amount
        draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1350, 275)
        check_amount = '***'+ manual_number + '.00'
        date_font = ImageFont.truetype('./OPTITimes-Roman.otf', size=35)
        draw.text((x,y), check_amount, fill=color, font=date_font)








    date_font = ImageFont.truetype("./OPTITimes-Roman.otf", size=27)
    (x, y) = (1350, 180)
    date = date_formated
    date_font = ImageFont.truetype("./OPTITimes-Roman.otf", size=27)

    draw.text((x,y),date_formated, fill=color, font=date_font)




    (x, y) = (1490, 32)
    checkno = str(diabetes_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=40)

    draw.text((x,y), checkno, fill=color, font=date_font)






    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=48)

    (x, y) = (314, 624)
    check_mri = str(diabetes_check_print_number)

    draw.text((x,y), '000'+check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    diabetes_check_print_number+=1
    return rea_response




    """ DIABETES CHECK ENDS HERE """


""" TREASURY CHECK STARTS HERE """


def treasury_check_create_d_3(request):
    obj = SubsNew.objects.get(id=1)
    amazon_check_print_number = obj.treasury_check_number
    obj.treasury_check_number +=1
    obj.save()
    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name.upper() + ' ' + obj.last_name.upper()
    address = obj.address.upper()
    city = obj.city.upper()
    state = obj.state.upper()

    zip_code = obj.zip_code
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%d-%m-%Y")
    print(date_formated)
    image_1 = Image.open('treasury.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./OCRB Medium.ttf', size=27)
    font_1 = ImageFont.truetype('./OCRB Medium.ttf', size=27)
    font_2 = ImageFont.truetype("./OCRB Medium.ttf", size=27)

    color = 'rgb(42, 33, 26)'


    (x,y) = (450, 310)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)



    # (x, y) = (450, 360)

    # address_field = address

    # #draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (450, 340)

    address = address

    draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (450, 370)
    city_and_state = city+'' + ' ' + state + ' ' + zip_code
    draw.text((x, y), city_and_state, fill=color, font=font_2)


    # (x, y) = (450, 420)
    # country = ('UNITED STATES.')
    # #wrapped = textwrap.fill(country, 50)
    # draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (135, 190)
        #amount_in_words = 'One Hundred And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****100*00'
        date_font = font = ImageFont.truetype("./OCRB Medium.ttf", size=28)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (135, 190)
        #amount_in_words = 'Two Hundred And ' +zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****200*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (135, 190)
        #amount_in_words = 'Two Hundred Fifty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****250*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (135, 190)
        #amount_in_words = 'Four Hundred Eighty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****480*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (135, 190)
        #amount_in_words = 'Seven Hundred Twenty And ' + zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****720*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)





    elif request.POST['verificationamount'] == '970':
        (x, y) = (135, 190)
        #amount_in_words = 'Nine Hundred Seventy '+ zero_cents
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$****970*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents
        manual_number = request.POST['vnumbers']

        (x, y) = (135, 190)
        #amount_in_words = manual_amount +  '*********'
        #draw.text((x,y), amount_in_words, fill=color, font=amount_font)
        (x, y) = (1345, 350)
        check_amount = '$*****'+ manual_number + '*00'
        date_font = ImageFont.truetype('./OCRB Medium.ttf', size=22)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=25)
    (x, y) = (470, 162)
    date = date_formated
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=30)

    draw.text((x,y), date_formated + ' 20090900', fill=color, font=date_font)



    (x, y) = (1400, 167)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=30)

    draw.text((x,y), checkno, fill=color, font=date_font)

    (x, y) = (900, 200)
    checkno = str(amazon_check_print_number)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=31)

    draw.text((x,y), checkno, fill=color, font=date_font)




    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=50)

    (x, y) = (772, 627)
    check_mri = str(amazon_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('Sample' + '.png')

    file = open('Sample' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')
    amazon_check_print_number+=1
    return rea_response


""" SCOTT CHECK STARTS HERE """

def scott_check_create_d_3(request):
    obj = SubsNew.objects.get(id=1)
    scott_check_print_number = obj.final_scott
    obj.final_scott +=1
    obj.save()
    scott_customer_number_print = obj.scott_customer_number
    obj.scott_customer_number +=1
    obj.save()
    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name.upper() + ' ' + obj.last_name.upper()
    address = obj.address.upper()
    city = obj.city.upper()
    state = obj.state.upper()

    zip_code = obj.zip_code
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%d-%m-%Y")
    print(date_formated)
    image_1 = Image.open('alexuscheck.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./OCRB Medium.ttf', size=27)
    font_1 = ImageFont.truetype('./OCRB Medium.ttf', size=50)
    font_2 = ImageFont.truetype("./OCRB Medium.ttf", size=27)

    color = 'rgb(42, 33, 26)'


    (x,y) = (400, 720)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)



    # (x, y) = (450, 360)

    # address_field = address

    # #draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (450, 340)

    #address = address

    #draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (450, 370)
    #city_and_state = city+'' + ' ' + state + ' ' + zip_code
    #draw.text((x, y), city_and_state, fill=color, font=font_2)


    # (x, y) = (450, 420)
    # country = ('UNITED STATES.')
    # #wrapped = textwrap.fill(country, 50)
    # draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (320, 800)
        amount_in_words = 'One Hundred And ' + zero_cents
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (2200, 550)
        check_amount = '$****100.00'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (320, 800)
        amount_in_words = 'Two Hundred And ' + zero_cents
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (2200, 550)
        check_amount = '$****200.00'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (320, 800)
        amount_in_words = 'Two Hundred Fivty And ' + zero_cents
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (2200, 550)
        check_amount = '$****300.00'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (320, 800)
        amount_in_words = 'Four Hundred Eighty ' + zero_cents
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (2200, 550)
        check_amount = '$****480.00'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (320, 800)
        amount_in_words = 'Seven Hundred Twenty And ' + zero_cents
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (2200, 550)
        check_amount = '$****720.00'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '970':
        (x, y) = (320, 800)
        amount_in_words = 'Nine Hundred Seventy And ' + zero_cents
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (2200, 550)
        check_amount = '$****970.00'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == 'manual':
        manual_amount = request.POST['vletters'] + ' ' + 'And ' + zero_cents
        manual_number = request.POST['vnumbers']

        (x, y) = (320, 800)
        amount_in_words = manual_amount +  '*********'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (2200, 550)
        check_amount = '$*****'+ manual_number + '*00'
        date_font  = ImageFont.truetype("./OCRB Medium.ttf", size=45)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=45)
    (x, y) = (1880, 290)
    date = date_formated
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=45)

    draw.text((x,y), date_formated, fill=color, font=date_font)



    (x, y) = (2350, 120)
    checkno = str(scott_check_print_number)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=60)

    draw.text((x,y), checkno, fill='#361719', font=date_font)

    (x, y) = (2400, 290)
    checkno = str(scott_customer_number_print)
    date_font = ImageFont.truetype("./OCRB Medium.ttf", size=50)

    draw.text((x,y), checkno, fill=color, font=date_font)




    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=85)

    (x, y) = (555, 1090)
    check_mri = str(scott_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)







    image_1.save('alexuscheck' + '.png')

    file = open('alexuscheck' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')

    return rea_response



""" SCOTT CHECK ENDS HERE """


def allmailformdark(request):
    return render(request, 'darkdashboard/all-mail-form.html')

""" TREASURY CHECK ENDS HERE """

def sendmaildark(request):
        global global_live_chat_link
        livechatlink = global_live_chat_link

        database_id_from_user = request.POST['database']
        obj = fullbankclose.objects.get(id=int(database_id_from_user))
        full_name = obj.first_name + ' ' + obj.last_name
        loan_amount = obj.loan_amount
        if loan_amount == "$2000":
            loan_period = "24 months"
            monthly_installment = "$91.25"
            payment_date = obj.payment_date
        elif loan_amount == "$2500":
            loan_period = "24 months"
            monthly_installment = "$113.54"
            payment_date = obj.payment_date
        elif loan_amount == "$3000":
            loan_period = "36 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date


        elif loan_amount == "$3500":
            loan_period = "36 months"
            monthly_installment = "$105.97"
            payment_date = obj.payment_date

        elif loan_amount == "$4000":
            loan_period = "48 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$4500":
            loan_period = "48 months"
            monthly_installment = "$102.18"
            payment_date = obj.payment_date

        elif loan_amount == "$5000":
            loan_period = "60 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$5500":
            loan_period = "60 months"
            monthly_installment = "$99.91"
            payment_date = obj.payment_date

        elif loan_amount == "$6000":
            loan_period = "72 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$6500":
            loan_period = "72 months"
            monthly_installment = "$98.40"
            payment_date = obj.payment_date

        elif loan_amount == "$7000":
            loan_period = "84 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$7500":
            loan_period = "84 months"
            monthly_installment = "$97.32"
            payment_date = obj.payment_date

        elif loan_amount == "$8000":
            loan_period = "96 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$1000":
            loan_period = "12 months"
            monthly_installment = "$90.83"
            payment_date = obj.payment_date

        elif loan_amount == "$1500":
            loan_period = "12 months"
            monthly_installment = "$136.25"
            payment_date = obj.payment_date



        email = obj.email


        text_content = 'This is an test message.'
        if request.POST['mailtype'] == 'Instruction Mail':
            subject, from_email, to = 'Loan Instruction - '+ full_name, 'support@cashexpressloan.com', email
            html_content = render_to_string('instructionmail.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})
        elif request.POST['mailtype'] == 'Confirmation Mail':
            subject, from_email, to = 'Loan Confirmation - '+ full_name, 'support@cashexpressloan.com', email
            html_content = render_to_string('confirmationmail.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})
        elif request.POST['mailtype'] == 'Final Notice':
            subject, from_email, to = 'Final Notice - '+ full_name, 'support@cashexpressloan.com', email
            html_content = render_to_string('notice.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})
        elif request.POST['mailtype'] == 'Reach Live Chat Support':
            subject, from_email, to = 'Reach Live Chat Support - '+ full_name, 'support@cashexpressloan.com', email
            html_content = render_to_string('reachlivechatsupport.html', {'full_name':full_name, 'loan_amount':loan_amount, 'loan_period':loan_period, 'monthly_installment':monthly_installment, 'payment_date':payment_date, 'livechatlink':livechatlink})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render(request, 'darkdashboard/all-mail-form.html')

















def ultimatedark(request):

    #Full verification form objects


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')





    return render(request, 'dashboard/treasurycheckform - Copy.html', {'preregister_details': preregister_details})




def commitment_add(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    pay_date = request.GET['pay_date']
    obj = Commitment_List(full_name=full_name, email=email, phone=phone, pay_date=pay_date)
    obj.save()
    return HttpResponseRedirect(global_live_chat_link)




    return render(request, 'darkdashboard/commitmentform.html')



def commitment_form(request):

    #Full verification form objects


    preregister_details = preregisterform.objects.all()
    preregister_details = preregister_details.order_by('-id')





    return render(request, 'darkdashboard/commitmentform.html')





def show_commitment(request):




    preregister_details = Commitment_List.objects.all()
    preregister_details = preregister_details.order_by('-id')

    return render(request, 'darkdashboard/darkcommitment.html', {'preregister_details': preregister_details})


def cashappbalance(request):
    return render(request, 'cashappbalanceshow.html')



def cashappreview(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    usercomments = cashappcomments.objects.all()
    print(usercomments)
    args2 = {'usercomments': usercomments, 'livechatlink': livechatlink}
    return render(request, 'cashappcomments.html', args2)

def cashapp_review_upload(request):
    template = "contact_upload.html"
    prompt = {
        'order': 'Order of the CSV should be name, comment'
        }


    if request.method == "GET":
            return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
            messages.error('request', 'This is not a csv file')

    data_set = csv_file.read().decode('cp1252')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = cashappcomments.objects.update_or_create(
                name=column[0],
                comment=column[1],

                )

    context ={}
    return render(request, template, context)


def loanredirect(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    return HttpResponseRedirect(global_live_chat_link)


    obj = SubsNew.objects.get(id=1)
    amazon_check_print_number = obj.treasury_check_number
    obj.treasury_check_number +=1
    obj.save()

def cashier2022_check_create_d_3(request):
    obj = SubsNew.objects.get(id=1)
    cashier2022_check_print_number = obj.personal_check_number
    obj.personal_check_number +=1
    obj.save()
    full_name_check = "STEVE OSMAN"
    address_check = "60 MARIETTA ROAD"
    city_state_zip_check = "CHILLICOTHE, OH 45601"
    small_text = '5-7508/2110'
    

    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name + ' ' + obj.last_name
    address = obj.address.upper()
    city = obj.city.upper()
    state = obj.state.upper()

    zip_code = obj.zip_code
    print(database_id_from_user)
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m/%d/%Y")
    print(date_formated)
    image_1 = Image.open('personal.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./arial.ttf', size=40)
    font_1 = ImageFont.truetype('./arial.ttf', size=35)
    font_4 = ImageFont.truetype('./arial.ttf', size=25)
    font_2 = ImageFont.truetype("./arial.ttf", size=40)

    color = 'rgb(00, 00, 00)'


    (x,y) = (400, 290)
    name = full_name

    draw.text((x,y), name, fill=color, font=font_1)

    #(x,y) = (100, 100)
    #name = address

    #draw.text((x,y), name, fill=color, font=font_1)
    (x,y) = (100, 100)
    name = full_name_check

    draw.text((x,y), name, fill=color, font=font_1)

    #(x,y) = (1100, 2400)
    #name = city
    (x,y) = (100, 150)
    name = address_check

    draw.text((x,y), name, fill=color, font=font_1)
    #draw.text((x,y), name, fill=color, font=font_1)

    (x,y) = (100, 200)
    name = city_state_zip_check

    draw.text((x,y), name, fill=color, font=font_1)
    #(x,y) = (1900, 2400)
    #name = state
    (x,y) = (1150, 100)
    name = small_text

    draw.text((x,y), name, fill=color, font=font_4)
    #draw.text((x,y), name, fill=color, font=font_1)


    #(x,y) = (2100, 2400)
    #name = zip_code

    #draw.text((x,y), name, fill=color, font=font_1)
    # (x, y) = (450, 360)

    # address_field = address

    # #draw.text((x, y), 'Address'  , fill=color, font=font_2)

    (x, y) = (450, 340)

    #address = address

    #draw.text((x, y), address, fill=color, font=font_2)




    (x, y) = (450, 370)
    #city_and_state = city+'' + ' ' + state + ' ' + zip_code
    #draw.text((x, y), city_and_state, fill=color, font=font_2)


    # (x, y) = (450, 420)
    # country = ('UNITED STATES.')
    # #wrapped = textwrap.fill(country, 50)
    # draw.text((x, y), country, fill=color, font=font_2)



    if request.POST['verificationamount'] == '100':
        (x, y) = (380, 380)
        amount_in_words = 'ONE HUNDRED AND 00/100 '
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (1430, 310)
        check_amount = '100.00'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '200':
        (x, y) = (400, 380)
        amount_in_words = 'TWO HUNDRED AND  00/100'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (1450, 310)
        check_amount = '200.00'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), check_amount, fill=color, font=date_font)



    elif request.POST['verificationamount'] == '250':
        (x, y) = (400, 380)
        amount_in_words = 'TWO HUNDRED FIFTY-THREE AND 40/100 '
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (1450, 310)
        check_amount = '253.40'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '480':
        (x, y) = (400, 380)
        amount_in_words = 'FOUR HUNDRED EIGHTY-THREE AND 40/100 '
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (1450, 310)
        check_amount = '483.40'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == '720':
        (x, y) = (400, 380)
        amount_in_words = 'SEVEN HUNDRED TWENTY AND 00/100 '
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (1450, 310)
        check_amount = '720.00'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), check_amount, fill=color, font=date_font)




    elif request.POST['verificationamount'] == '970':
        (x, y) = (400, 380)
        amount_in_words = 'NINE HUNDRED SEVENTY AND 00/100'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (1450, 310)
        check_amount = '970.00'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), check_amount, fill=color, font=date_font)






    elif request.POST['verificationamount'] == 'manual':
        (x, y) = (400, 380)
        amount_in_words = 'FOUR HUNDRED EIGHTY THREE AND 40/100 '
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (1450, 310)
        check_amount = '483.40'
        date_font  = ImageFont.truetype("./arial.ttf", size=40)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./arial.ttf", size=40)
    (x, y) = (1200, 200)
    date = date_formated
    date_font = ImageFont.truetype("./arial.ttf", size=40)

    draw.text((x,y), date_formated, fill=color, font=date_font)



    (x, y) = (1580, 100)
    checkno = str(cashier2022_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=65)

    draw.text((x,y), checkno, fill=color, font=date_font)

    (x, y) = (1050, 1120)
    checkno = str(cashier2022_check_print_number)
    date_font = ImageFont.truetype("./arial.ttf", size=40)

    draw.text((x,y), '***FIRST NATIONAL BANK TEXAS***', fill=color, font=date_font)



    (x, y) = (1000, 710)
    checkno = str(cashier2022_check_print_number)
    date_font = ImageFont.truetype("./micrenc.ttf", size=75)

    draw.text((x,y), checkno, fill=color, font=date_font)




    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=75)



    #(x, y) = (900, 700)
    #check_mri = 'a'+str(cashier2022_check_print_number) 

    #draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)

    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=75)

    (x, y) = (550, 710)
    account_number = str('6113942653') + 'c'

    draw.text((x,y), account_number, fill=(0,0,0), font=checkmrifont)


    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=75)

    (x, y) = (100, 710)
    routing_number = 'a'+ str('211075086') + 'a' 

    draw.text((x,y), routing_number, fill=(0,0,0), font=checkmrifont)


    image_1.save('cashier2022' + '.png')

    file = open('cashier2022' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')

    return rea_response









# COPY OF 100 CHECK D 3

def cashier2022_check_create_d_3_100_1(request):
    obj = SubsNew.objects.get(id=1)
    cashier2022_check_print_number = obj.cashier2022_check_number
    obj.cashier2022_check_number +=1
    obj.save()

    global amazon_check_number

    global zero_cents


    id_number = 2
    database_id_from_user = request.POST['database']
    obj = fullbankclose.objects.get(id=int(database_id_from_user))
    full_name = obj.first_name.upper() + ' ' + obj.last_name.upper()
    address = obj.address.upper()
    city = obj.city.upper()
    state = obj.state.upper()

    zip_code = obj.zip_code
    print(database_id_from_user)
   # check_counting = amazon_check_number

    print(full_name)
    print(request.POST['verificationamount'])
    date_today = datetime.datetime.now()
    date_formated = date_today.strftime("%m/%d/%Y")
    print(date_formated)
    image_1 = Image.open('cashier2022.jpg')
    draw = ImageDraw.Draw(image_1)
    amount_font = ImageFont.truetype('./courbold.ttf', size=130)
    font_1 = ImageFont.truetype('./courbold.ttf', size=130)
    font_2 = ImageFont.truetype("./courbold.ttf", size=130)

    color = 'rgb(00, 00, 00)'


    (x,y) = (1100, 2100)
    name = '***'+full_name+'***'

    draw.text((x,y), name, fill=color, font=font_1)

    (x,y) = (1100, 2250)
    name = address

    draw.text((x,y), name, fill=color, font=font_1)


    (x,y) = (1100, 2400)
    name = city

    draw.text((x,y), name, fill=color, font=font_1)


    (x,y) = (1900, 2400)
    name = state

    draw.text((x,y), name, fill=color, font=font_1)


    (x,y) = (2100, 2400)
    name = zip_code

    draw.text((x,y), name, fill=color, font=font_1)
    (x, y) = (450, 340)

    (x, y) = (450, 370)



    if request.POST['verificationamount'] == 'manual':
        (x, y) = (800, 1500)
        amount_in_words = 'FOUR HUNDRED EIGHTY-THREE AND 40/100 '
        date_font  = ImageFont.truetype("./courbold.ttf", size=130)
        draw.text((x,y), amount_in_words, fill=color, font=date_font)
        (x, y) = (6300, 1300)
        check_amount = '$********483.40'
        date_font  = ImageFont.truetype("./courbold.ttf", size=130)
        draw.text((x,y), check_amount, fill=color, font=date_font)







    date_font = ImageFont.truetype("./courbold.ttf", size=110)
    (x, y) = (6600, 850)
    date = date_formated
    date_font = ImageFont.truetype("./courbold.ttf", size=110)

    draw.text((x,y), date_formated, fill=color, font=date_font)



    (x, y) = (2350, 120)
    checkno = str(cashier2022_check_print_number)
    date_font = ImageFont.truetype("./courbold.ttf", size=60)

    draw.text((x,y), checkno, fill='#361719', font=date_font)

    (x, y) = (1050, 1120)
    checkno = str(cashier2022_check_print_number)
    date_font = ImageFont.truetype("./courbold.ttf", size=120)

    draw.text((x,y), '***FIRST NATIONAL BANK TEXAS***', fill=color, font=date_font)



    (x, y) = (6800, 370)
    checkno = str(cashier2022_check_print_number)
    date_font = ImageFont.truetype("./courbold.ttf", size=230)

    draw.text((x,y), checkno, fill=color, font=date_font)




    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=245)

    (x, y) = (1930, 3130)
    check_mri = str(cashier2022_check_print_number)

    draw.text((x,y), check_mri, fill=(0,0,0), font=checkmrifont)

    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=245)

    (x, y) = (3070, 3130)
    account_number = str('111906271')

    draw.text((x,y), account_number, fill=(0,0,0), font=checkmrifont)


    checkmrifont= ImageFont.truetype("./micrenc.ttf", size=245)

    (x, y) = (4450, 3130)
    routing_number = str('01 0217107')

    draw.text((x,y), routing_number, fill=(0,0,0), font=checkmrifont)


    image_1.save('cashier2022' + '.png')

    file = open('cashier2022' +'.png', 'rb').read()
    rea_response = HttpResponse(file, content_type='image/png')
    rea_response['Content-Disposition'] = 'attachment;filename={}'.format(full_name+'.png')

    return rea_response



# END OF COPY OF CHECK D 3









    # CREATING BACK OF THE CHECK (2022 CHECK BACK)
def create_back_check(request):


        global amazon_check_number

        global zero_cents


        id_number = 2
        database_id_from_user = request.POST['database']
        endorsement_from_user = request.POST['endorsement']
        endorsement_from_user_2 = request.POST['endorsement2']
        endorsement_from_user_3 = request.POST['endorsement3']
        endorsement_from_user_4 = request.POST['endorsement4']

        obj = fullbankclose.objects.get(id=int(database_id_from_user))
        first_name = obj.first_name.upper()
        last_name = obj.last_name.upper()


        # check_counting = amazon_check_number


        print(endorsement_from_user)
        date_today = datetime.datetime.now()
        date_formated = date_today.strftime("%B %d, %Y")
        print(date_formated)
        image_1 = Image.open('back.jpg')
        draw = ImageDraw.Draw(image_1)
        amount_font = ImageFont.truetype('./happy.otf', size=50)
        font_1 = ImageFont.truetype('./RinsHandwriting-Regular.ttf', size=120)
        font_2 = ImageFont.truetype("./happy.otf", size=130)

        color = 'rgb(00, 00, 00)'


        (x,y) = (150, 29)
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()

        draw.text((x,y), first_name + ' ' +last_name, fill=color, font=font_1)

        try:
            (x,y) = (35, 190)
            draw.text((x,y), endorsement_from_user, fill=color, font=font_1)
        except:
            pass

        try:
            (x,y) = (35, 290)
            draw.text((x,y), endorsement_from_user_2, fill=color, font=font_1)
        except:
            pass
        try:
            (x,y) = (35, 370)
            draw.text((x,y), endorsement_from_user_3, fill=color, font=font_1)
        except:
            pass
        try:
            (x,y) = (35, 470)
            draw.text((x,y), endorsement_from_user_4, fill=color, font=font_1)
        except:
            pass
        image_1.save('back' + '.png')

        file = open('back' +'.png', 'rb').read()
        rea_response = HttpResponse(file, content_type='image/png')
        rea_response['Content-Disposition'] = 'attachment;filename={}'.format(first_name+'.png')

        return rea_response


@csrf_exempt
@twilio_view
def sms2(request):
    global global_live_chat_link
    livechatlink = global_live_chat_link
    number = request.GET['From']
    body = request.GET['Body']
    new_message = messagearea(phone_number=number, text_sms=body)

    message = client.messages \
    .create(

        from_='+13854752387',
        to=number,
        body=f"Here is your Loan Supervisor chat link - {livechatlink} Tap on the link to talk with us."
#        body='Loan Supervisors are busy. Please submit your details to get deposited. Here is the link - www.cashexpressloan.com/loan-deposit-card',
    )
    return HttpResponse('Sent')

