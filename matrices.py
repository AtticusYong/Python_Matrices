# FUNCTIONS

# Solve Matrices
def solve_matrices_three(a, b, c, d, e, f, g, h, i):
  # | a b c |
  # | d e f | --> a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
  # | g h i |
  return a * e * i + b * f * g + c * d * h - c * e * g - b * d * i - a * f * h

def solve_matrices_two(a, b, c, d):
  # | a b |
  # | c d | --> a*d - b*c
  return a * d - b * c



# Solve Equations using Cramer's Rule Method
def solve_three_var_eq(a, b, c, d, e, f, g, h, i, j, k, l):
  # Cramer's Rule Method
  # | a b c   d |       | a b c |         | d b c |         | a d c |         | a b d |
  # | e f g   h | --> D=| e f g |  --> Dx=| h f g |  --> Dy=| e h g |  --> Dz=| e f h |
  # | i j k   l |       | i j k |         | l j k |         | i l k |         | i j l |
  
  #   Dx      Dy      Dz
  # x=-- ;  y=-- ;  z=--
  #   D       D       D
  dd = a * f * k + b * g * i + c * e * j - c * f * i - b * e * k - a * g * j
  dx = d * f * k + b * g * l + c * h * j - c * f * l - b * h * k - d * g * j
  dy = a * h * k + d * g * i + c * e * l - c * h * i - d * e * k - a * g * l
  dz = a * f * l + b * h * i + d * e * j - d * f * i - b * e * l - a * h * j
  if dd == 0:
    print(
      "Cannot find value of x, y, z. Some of the equations are proportional,\n therefore the equations are the same.")
  else:
    x = dx / dd
    y = dy / dd
    z = dz / dd

    return x, y, z

def solve_two_var_eq(a, b, c, d, e, f):
  # Cramer's Rule Method
  # | a b     c |       | a b |         | c b |         | a c |
  # | d e     f | --> D=| d e |  --> Dx=| f e |  --> Dy=| d f |

  #   Dx      Dy
  # x=-- ;  y=-- 
  #   D       D
  dd = a * e - b * d
  dx = c * e - b * f
  dy = a * f - c * d
  if dd == 0:
    print(
      "Cannot find value of x, y. The two equations are proportional,\n therefore the equations are the same.")
  else:
    x = dx / dd
    y = dy / dd

    return x, y

# Solve Equations using Gauss-Jordan Method
def three_var_eq(a, b, c, d, e, f, g, h, i, j, k, l):
  # Gauss-Jordan Method
  # | a b c   d |     | a    b       c          d    |      | a           b                 c                        d         | 
  # | e f g   h | --> | 0 f*a-b*e g*a-c*e    h*a-d*e | -->  | 0        f*a-b*e            g*a-c*e                 h*a-d*e      |
  # | i j k   l |     | 0 j*e-f*i k*e-g*i    l*e-h*i |      | 0           0 (k*e-g*i)(f*a-b*e)-(g*a-c*e)(j*e-f*i)    (l*e-h*i)(f*a-b*e)-(h*a-d*e)(j*e-f*i) |

  # FINDING VARIABLES
  dz = ( k * e - g * i ) * ( f * a - b * e ) - ( g * a - c * e ) * ( j * e - f * i )
  if dz == 0:
    print(
      "Cannot find value of x, y, z. Some of the equations are proportional,\n therefore the equations are the same."
    )
  else:
    ddz = ( l * e - h * i ) * ( f * a - b * e ) - ( h * a - d * e ) * ( j * e - f * i )
    z = ddz / dz

    ddy = h * a - d * e - z * ( g * a - c * e )
    dy = f * a - b * e 
    y = ddy / dy

    ddx = d - c * z - b * y
    dx = a
    x = ddx / dx
 

    return x, y, z

def two_var_eq(a, b, c, d, e, f):
  # Gauss-Jordan Method
  # | a b     c |     | a b   c |      | a   b          c |
  # | d e     f | --> | d e   f |  --> | 0 e*a-b*d   f*a-c*d|

  # FINDING VARIABLES
  dy = e * a - b * d
  if dy == 0:
    print(
      "Cannot find value of x, y. The two equations are proportional,\n therefore the equations are the same."
    )
  else:
    ddy = f * a - c * d
    y = ddy / dy

    ddx = c - b * y
    dx = a
    x = ddx / dx

    return x, y



# OUTPUT
print("The answer to the 3x3 matrix is: ",
  solve_matrices_three(
    2, 0, 1,
    1, 1, 2,
    -1, 0, 1
  )
)

print("The answer to the 2x2 matrix is: ",
  solve_matrices_two(
    3, -2,
    4, 1
    )
)

print("\n")

print("Using the Cramer's Rule Method, the values of (x, y, z): ",
  solve_three_var_eq(
    1, -2, -2, 4,
    2, 1, -3, 7,
    1, -1, -1, 3
  )
)

print("Using the Cramer's Rule Method, the values of (x, y): ",
  solve_two_var_eq(
    2, 1, 5,
    3, -5, 14
  )
)

print("\n")

print("Using the Gauss-Jordan Method, the values of (x, y, z): ",
  three_var_eq(
    1, 3, -1, 5,
    3, -1, 2, 5,
    1, 1, 2, 7
  )
)

print("Using the Gauss-Jordan Method, the values of (x, y): ",
  two_var_eq(
    3, -2, 16,
    4, 2, 12
  )
)