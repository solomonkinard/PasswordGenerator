import random, string, unittest


class PasswordGenerator:
  @staticmethod
  def gen(template):
    d = {
      'l': lambda: random.choice(string.ascii_lowercase),
      'u': lambda: random.choice(string.ascii_uppercase),
      'd': lambda: random.choice(string.digits),
    }
    return ''.join([d[c]() if c in d else c for c in template])

class TestPasswordGenerator(unittest.TestCase):
  def test_basic(self):
    template = 'ull-llu'
    pw = PasswordGenerator().gen(template)
    self.assertEqual(len(pw), len(template))
    self.assertNotEqual(pw, template)
    for i, c in enumerate(template):
      if c == 'u':
        self.assertTrue(pw[i].isupper())
      elif c == 'l':
        self.assertTrue(pw[i].islower())


if __name__ == '__main__':
  unittest.main()
