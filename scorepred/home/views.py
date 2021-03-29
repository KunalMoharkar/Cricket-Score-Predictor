from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle
# Create your views here.

def index(request):

    if request.method == "GET":

        return render(request,"index.html")
    
    else:

        score = request.POST.get("score")
        wickets = request.POST.get("wickets")
        overs = request.POST.get("overs")
        striker = request.POST.get("striker")
        nonstriker = request.POST.get("nonstriker")

        print(int(score))
        print(int(wickets))
        print(int(overs))
        print(int(striker))
        print(int(nonstriker))

        filename = "C:/Users/kumar/Desktop/mywork/Cricket-score-predictor/scorepred/home/models/finalized_model.sav"

        loaded_model = pickle.load(open(filename, 'rb'))
        new_prediction = loaded_model.predict((np.array([[int(score),int(wickets),int(overs),int(striker),int(nonstriker)]])))
        print("Prediction score:" , new_prediction)

        return render(request,"index.html",{'score':int(new_prediction[0])})