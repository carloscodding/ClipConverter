import os 

import subprocess

import ffmpeg 

from tqdm import tqdm 

import time 

print("Bem Vindo Ao ClipConverter")

print("Script: CarlosCodding")

print("===============================")

try:
  os.mkdir("input")
  os.mkdir("output")

except:
  
  for x in os.listdir("input"):
    
    if ".mp4" in x:
      
      subprocess.run("ffmpeg"," -i ","input//",x," output//",x.replace(".mp4",".mp3"))
      
      for i in tqdm(range(100)):
        
        time.sleep(0.1)
        
      print('{} Convertido Com Sucesso'.format(x.replace(".mp4",".mp3")))
      
    else:
      
      print("Não Existe Nenhum MP4 Na Pasta Input Por Favor Coloque E Tente Novamente")
      
      exit()
      
  
  
  
  
