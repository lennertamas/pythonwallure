import prime
import pytest
import allure

@allure.title("Test 4 is prime ")
@allure.description("This test attempts to test wether 4 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_is_prime():
    assert prime.is_prime(4)==False

@allure.title("Test 5 is prime ")
@allure.description("This test attempts to test wether 5 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-123")
@allure.severity(allure.severity_level.CRITICAL)
def test_5_is_prime():
    assert prime.is_prime(5)==True

@allure.title("Test exception ")
@allure.description("This test attempts to test wether an alphabet char raises exception")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-444")
@allure.severity(allure.severity_level.CRITICAL)
def test_exception():
    with pytest.raises(Exception):
        prime.is_prime("a")