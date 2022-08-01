#Creating a fuel station for helicopters

import pandas as pd
import random
import datetime

#Creating Client DataFrame
client = []
Client = pd.DataFrame(client, columns=['ID','Model','Company'])

#Lists of Helicopter Companies and Models
List_Companies = ('Agusta','Bell','Airbus')
List_Agusta = ('AW109','AW119')
List_Airbus = ('H125','H130','H135')
List_Bell = ('B505','B407','B429')

#Generating Clients and inserting them to Client DataFrame
for x in range(500):
    ID = random.choice(range(1000,9999))
    Company = random.choice(List_Companies)
    Model = 0
    if Company == 'Agusta':
        Model = random.choice(List_Agusta)
    if Company == 'Airbus':
        Model = random.choice(List_Airbus)
    if Company == 'Bell':
        Model = random.choice(List_Bell)
    Cliente = {'ID':ID,'Model':Model,'Company':Company}
    Client.loc[len(Client)] = [ID,Model,Company]

#Setting ID column as index
#Client = Client.set_index('ID')

#Printing
print('')
print('Client List:')
print(Client)
print('')

#Creating the Station DataFrame
station = ()
Station = pd.DataFrame(station,columns=['ID','Model','Company','Fuel_Filled'])

#Generating the Client frequencies
for x in range(11):
    ID = random.choice(Client['ID'])
    FClient = Client[Client['ID'] == ID]
    Station = pd.concat([Station, FClient], axis=0, ignore_index=True)

    #Creating a probability if the client asked for fuel
    Prob_Fill = random.choice(range(1,10))
    if Prob_Fill <= 3:
        Station.loc[x,'Fuel_Filled'] = 200
    if Prob_Fill > 3:
        Station.loc[x,'Fuel_Filled'] = 0

print(Station)

