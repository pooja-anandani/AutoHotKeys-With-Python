


import subprocess,time,psutil,keyboard
#loop this up if you have more than one file 
filename= #autohot key file you want to read 
#i.e. (abc.ahk)
proc=subprocess.Popen([r"C:\Program Files\AutoHotkey\AutoHotkey.exe",filename ])
time.sleep(5)
keyboard.send('ctrl+]')
keyboard.write('quit\n')
keyboard.write('exit\n')
output_file=#filename that you want your file to be written to 

#if you want to store the data into the database better way is to store the data in dataframe and ingest directly into the database.
               
               
               
               
               
               
               
               
               
               
               
               
               
               
   