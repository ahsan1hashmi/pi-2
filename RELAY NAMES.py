import piplates.RELAYplate as RELAY


x = 1
while x == 1:
    
    relay = str(input())
    if relay == 'MITA_RELAY_1_CMD_ON':
        RELAY.relayON(0,1)
    elif relay == 'MITA_RELAY_1_CMD_OFF':
        RELAY.relayOFF(0,1)

    elif relay == 'MITA_RELAY_2_CMD_ON':
        RELAY.relayON(0,2)
    elif relay == 'MITA_RELAY_2_CMD_OFF':
        RELAY.relayOFF(0,2)
        
    elif relay == 'MITA_RELAY_3_CMD_ON':
        RELAY.relayON(0,3)
    elif relay == 'MITA_RELAY_3_CMD_OFF':
        RELAY.relayOFF(0,3)
        
 
    elif relay == 'MITA_RELAY_4_CMD_ON':
        RELAY.relayON(0,4)
    elif relay == 'MITA_RELAY_4_CMD_OFF':
        RELAY.relayOFF(0,4)
        
    elif relay == 'MITA_RELAY_5_CMD_ON':
        RELAY.relayON(0,5)
    elif relay == 'MITA_RELAY_5_CMD_OFF':
        RELAY.relayOFF(0,5)
        
    elif relay == 'MITA_RELAY_6_CMD_ON':
        RELAY.relayON(0,6)
    elif relay == 'MITA_RELAY_6_CMD_OFF':
        RELAY.relayOFF(0,6)
        
    elif relay == 'MITA_RELAY_7_CMD_ON':
        RELAY.relayON(0,7)
    elif relay == 'MITA_RELAY_7_CMD_OFF':
        RELAY.relayOFF(0,7)