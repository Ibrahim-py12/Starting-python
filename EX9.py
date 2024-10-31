#Shout outs using python 

import win32com.client
winners  = ["Ali , Ahmed , Rehan"]
first  =["ibrahim"]



speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("The top scorrers are")
for i in winners:
    
    print (i)
    # speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(i)
a=first[0]
print(a) 
speaker.Speak("and the first place belongs to " )
speaker.Speak(a)