from cryptography.fernet import Fernet
import secrets 
import json

class PasswordManager:
    def __init__(self, json_file_name = "vault.json", secret_file_name="secret.key"):
        self.json_file_name = json_file_name
        self.secret_file_name = secret_file_name
        self.data = self._load_data()
        self.key = self._read_secret_key()
        self.cypher = Fernet(self.key)
                   
    
    def _load_data(self):    
        try:
            with open(self.json_file_name, 'rt') as f:
                    return json.load(f) or []
        except (FileNotFoundError, json.JSONDecodeError) :
                return []
    
    
    def _save_to_json(self):
        try :
            with open(self.json_file_name, "wt") as f:
                json.dump(self.data, f)
        except :
             print("Could not open file to write")    


    def _read_secret_key(self):
        try :
            with open(self.secret_file_name, "rb") as f:
                return f.read()
        except FileNotFoundError :
            key = Fernet.generate_key()
            with open(self.secret_file_name, 'wb') as f:
                f.write(key)
            return key   
            
            


if __name__ == "__main__":
    password_manager = PasswordManager()
