#Imports
import pysrt
import pydeepl

import sys  

reload(sys)  

sys.setdefaultencoding('utf8')


def load_file(loc):

  try:

      subtitles = pysrt.open(loc,encoding='iso-8859-1')
      return subtitles
 
  except Exception as e:
    
      print("The location you have provided seems to be wrong. Try providing the full(and correct!) location")
      sys.exit(0)


def rep(to_rep):
    
    to_rep = to_rep.replace(".",".||;")
    
    to_rep = to_rep.replace("?","?||;")
    
    to_rep = to_rep.replace("!","!||;")

    
    return to_rep



def change_lang(to_translate,to_language,from_language):
  
  try:  
      
      return pydeepl.translate(to_translate,to_language,from_lang=from_language)
  
  except Exception as e:
      
      s = to_translate.split("\n")
      
      s1 = ""
      
      
      for i in s:
      
          s1 = s1 + pydeepl.translate(i,to_language,from_lang=from_language)+"\n"
      
      return s1




def save(subtitles):

    try:
     
        subtitles.save(sys.argv[4],encoding='utf-8')
    
    except:

        if sys.argv[1].find("/") != -1:
      
            name = sys.argv[1][sys.argv[1].rfind("/")+1:sys.argv[1].rfind(".")]
      
            subtitles.save(name+"-"+sys.argv[3]+".srt",encoding='utf-8')
      
        elif sys.argv[1].find("\\") != -1:
            
            name = sys.argv[1][sys.argv[1].rfind("\\")+1:sys.argv[1].rfind(".")]
            
            subtitles.save(name+"-"+sys.argv[3]+".srt",encoding='utf-8')
       
        else:
           
            name = sys.argv[1][:sys.argv[1].rfind(".")]
           
            subtitles.save(name+"-"+sys.argv[3]+".srt",encoding='utf-8') 
 



def translator(location,from_lang,to_lang):
  
  subs = load_file(location)  
  
  from_language = from_lang
 
  to_language = to_lang
  
  length = len(subs)

  
  for i in range(length-1):
  
     print("Line "+str(i))

     text = subs[i].text.encode("utf-8")
     
     text = rep(text)

     arr = text.split("||;")
     
     arr1 = arr
     
     if(len(arr)!=1):
       
         arr = arr[0:len(arr)-1]
     
     x = -1
     
     try:
       
       if arr[x][x]!="." and arr[x][x]!="?" and arr[x][x]!="!" and len(arr)!=1 : 
          to_translate = " ".join(arr[0:len(arr)-2])
     
          subs[i+1].text = arr[-1]+" "+subs[i+1].text
     
       else:
          
          to_translate = " ".join(arr)
     
     except IndexError:
          
          print("index \n")
          
          print(arr1)
                  
          if arr[x][x]!="." and arr[x][x]!="?" and arr[x][x]!="!": 
            
            to_translate = " ".join(arr[0:len(arr)-2])
     
            subs[i+1].text = arr[-1]+" "+subs[i+1].text
     
          else:
          
            to_translate = " ".join(arr)
     
     
     
     subs[i].text = change_lang(to_translate,to_language,from_language)
     
     if (i+1) % 10 ==0:
         
         save(subs[0:i+1])
  
  subs[length-1].text = change_lang(subs[length-1].text,to_language,from_language)    
      
  
  save(subs)


    

if __name__ == "__main__":
    
    file_loc = sys.argv[1]
    
    from_lang =  sys.argv[2]
    
    to_lang =  sys.argv[3]
    
    translator(file_loc,from_lang,to_lang)
  

