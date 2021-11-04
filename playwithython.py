Microsoft Windows [Version 10.0.19043.1288]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Iklus>python
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>>
>>> # Verander <JOUW NAAM HIER> in je eigen naam
>>> print('Mijn naam is <JOUW NAAM HIER>')
Mijn naam is <JOUW NAAM HIER>
>>> naam = '<JOUW NAAM HIER>'
>>> print(naam)
<JOUW NAAM HIER>
>>> print(naam.upper())
<JOUW NAAM HIER>
>>> print(naam[0:2])
<J
>>> print(naam[::-1])
>REIH MAAN WUOJ<
>>>
>>> # Verander dit in je eigen leeftijd
>>> leeftijd = 15
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo <JOUW NAAM HIER> ben je al 15 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> leeftijd-=1
>>> leeftijd
15
>>>
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
...     # Let op: hier 2x een enter doen!
...
Over 3 jaar wordt je 18
>>> # Willekeurige getallen genereren
>>> from random import randint
>>> randint(0,1000)
809
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
547
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 547
>>>
>>> # Datum en tijd
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-11-04 11:31:23.136140
>>> datum.strftime('%A %d %B %Y')
'Thursday 04 November 2021'
>>>
>>> # Nu in een andere taal
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'donderdag 04 november 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'giovedì 04 novembre 2021'
>>>
>>>