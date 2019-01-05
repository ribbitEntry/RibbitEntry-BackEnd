from tests import TCBase, check_status_code


class LoginTest(TCBase):

    def setUp(self):
        super(LoginTest, self).setUp()
        self.short_url = self.save_url_request()
