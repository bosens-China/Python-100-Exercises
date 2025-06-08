import unittest
from part_4_oop.exercise_066 import Cat

class TestClassAndInstanceVariables(unittest.TestCase):
    def setUp(self):
        """在测试前重置类变量，以防被其他测试修改。"""
        Cat.species = "Felis catus"

    def test_instance_variables(self):
        """测试实例变量是否对每个实例都是唯一的。"""
        cat1 = Cat("Whiskers")
        cat2 = Cat("Tom")
        self.assertEqual(cat1.name, "Whiskers")
        self.assertEqual(cat2.name, "Tom")

    def test_class_variable_access(self):
        """测试类变量可以被类和所有实例访问。"""
        cat1 = Cat("Garfield")
        # 通过类访问
        self.assertEqual(Cat.species, "Felis catus")
        # 通过实例访问
        self.assertEqual(cat1.species, "Felis catus")

    def test_class_variable_modification(self):
        """测试修改类变量会影响所有实例。"""
        cat1 = Cat("Felix")
        cat2 = Cat("Sylvester")
        
        # 初始状态
        self.assertEqual(cat1.species, "Felis catus")
        self.assertEqual(cat2.species, "Felis catus")
        
        # 修改类变量
        Cat.species = "A new species"
        
        # 验证所有实例都受到了影响
        self.assertEqual(cat1.species, "A new species")
        self.assertEqual(cat2.species, "A new species")

    def test_instance_shadowing_class_variable(self):
        """测试在实例上赋同名变量不会影响类变量。"""
        cat1 = Cat("Shadow")
        cat2 = Cat("No-Shadow")

        # 在 cat1 实例上创建一个名为 'species' 的实例变量
        cat1.species = "Panthera pardus"
        
        # cat1 的 'species' 是实例变量
        self.assertEqual(cat1.species, "Panthera pardus")
        
        # cat2 仍然访问的是类变量
        self.assertEqual(cat2.species, "Felis catus")
        
        # Cat 类的变量没有被改变
        self.assertEqual(Cat.species, "Felis catus")

if __name__ == '__main__':
    unittest.main() 