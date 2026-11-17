import unittest
from compose_check import check_document

class ComposeTests(unittest.TestCase):
    def test_missing_dependency_and_port_collision(self):
        doc={"services":{"web":{"image":"nginx","ports":["8080:80"]},
                         "api":{"build":".","depends_on":["cache"],"ports":["8080:3000"]}}}
        issues=check_document(doc)
        self.assertTrue(any("unknown service 'cache'" in x for x in issues))
        self.assertTrue(any("host port 8080" in x for x in issues))

    def test_valid_compose_subset(self):
        doc={"services":{"db":{"image":"sqlite:latest"},"api":{"build":".","depends_on":["db"]}}}
        self.assertEqual(check_document(doc),[])

if __name__=="__main__": unittest.main()
