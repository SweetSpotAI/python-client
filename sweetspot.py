import requests


class Study:
    def __init__(self, study_name, params, endpoint="http://localhost:8080/", token=None):
        if token == None:
            raise "No token provided, please provide a token"
        self.endpoint = endpoint
        self.params = params
        self.token = token
        self.endpoint = endpoint

        self.study_id = requests.post(self.endpoint + "new_experiment", json={'parameters': params,
                                                         'experiment_name': study_name,
                                                         "algorithm": "NeverGrad",
                                                         "auth_token": token}).json()

    def ask(self):
        params = []
        while len(params) == 0:
            r = requests.get(self.endpoint + "params/" + self.study_id)
            r.encoding = 'UTF-8'
            params = r.json()
        return params


    def tell(self, params, output):
    	requests.post(
                self.endpoint + "register", json={"inputs": params, "output": output, "experiment_id": self.study_id})


#study = Study("test1", {'x': {'number': 'continuous'}}, token="17a3ae3404414c26a043cdafc3c47cb4")
#x = study.ask()
#print('got:', x)
#study.tell(x, 1.0)