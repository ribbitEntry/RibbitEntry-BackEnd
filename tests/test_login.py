from . import TCBase, check_status_code


class LoginTest(TCBase):

    def register(self, userId, pw, nickname):
        return self.app.post(
            '/api/sign-up',
            data=dict(userId=userId, password=pw, nickname=nickname),
            follow_redirects=True
        )

    def login(self, userId, pw):
        return self.app.post(
            '/api/login',
            data=dict(userId=userId, password=pw)
        )

    def test_valid_registration(self):
        response = self.register('onlyfortest@gmail.com', 'thisispassword', 'mynickname')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Thank you for sign in our service!', response.data)

    def test_invalid_registration_non_nickname(self):
        response = self.register('onlyfortest@gmail.com', 'thisispassword')
        self.assertIn("nickname hasn't found.", response.data)
