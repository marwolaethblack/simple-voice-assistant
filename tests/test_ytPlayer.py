import unittest
from modules.ytPlayer import ytPlayer

class TestYtPlayer(unittest.TestCase):

    def test_link_from_query(self):
        query = "50 cent"
        url = ytPlayer.yt_link_from_query(query)
        self.assertEqual("http://www.youtube.com/watch?v=5qm8PH4xAss", url)

if __name__ == '__main__':
    unittest.main()