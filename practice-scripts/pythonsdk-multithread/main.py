import sys
from splitio import get_factory
from splitio.exceptions import TimeoutException

from splitio_toolbox import *
import time

def randomizeMap():


print("Welcome to my testing script!")
print("We are running on: " + sys.version)

#test parameters
numberOfPasses = 2
key = 'agus'
randomizeKey = True
sleeptime = 1
splitName = 'split_integration_demo'

#factory and client init
factory = get_factory('97brq63mkf3drbop3f5tdp1ar24gpjtj7b28')
try:
    factory.block_until_ready(5) # wait up to 5 seconds
    print("Factory is ready!")
except TimeoutException:
    # Now the user can choose whether to abort the whole execution, or just keep going
    # without a ready client, which if configured properly, should become ready at some point.
    print("We timed out :(")
    pass
splitclient = factory.client()

#get treatment calls and event tracking
for i in range(numberOfPasses):
    if randomizeKey:
        key = randomAlphanumKey(10)
    print('Got ' + splitName + ' treatment for ' + key + ' : ' + splitclient.get_treatment(key,splitName))
    time.sleep(sleeptime)

print('Destroying client...')
splitclient.destroy()
print('Done. Exiting...')