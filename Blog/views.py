from django.shortcuts import render

from django.http import HttpResponse

import pyrebase

config = {
    'apiKey' : "AIzaSyAtGoWKvmTbbWxseKiFjLqam76x47MHJck",
    'authDomain' : "project-mtiet-2235c.firebaseapp.com",
    'databaseURL' : 'https://project-mtiet-2235c-default-rtdb.firebaseio.com/',
    'projectId' : "project-mtiet-2235c",
    'storageBucket' : "project-mtiet-2235c.appspot.com",
    'messagingSenderId' : "289941532910",
    'appId' : "1:289941532910:web:2d52390e9379e6b75d43ff",
    'measurementId' : "G-F9XF33FSK2"

}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def home(request):

    name = database.child('Data').child('user').get().val()
    title = database.child('Data').child('title').get().val()

    content = database.child('Data').child('content').get().val()

    date = database.child('Data').child('date').get().val()

    context =      {
         'name': name,
        'title' : title,
        'cotent' : content,
        'date' : date
    }

    return render(request, "Blog/index.html", context)