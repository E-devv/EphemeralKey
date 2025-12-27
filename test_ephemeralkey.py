import unittest
import random
import string
from ephemeralkey import generate_strong_password, generate_temp_email


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        """Verifies that the generated password has the correct length."""
        random.seed(0)
        password = generate_strong_password(length=20)
        self.assertEqual(len(password), 20)

        random.seed(0)
        password = generate_strong_password(length=8)
        self.assertEqual(len(password), 8)

    def test_all_character_types_included(self):
        """Verifies that all character types are included by default."""
        random.seed(0)
        password = generate_strong_password()
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in "!@#$%^&*()-_=+" for c in password))

    def test_character_type_exclusion(self):
        """Verifies the exclusion of specific character types."""
        random.seed(0)
        # Exclude uppercase
        password = generate_strong_password(use_upper=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

        random.seed(0)
        # Exclude digits
        password = generate_strong_password(use_digits=False)
        self.assertFalse(any(c in string.digits for c in password))

        random.seed(0)
        # Exclude symbols
        password = generate_strong_password(use_symbols=False)
        self.assertFalse(any(c in "!@#$%^&*()-_=+" for c in password))

        random.seed(0)
        # Exclude lowercase
        password = generate_strong_password(use_lower=False)
        self.assertFalse(any(c in string.ascii_lowercase for c in password))

    def test_only_one_character_type(self):
        """
        Verifies that the password is generated with only one character type.
        """
        random.seed(0)
        password = generate_strong_password(
            use_upper=True, use_lower=False,
            use_digits=False, use_symbols=False
        )
        self.assertTrue(all(c in string.ascii_uppercase for c in password))
        random.seed(0)
        password = generate_strong_password(
            use_upper=False, use_lower=False,
            use_digits=True, use_symbols=False
        )
        self.assertTrue(all(c in string.digits for c in password))

    def test_no_character_sets_selected_raises_error(self):
        """
        Verifies that a ValueError is raised if no character type is
        selected.
        """
        with self.assertRaises(ValueError):
            generate_strong_password(
                use_upper=False, use_lower=False,
                use_digits=False, use_symbols=False
            )


class TestEmailGenerator(unittest.TestCase):

    def test_email_format(self):
        """Verifies that the generated email has a valid format."""
        random.seed(0)
        email = generate_temp_email()
        self.assertIn('@', email)
        parts = email.split('@')
        self.assertEqual(len(parts), 2)
        self.assertTrue(len(parts[0]) > 0)
        self.assertTrue(len(parts[1]) > 0)

    def test_custom_domain(self):
        """Verifies that the email is generated with the specified domain."""
        random.seed(0)
        email = generate_temp_email(domain="custom.com")
        self.assertTrue(email.endswith("@custom.com"))

    def test_username_length(self):
        """Verifies the length of the username part of the email."""
        random.seed(0)
        email = generate_temp_email(username_length=10)
        username = email.split('@')[0]
        self.assertEqual(len(username), 10)

    def test_username_characters(self):
        """
        Verifies that the username contains only valid characters (lowercase
        and digits).
        """
        random.seed(0)
        email = generate_temp_email(username_length=20)
        username = email.split('@')[0]
        valid_chars = string.ascii_lowercase + string.digits
        self.assertTrue(all(c in valid_chars for c in username))


if __name__ == '__main__':
    unittest.main()
