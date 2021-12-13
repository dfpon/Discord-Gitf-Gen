# -*- coding: utf-8 -*-
import random, string

"""
                                                                                                                                                                                                                                                                                                                                                                        
        ......                                                              .J.   .(JJ         .,        .kWm,     .J.             ..  ..     .....       .....       .....      .....    (#
      .dM#"YHMN,                               dN_                          d#{  .M#=!        .M> dHkQQNMMm.d\    .d@`            .MC .d@   .gMB"YMNe   .NMB"WMN,   (M#""MMe   .dMB"WMm.  (#
     (MB`    .MM< .(,.(+.  .(+J,.    ..J+-,  .(dNg-.  ..J+J,     .    ..J+-.d#{ .+Mm(,        J#  `    dD -~`     (M!           ..dN&.(Me.. dM\    7"`  T5`   (MP  ,M@    dN}  dM>   (M#  (#
     dM\          .MM@"?`.MM=?7MN,  dMY<?TMb  ?MN=!` .MB=?TMm.  dMt  .MM"?7HM#{ ?OM8?!        d$  dHHHHM#WY=     (M%..          7TM@"7MMY7!.Mb(gNNNx.     ....M#'        .M@` .M#`    dN{ (#
     MN_          .M@    dNa....Mb.  .....M#_  dN~  .MN....(Mr   `   dM~   .M#{  (M$          M\       dP       .dN#9TN-    .    (#{ .MF   ,MMD!  ?MN.    ?""WNm,      .jMD`  (Mb     JN\ (#
     dM[      ... .MP   .M#Y777777 .dM9"77M#_  dN~  (M#777777^       MN.    d#{  (M$          Mn#{.(gmgMb.      dM=  .H)   .M\ dMMMMMMMMMt ,M#!    JMt  ..     MN.   .(M@!    .MN_   .d#! (#
     .HNe....(M#` .MP    ?Mm....g[ ,Mb...(M#_  dNe.  WNe...(g>  .J,  vMm...JM#{  (M$    -J.   MMD dD`  d#TNe   (#\   .ML  .MD   .M% .d@     ?Mm...-M#! .MN,...(M#   .MMl.....  ?Mm, .uM$  (#
       ?TMMMMB=   .M$     (TMMMB=   ?TMMB=TE`  .TMM>  ?TMMM9^   7M\   (TMMB"7B!  (Mt    TB'   dM` (TMpMB!  ~  .MD     ?TMH9'    ?B` .M>      (TMMMH=`    7WMMMB=   .MMMMMMMM%   (TMMMB^   (#
"""


def createNitro():
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(16)]
    return ''.join(randlst)

print('---NitroGenerator---')
print('create:df.ぽん#6320:DiscordTag')
print('--------------------')

num = int(input('NitroGen : How many times do you try?'))

print('NitroGen : Run {} times. Please wait until the preparation is completed.'.format(num))
import time,requests

time.sleep(2)

print('NitroGen : All ready.')

for i in range(num):
    id_ = createNitro()
    url = ('https://discordapp.com/api/v6/entitlements/gift-codes/{0}?with_application=false&with_subscription_plan=true'.format(id_))
    r = requests.get(url)
    if r.status_code == 200:
        print('Success : https://discord.gift/{}'.format(id_))
        print('NitroGen : Found a usable Nitro.')
        break
    else:
        print('Failure : https://discord.gift/{}'.format(id_))

print('NitroGen : Press any key to exit.')
