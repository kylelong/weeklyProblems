=begin
resource: https://www.mathwarehouse.com/geometry/triangles/triangle-inequality-theorem-rule-explained.php
Checks if three sides of potential triangle would make a valid triangle
@param a, one side of the triangle
@param b, one side of the triangle
@param c, one side of the triangle
@return true/false whether the sides would make a valid triangle
=end
def validTriangle(a,b,c)
    (a + b) > c and (a + c) > b and (b + c) > a
end
puts validTriangle(60, 80, 40)
puts validTriangle(5, 5, 50)