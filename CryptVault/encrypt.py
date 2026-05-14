from datetime import datetime, timezone
from cryptography.fernet import Fernet
import secrets 
import json
import string

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

    
    def _check_account_exists(self, account, username):
        return bool(account and username and account.strip() and username.strip())

    # genereate password
    # add password
    # updaste password
    # delete password 
    # list passwords

    def _encrypt_string(self, string):
        if not string:
            return None
        # Fernet requires data to be in bytes. so de encode the string before encrypting, but we need to decode the encrypted data to string before storing it in json file as json does not support bytes data type
        return self.cypher.encrypt(string.encode()).decode()
    
    def generate_password(self, length=16):
        '''Generates a secure random password of the specified length.
        The password includes a mix of uppercase letters, lowercase letters, digits, and punctuation.
        Args:
            length: The desired length of the generated password (default is 16).
        Returns:
            A securely generated random password as a string.
        '''
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))


  
    def add_password(self, account, username, password=None):
        """Add a password entry to the vault.

        If `password` is not provided, a secure password is generated.
        The `(account, username)` pair must be unique.

        Args:
            account: Service name, normalized to lowercase.
            username: Account username/email.
            password: Plaintext password. If None, generates one.

        Returns:
            None
        """

        if not self._check_account_exists(account, username) :
            print("Account and username are required")
            return
        
        accnt = account.strip().lower()
        user = username.strip()

        for entry in self.data :
            if entry["account"] == accnt and entry["username"] == user :
                print("Entry exists; use update instead")
                return 


        passObj = {
            'account' : accnt, 
            'username' : user
            }
        
        if password is None :
            password = self.generate_password()
        
        encrypted_password = self._encrypt_string(password)
        
        passObj['encrypted_password'] = encrypted_password
        passObj['created_at'] = now_iso()
        passObj['updated_at'] = passObj['created_at']
        
        self.data.append(passObj)
        self._save_to_json()

    
    def update_password(self, account, username, new_password=None):
        """Update the password for an existing entry.

        Args:
            account: Service name, normalized to lowercase.
            username: Account username/email.
            new_password: New plaintext password.  
        Returns:
            None
        """
        if not self._check_account_exists(account, username):
            print("Account and username are required")
            return
        
        accnt = account.strip().lower()
        user = username.strip()

        existing = next((e for e in self.data if e["account"] == accnt and e["username"] == user), None)

        if not existing :
            print("entry does not exist")
            return 
            

        if new_password is None :
            new_password = self.generate_password()

        encrypted_password = self._encrypt_string(new_password)
        existing['encrypted_password'] = encrypted_password
        existing['updated_at'] = now_iso()
        self._save_to_json()
        
                
    def get_password(self, account, username):
        """Retrieve the decrypted password for a given account and username.

        Args:
            account: Service name, normalized to lowercase.
            username: Account username/email. 
        Returns:
            The decrypted password as a string, or None if not found.
        """
        if not self._check_account_exists(account, username) :
            print("Account and username are required")
            return
        
        accnt = account.strip().lower()
        user = username.strip()
        
        existing = next((e for e in self.data if e['account'] == accnt and e['username'] == user), None)

        if not existing :
            print("No entry found for that account and user name")
            return
        
        encrypted_password = existing['encrypted_password']
        return self.cypher.decrypt(encrypted_password.encode()).decode()


    def list_accounts(self):
        ''' List all stores accounts with username without showing passwords
        '''
        print(f"{'Account':<10} | {'Username':<10}")
        for e in self.data :
            print(f"{e['account']:<10} | {e['username']:<10}")
            

            
def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec='seconds').replace("+00:00", "Z")



if __name__ == "__main__":
    password_manager = PasswordManager()
    # password_manager.add_password("gmail", "rahimovic", "mysecretpassword")
    # password_manager.add_password("github", "rahimovic")
    # password_manager.update_password("github", "rahimovic", "mynewsecretpassword")
    print(password_manager.get_password('github', 'rahimovic'))
    password_manager.list_accounts()