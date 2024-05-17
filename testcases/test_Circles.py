import math
import Source.Shapes as shape1


class TestingCircle:

    def setup_method(self, method):
        print(f"seeting methods {method}")
        self.circle= shape1.Circle(10)

    def teardown_method(self, method):
        print(f"teardown method {method}")
            # del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        del self.circle

    def test_perimetere(self):

        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
