from clarifai.rest import ClarifaiApp
myApi='937179c1c41f4378b15017c3bc501ce4'
app = ClarifaiApp(api_key=myApi)


def predict(imageLink, myApi):  
    app = ClarifaiApp(api_key=myApi)

    model = app.public_models.general_model

    response = model.predict_by_filename(imageLink)

    concepts = response['outputs'][0]['data']['concepts']
    results = []

    for concept in concepts:
        results.append((concept['name']))

    return results