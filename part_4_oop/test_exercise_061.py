import unittest
from part_4_oop.exercise_061 import Dog

class TestDogClass(unittest.TestCase):
    def test_dog_creation(self):
        """测试 Dog 实例是否能被成功创建，并且属性是否被正确设置。"""
        my_dog = Dog("Fido", 5)
        self.assertIsInstance(my_dog, Dog)
        self.assertEqual(my_dog.name, "Fido")
        self.assertEqual(my_dog.age, 5)

    def test_another_dog(self):
        """测试创建另一个不同的 Dog 实例。"""
        another_dog = Dog("Buddy", 2)
        self.assertEqual(another_dog.name, "Buddy")
        self.assertEqual(another_dog.age, 2)
        
    def test_attribute_types(self):
        """测试属性的类型是否正确。"""
        dog = Dog("Rex", 3)
        self.assertIsInstance(dog.name, str)
        self.assertIsInstance(dog.age, int)


if __name__ == '__main__':
    unittest.main() 