import requests
data = {'email':'test@email.com',
        'classes_': model.classes_.tolist() ,
        'coef_':model.coef_.tolist() ,
        'intercept_': model.intercept_.tolist() ,
        'n_iter_': model.n_iter_.tolist()}

resp = requests.post(url = "https://project-insight-chat.herokuapp.com/get-score", json=data).json()
print(float(resp))

