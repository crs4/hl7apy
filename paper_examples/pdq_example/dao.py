

class DAO:
    def __init__(self):
        self._patients = [("Patient_Surname" ,"One", "19700101") ,("Patient_Surname" ,"Two", "19600105"),]
    
    def get_data(self, params):
        return [p for p in self._patients if params.get("NAME","").lower() in p[1].lower() and params.get("SURNAME","").lower() in p[0].lower()]
    