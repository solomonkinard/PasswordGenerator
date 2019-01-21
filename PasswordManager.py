from Crypto.Cipher import AES
import asyncio, os, random, hashlib

class PasswordManager:
  def __init__(self):
    self.db_filename = 'pm.pdb'
    self.key_filename = 'pm.pky'

  def start(self):
    if not os.path.exists(self.key_filename):
      with open(self.key_filename, 'w') as f:
        h = hashlib.sha512()
        h.update(str(random.random()).encode())
        f.write(h.hexdigest())
    if not os.path.exists(self.db_filename):
      open(self.db_filename, 'w')

  def __del__(self):
    os.remove(self.db_filename)
    os.remove(self.key_filename)

  def encrypt(self):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)

    nonce = cipher.nonce

    data = b'hello, world!'
    ciphertext, tag = cipher.encrypt_and_digest(data)

    print(ciphertext, tag)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
      cipher.verify(tag)
      print('The message is authentic')
    except ValueError:
      print("Key incorrect or message corrupted")
    print(plaintext, nonce)


async def main():
  PasswordManager()

  options = {
    'start': lambda: None,
    'end': lambda: None,
    'find': lambda: None,
  }
  while True:
    option = input('> ')
    if option not in options:
      break


if __name__ == '__main__':
  asyncio.run(main())