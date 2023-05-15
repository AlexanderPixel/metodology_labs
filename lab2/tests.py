import unittest
import list

class TestLinkedList(unittest.TestCase):

    list = list.LinkedList()

    def test_append(self):
        #arrange
        ls = list.LinkedList()
        value = "1"

        #act
        ls.append(value)

        #assert
        self.assertEqual(ls.get(0), value)

    def test_insert(self):
        #arrange
        ls = list.LinkedList()

        #act
        ls.append('4')
        ls.insert(0, '0')
        ls.print()

        #arrange
        self.assertEqual(ls.get(1), '4')

        with self.assertRaises(IndexError):
            ls.insert(ls.get_length(), 'Invalid Value')

    def test_length(self):
        ls = list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')

        self.assertEqual(ls.get_length(), 3)

    def test_get(self):
        #arrange
        ls = list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')
        
        #act
        value = ls.get(0)
        #assert
        self.assertEqual(value, '1')

        with self.assertRaises(IndexError):
            ls.get(ls.get_length() + 1)

    def test_clear(self):

        ls = list.LinkedList()
        
        ls.append('1')
        ls.append('2')
        ls.append('3')
        
        ls.clear()

        self.assertEqual(ls.get_length(), 0)

    def test_delete(self):
        ls = list.LinkedList()
        
        ls.append('1')
        ls.append('2')
        ls.append('3')

        deleted = ls.delete(0)

        self.assertEqual(ls.get_length(), 2)
        self.assertEqual(deleted, '1')

        with self.assertRaises(IndexError):
            ls.delete(ls.get_length() + 1)

    def test_delete_all(self):
        ls = list.LinkedList()
        
        ls.append('1')
        ls.append('3')
        ls.append('3')

        ls.delete_all('3')

        self.assertEqual(ls.get_length(), 1)

    def test_find_first(self):
        ls = list.LinkedList()
        
        ls.append('3')
        ls.append('1')
        ls.append('3')

        first = ls.find_first('3')

        self.assertEqual(first, 0)

    def test_find_last(self):
        ls = list.LinkedList()
        
        ls.append('3')
        ls.append('1')
        ls.append('3')

        last = ls.find_last('3')

        self.assertEqual(last, 2)

    def test_reverse(self):
        ls = list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')

        ls.reverse()

        self.assertEqual(ls.get(0), '3')

    def test_clone(self):
        ls = list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')

        clone = ls.clone()

        self.assertEqual(ls.get(0), clone.get(0))

    def test_extend(self):
        ls1 = list.LinkedList()
        ls2 = list.LinkedList()

        ls1.append('First list')
        ls2.append('Second list')

        ls1.extend(ls2)

        self.assertEqual(ls1.get(1), 'Second list')

    def test__get_node(self):
        ls = list.LinkedList()
        ls.append('2')
        ls.append('4')

        node = ls._get_node(1)

        self.assertEqual(node.element, '4')

        with self.assertRaises(IndexError):
            ls._get_node(ls.get_length() + 2)


if __name__ == '__main__':
    unittest.main()