# -*- coding: utf-8 -*-
"""ChatBot_py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UanYrqD1ZgN20bOkIKJXUX4MKH2wf96l
"""

import time
now = time.ctime()

import time
now = time.ctime()

#question/answer

qna ={
    "Hi":"Hey",
    "hi":"Hi",
    "Hey":"Hey",
    "Hello":"Yeah,hello",
    "Hlw":"Hey,you shortform!",
    "How are you":"I'm fine, What about you?",
    "Who are you":"I'm BotDengue 0.1.",
    "What is your name":"My name is BotDengue 0.1.",
    "What time now": now,
    "Is dengue contagious from person to person?": "No, dengue is not contagious and cannot be spread merely by person to person contact. The dengue virus is carried and transmitted by mosquitoes.",
    "Can I be infected with dengue a second or more times?": "Yes. Dengue is caused by four different viral strains and infection with one virus does not protect a person against infection from the other three strains.",
    "Can I be infected with dengue a second or more times?":"Yes. Dengue is caused by four different viral strains and infection with one virus does not protect a person against infection from the other three strains.",
    "What kinds of mosquito repellents are safe?":"It is safe to use a repellent that has DEET (diethyltoluamide or diethylmethylbenzamide) or picaridin.",
    "Where do most outbreaks of dengue occur?":"Outbreaks of dengue occur primarily in areas where Aedes aegypti mosquitoes breed and thrive, i.e., mostly in tropical and sub-tropical areas of the world.",
    "Can one treat dengue with antibiotics?":"No, since dengue is caused by a virus, antibiotics are not effective against it and should not be used.",
    "Is dengue a deadly disease?":"Although dengue fever is a serious and often painful condition, it is not a deadly disease and does not lead to death.",
    "Which type of doctor should one consult for dengue fever?":"Consult a physician or an infectious disease doctor.",
    "If I have had dengue fever, can I get it again?":"Yes, a single attack of dengue fever only protects the person against the particular virus serotype.",
    "What can be done to reduce the risk of acquiring dengue?":"Reducing stagnant water bodies that are the main breeding centers for the female Aedes mosquitoes to lay their eggs reduces the risk of acquiring dengue.",

}

#Condition
while True:
  qs = input("You: ")

  if (qs =="exit"):
    break
  else:
    print("Bot:",qna[qs])

