from django.test import TestCase
from django.contrib.auth import get_user_model



class CustomUserTests(TestCase):
    def test_crear_usuario(self):
        Usu = get_user_model()
        usu = Usu.objects.create_user(
            username = "walter",
            email = "walter@mail.com",
            password = "123"
        )

        # Que esperamos
        self.assertEqual(usu.username, "walter")
        self.assertEqual(usu.email, "walter@mail.com")
        self.assertTrue(usu.is_active)
        self.assertFalse(usu.is_staff)
        self.assertFalse(usu.is_superuser)

    def test_crear_superusuario(self):
        Usu = get_user_model()
        usu = Usu.objects.create_superuser(
            username = "walter",
            email = "walter@mail.com",
            password = "123"
        )

        # Que esperamos
        self.assertEqual(usu.username, "walter")
        self.assertEqual(usu.email, "walter@mail.com")
        self.assertTrue(usu.is_active)
        self.assertTrue(usu.is_staff)
        self.assertTrue(usu.is_superuser)
