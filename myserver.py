import RemoteControlServer as RCS
import win32api

current = win32api.GetCursorPos()
cx =  current[0]
cy =  current[1]

# sonksiyon tanımla
def tikla():

    win32api.SetCursorPos((cx,cy))
    return current

def sol():

    win32api.SetCursorPos((cx-10,cy))

def sag():

    win32api.SetCursorPos((cx+10,cy))

def yukari():

    win32api.SetCursorPos((cx,cy+10))

def asagi():

    win32api.SetCursorPos((cx,cy-10))

# bton ekle
 
butDef = RCS.ButtonsDefinition()
butDef.addButton("Yukar�", yukari)
butDef.addButton("A�a��", asagi)
butDef.addButton("Sa�a", sag)
butDef.addButton("Sola", sol)
butDef.addButton("T�kla", tikla)



server = RCS.Server(butDef)

# server
print ('Running server')
server.run()
