# -*- coding: utf-8 -*-
import random, string

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