from django.urls import path
from .import views
app_name = 'events'

urlpatterns = [

    path('about-us/', views.about, name='about'),
    path('mission-statement/', views.family, name='family'),
    path('team/', views.team, name='team'),
    path('financial-transparency/', views.financial_transparency, name='financial'),
    path('contact/', views.contact, name='contact'),
    #     path('impact/', views.impact, name='impact'),
    path('faqs/', views.faqs, name='faqs'),
    #     path('media/', views.media, name='media'),
    path('chat-over-coffee/', views.chat_over_coffee, name='chat_over_coffee'),
    path('focal-point/', views.focal_point, name='focal_point'),
    path('forums/', views.forums, name='forums'),
    path('music/', views.music, name='music'),
    path('language/', views.language, name='language'),
    path('alumni/', views.Alumni, name='alumni'),
    path('internships/', views.Internships, name='internship'),
    #     path('donate/', views.donation, name='donate'),
    path('volunteer/', views.Volunteer, name='volunteer'),
    path('impacts/', views.Impact, name='impact'),
    path('success-stories/', views.Success_Stories, name='success-stories'),
    path('nandlal-community/', views.Nandlal_Community, name='Nanadlal_community'),
    path('badabagh-community/', views.Bada_Bagh, name='Bada_Bagh'),
    path('campus-engagement/', views.Campus_Engagement, name='Campus_Engagement'),
    path('awareness-program/', views.Awareness_Program, name='Awareness_Program'),
    path('relief-funds/', views.Relief_Funds, name='Relief_Funds'),
    path('co-curricular-activities/', views.Co_Curricular_Activities,
         name='Co_Curricular_Activities'),
    path('child-sponsorship-program/', views.Child_Sponsorship_Program,
         name='Child_Sponsorship_Program'),
    path('field-visit/', views.Field_Visit, name='Field_Visit'),
    path('blanket-drive/', views.Blanket_Drive, name='Blanket_Drive'),
    path('impacts/', views.Impact, name='impact'),
    path('medical-camp/', views.Medical_Camp, name='Medical_Camp'),








]
