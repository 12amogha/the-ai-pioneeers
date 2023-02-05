import firebase
#import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from firebase_admin import credentials
import sys
def checkxml(loc):
    f = open(loc, "r+")
    list1 = []
    ans=0
    perml = ['CAMERA','STORAGE','CONTACTS','MICROPHONE','MICROPHONE','SMS','PHONE']
    import re
    pattern = r'android.permission\.(\w+)'
    for i in f.readlines():
        list1 += i.split(" ")
    for i in list1:
        match = re.search(pattern, i)
        if match:
            permission = match.group(1)
            if ([c for c in permission.split('_') if c in perml]):
                ans+=1
    return ans
loc=sys.argv[1]
ans=checkxml(loc)
t ="this app has {} unrequired permissions which make the app dangerous to use and hence it is a probable fraudulent app".format(ans)





i = 4
firebaseConfig = {
  "apiKey": "AIzaSyC_-hBXpK-3eZvDTHKb2DIurcVvx-6q1lc",
  "authDomain": "police-f2ce4.firebaseapp.com",
  "databaseURL": "https://police-f2ce4-default-rtdb.firebaseio.com",
 " projectId": "police-f2ce4",
  "storageBucket": "police-f2ce4.appspot.com",
 "messagingSenderId": "342750787617",
  "appId": "1:342750787617:web:44e18d97438a7fb96a0b60"
};

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
if not firebase_admin._apps:
  cred_obj2 = firebase_admin.credentials.Certificate('/content/police-f2ce4-firebase-adminsdk-zkk2p-b41281fac2.json')
  default_app2 = firebase_admin.initialize_app(cred_obj2, {'databaseURL':'https://police-f2ce4-default-rtdb.firebaseio.com'})
appId2='com.mastermelon'
title2='mastermelon'
db.child("Fraud_Details").child(i).child("appid").set(appId2)
db.child("Fraud_Details").child(i).child("title").set(title2)
i+=1
print(t)
input()