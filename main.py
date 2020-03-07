###just some test for the matrix math.
import vector
import matrix

def main():
      m = [[1,4,6],[5,4,4],[0,0,1]]
      b = [[6,3,3],[12,4,6],[6,5,5]]
      m = matrix.scale_row(b,2,"mul",2)
      f = matrix.scale_row(m,0,"div",3)
      matrix.print_matrix(m)
      matrix.print_matrix(f)
      w = matrix.get_vector(m,1)
      matrix.print_matrix(w)
      k = [[2,2],[1,0],[9,7],[6,6]]
      c = [[2,6,3],[7,7,7]]
      res = matrix.multiply_matrix(k,c)
      matrix.print_matrix(res)

if __name__ == "__main__":
   main()