import RemoteControlServer as RCS
import win32api

current = win32api.GetCursorPos()
cx =  current[0]
cy =  current[1]

# sonksiyon tanÄ±mla
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
butDef.addButton("Yukarý", yukari)
butDef.addButton("Aþaðý", asagi)
butDef.addButton("Saða", sag)
butDef.addButton("Sola", sol)
butDef.addButton("Týkla", tikla)



server = RCS.Server(butDef)

# server
print ('Running server')
server.run()
