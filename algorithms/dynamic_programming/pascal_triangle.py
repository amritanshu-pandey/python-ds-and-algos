class SolutionRecursion:
    def generate(self, numRows):
        row = numRows
        
        if numRows < 1:
            return []
        
        tri = []
        for i in range(0, numRows):
            tri.append([0] * (i+1))
        
        tri[0][0] = 1
        
        for i in range(0, numRows):
            self.helper(numRows-1, i, tri)
        
        return tri

    def helper(self, r, c, tri):
        if c == 0:
            tri[r][c] = 1
        elif c == r:
            tri[r][c] = 1
        else:
            tri[r][c] = (tri[r-1][c-1] or self.helper(r-1, c-1, tri)) + (tri[r-1][c] or self.helper(r-1, c, tri))
        return tri[r][c]

if __name__ == '__main__':
    print(SolutionRecursion().generate(5))