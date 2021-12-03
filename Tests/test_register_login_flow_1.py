from Pages.PowerPage import PowerPage
import pytest

# ---------------TEST CASE VARIABLES-----------------
expected_positive_register_message_count = 1
expected_positive_login_message_count = 1


@pytest.mark.usefixtures('init_driver')
class TestRegisterLoginFlow:
    def test_register_login_flow(self):
        pp = PowerPage(self.driver)
        pp.navigate_by_url("http://demo.guru99.com/insurance/v1/index.php")
        pp.navigate_to_register_page()
        pp.do_registration("Davit", "Amirkhanyan", "12345678", "Vilnyus", "Yerevan", 'Armenia', "12345", 'test@gmail.com', 'aaa111', 'aaa111')
        actual_positive_register_message_count = pp.return_element_count_on_page(pp.POSITIVE_REGISTER_FLAG)
        pp.do_login('test@gmail.com', 'aaa111')
        tuple_selector = (pp.POSITIVE_LOGIN_FLAG[0], pp.POSITIVE_LOGIN_FLAG[1].format('test@gmail.com'))
        actual_positive_login_message_count = pp.return_element_count_on_page(tuple_selector)
        assert actual_positive_register_message_count == expected_positive_register_message_count
        assert actual_positive_login_message_count == expected_positive_login_message_count
        