# CryptVault 🔐

A secure, lightweight CLI password manager that encrypts and stores passwords locally using symmetric encryption (Fernet).

## Overview

CryptVault is a command-line password management tool designed to help you securely store account credentials. All passwords are automatically encrypted using the cryptography library's Fernet cipher before being saved to a JSON file. Even if someone gains access to the vault file, they cannot read passwords without the encryption key.

## Features

- 🔒 **Secure Storage** — Passwords encrypted with symmetric encryption (Fernet)
- 🗝️ **Automatic Key Management** — Encryption key is generated once and stored securely
- 🎲 **Password Generation** — Generate strong, random passwords using Python's `secrets` library
- 💾 **JSON Storage** — All encrypted passwords stored in a portable JSON format
- 🖥️ **CLI Interface** — Simple command-line interface for easy access

## Installation

### Prerequisites

- Python 3.7 or higher

### Dependencies

- **cryptography** — Symmetric encryption (Fernet cipher)
- **json** — Built-in, for vault storage
- **secrets** — Built-in, for secure password generation
- **uuid** — Built-in, for unique entry identifiers

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python encrypt.py
```

On first run, `secret.key` and `vault.json` will be automatically created.

## JSON Format

The `vault.json` file stores encrypted passwords in the following format:

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "account": "gmail",
    "username": "user@gmail.com",
    "encrypted_password": "gAAAAABl2a3b4c5d6e7f8g9h0i...",
    "created_at": "2024-01-15T10:30:45Z",
    "updated_at": "2024-01-20T14:22:10Z",
    "note": "Primary email account"
  },
  {
    "id": "650e8400-e29b-41d4-a716-446655440001",
    "account": "github",
    "username": "myusername",
    "encrypted_password": "gAAAAABl2b5c6d7e8f9g0h1i2j3k...",
    "created_at": "2024-01-18T09:15:30Z",
    "updated_at": "2024-01-18T09:15:30Z",
    "note": null
  }
]
```

**Field Descriptions:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string (UUID) | Unique identifier for each password entry |
| `account` | string | Name of the account/service (e.g., "gmail", "github") |
| `username` | string | Username or email associated with the account |
| `encrypted_password` | string | Password encrypted using Fernet cipher |
| `created_at` | string (ISO 8601) | Timestamp when the entry was created |
| `updated_at` | string (ISO 8601) | Timestamp when the entry was last modified |
| `note` | string or null | Optional description or note about the account (null if not provided) |

## CLI Commands

### `add`
Add a new password to the vault.

**Usage:**
```bash
python encrypt.py add --account ACCOUNT_NAME --username USERNAME [--password PASSWORD]
```

**Options:**
- `--account` — Name of the account/service (e.g., `gmail`, `github`)
- `--username` — Username or email associated with the account
- `--password` — (Optional) Password to store. If omitted, a strong password will be generated

**Example:**
```bash
python encrypt.py add --account github --username john_doe --password mypassword
python encrypt.py add --account twitter --username john_doe  # Auto-generates password
```

---

### `list`
Display all stored accounts without showing passwords.

**Usage:**
```bash
python encrypt.py list
```

**Output:**
```
Account        | Username
---            | ---
gmail          | user@gmail.com
github         | john_doe
twitter        | john_doe
```

---

### `get`
Retrieve and decrypt a stored password for a specific account.

**Usage:**
```bash
python encrypt.py get --account ACCOUNT_NAME
```

**Options:**
- `--account` — Name of the account to retrieve

**Example:**
```bash
python encrypt.py get --account gmail
# Output: Password for gmail: your_encrypted_password_here
```

---

### `delete`
Remove an account and its password from the vault.

**Usage:**
```bash
python encrypt.py delete --account ACCOUNT_NAME
```

**Options:**
- `--account` — Name of the account to delete
- `--confirm` — (Optional) Skip confirmation prompt

**Example:**
```bash
python encrypt.py delete --account old_account
python encrypt.py delete --account old_account --confirm  # No confirmation
```

---

### `generate`
Generate a strong random password without storing it.

**Usage:**
```bash
python encrypt.py generate [--length LENGTH]
```

**Options:**
- `--length` — (Optional) Length of password to generate (default: 16)

**Example:**
```bash
python encrypt.py generate
python encrypt.py generate --length 32
# Output: Generated password: aBc1234!@#$XyZ9
```

---

### `update`
Update the password for an existing account.

**Usage:**
```bash
python encrypt.py update --account ACCOUNT_NAME [--password NEW_PASSWORD]
```

**Options:**
- `--account` — Name of the account to update
- `--password` — (Optional) New password. If omitted, a strong password will be generated

**Example:**
```bash
python encrypt.py update --account gmail --password newpassword
python encrypt.py update --account twitter  # Auto-generates new password
```

---

### `export`
Export all encrypted passwords to a backup file (encrypted).

**Usage:**
```bash
python encrypt.py export --output BACKUP_FILE
```

**Options:**
- `--output` — Path to backup file

**Example:**
```bash
python encrypt.py export --output vault_backup.json
```

---

### `help`
Display help information for all commands.

**Usage:**
```bash
python encrypt.py help [COMMAND]
```

**Example:**
```bash
python encrypt.py help
python encrypt.py help add
```

## Usage Example

```bash
# Initialize (automatically generates encryption key on first run)
python encrypt.py

# Add a new password
python encrypt.py add --account gmail --username john@gmail.com

# List all accounts
python encrypt.py list

# Get a password
python encrypt.py get --account gmail

# Generate a strong password
python encrypt.py generate --length 20

# Update a password
python encrypt.py update --account gmail

# Delete an account
python encrypt.py delete --account gmail
```

## Security Notes

⚠️ **Important:**
- Your encryption key is stored in `secret.key` — **do not share or lose this file**
- The `vault.json` file is encrypted but should still be kept private
- Never share your `secret.key` file with anyone
- Store `secret.key` in a safe location and back it up

## Files

- `encrypt.py` — Main application file containing the `PasswordManager` class
- `vault.json` — Encrypted password storage (auto-generated)
- `secret.key` — Encryption key (auto-generated on first run, **keep safe!**)

## License

MIT 



