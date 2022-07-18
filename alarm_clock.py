#Practice Alarm Clock
import datetime, time, os, webbrowser, sys, random, re




def vid_alarm():
  upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  setlist = upper+lower+digits

  dctlist = {0:"Laa2dqK2GiE", 1:"kYPD6TtFJqU", 2:"mO1oBfG59Xw", 3:"w7B2yJsN39c", 4:"AGqUCKin4X0", 5:"0k9wIsKKgqo", 6:"WEHQjbEEcg8", 7:"hQC8COGQ4BM", 8:"dmIFhpQe9Zk", 9:"n0UXA7oLc-s", 10:"sysgF_Vic4U"}
#Generate random string of length 11 using characters from setlist
  #i=0
  #while i < 10:
  #    vid_id = [] 
  #    vid_id.insert(i,random.choice(setlist))
  #    #vid_id[i] = random.choice(setlist)
  #    i+=1
  vid_id = []
  for i in range(0,11):
       item = random.choice(setlist)
       vid_id.append(item)
        
#If video is not open check with error
  vid_id_str = random.choice(dctlist)
  #vid_id_str = "".join(str(item) for item in vid_id)
  url = "https://www.youtube.com/watch?v=" + vid_id_str 
  if not webbrowser.open(url):
      print("Opening Video...")
      webbrowser.register('mozilla')
      while not webbrowser.open_new(url):
        webbrowser.open_new(url)
  if webbrowser.open(url):
      #Activate alarm then print message
      print("Samuel L. ""MotherF**king"" Jackson says: Wake Up!")   
  else: 
      raise TimeoutError("Program Time Out, Please Try Again")
  pass




def alarm_seconds(alarm_time):
#Convert to format to find lenght of list to convert to seconds
    alarm_time = [int(n) for n in alarm_time.split(":")]

#Convert the alarm time from [H:M] or [H:M:S] to seconds
    seconds_hms = [3600, 60, 1] #Number of seconds in an Hour, Minute, and Second for conversion

    alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])


#Get the current time of day in seconds
    now = datetime.datetime.now()

    current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

#Call function
    alarm(alarm_seconds, current_time_seconds) 




def alarm_input_check(alarm_time):
#Regular Expression to check if alarm matches 00:00 or 00:00:00 patern
    if re.match("[0-9][0-9]:[0-9][0-9]", alarm_time) or re.match("[0-9][0-9]:[0-9][0-9]:[0-9][0-9]", alarm_time) == True:
        alarm_seconds(alarm_time)
        return True 
    else:
        raise ValueError("ERROR: Enter time in HH:MM or HH:MM:SS format")
        return False




def alarm(alarm_seconds, current_time_seconds):
#Activate video 
    if current_time_seconds != alarm_seconds: #temp to excute fucntion 
        vid_alarm()
 

def sleep_alarm(current_time_seconds):
#Calculate the number of seconds until alarm goes off
    time_diff_seconds = alarm_seconds - current_time_seconds

# If time difference is negative, set alarm for next day
    if time_diff_seconds < 0:

        time_diff_seconds += 86400 # number of seconds in a day

# Display the amount of time until the alarm goes off
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Sleep until the alarm goes off
    time.sleep(time_diff_seconds)



#Prompt User for input
alarm_time = input("Set a time for the alarm (Ex. 06:30 or 18:30:00): ")

#alarm_time = [int(n) for n in alarm_time.split(":")]

if str.isalnum(alarm_time[0]):       
    #Call Functions
    alarm_input_check(alarm_time)
 






        

        



















# Load list of possible video URLs

#with open("youtube_alarm_videos.txt", "r") as alarm_file:

#   videos = alarm_file.readlines()

# Open a random video from the list

 #webbrowser.open(random.choice(videos))
    
