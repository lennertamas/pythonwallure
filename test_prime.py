# test_prime.py

import pytest
import allure

from prime import is_prime

@allure.title("Test is 1 prime ")
@allure.description("This test attempts to test wether 2 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.MINOR)
def test_1_is_prime():
    assert is_prime(5) == True

@allure.title("Test is 2 prime")
@allure.description("This test attempts to test wether 2 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.MINOR)
def test_2_is_prime():
    assert is_prime(6) == False



