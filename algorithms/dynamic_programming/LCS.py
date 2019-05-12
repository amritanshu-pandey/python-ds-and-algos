# LCS - Longest common subsequence problem


def LCS_naive_recursion(X, Y):
    m, n = len(X), len(Y)

    if m == 0 or n == 0:
        return 0

    if X[m-1] == Y[n-1]:
        return 1 + LCS_naive_recursion(X[:m-1], Y[:n-1])
    else:
        return max(
            LCS_naive_recursion(X, Y[:n-1]), LCS_naive_recursion(X[:m-1], Y))


def _print_matrix(matrix):
    for row in matrix:
        print(row)


def LCS_dynamic(X, Y):
    m, n = len(X), len(Y)

    L = [[0]*(n+1) for i in range(m+1)]

    for j in range(m+1):
        for k in range(n+1):

            if j == 0 or k == 0:
                pass
            elif X[j-1] == Y[k-1]:
                L[j][k] = L[j-1][k-1] + 1
            else:
                L[j][k] = max(L[j-1][k], L[j][k-1])

    _print_matrix(L)
    return L[m][n]


if __name__ == '__main__':
    str1 = input('String 1: ')
    str2 = input('String 2: ')
    print('Using naive recursion approach:', LCS_naive_recursion(str1, str2))
    print('Using dynamic proramming approach:', LCS_dynamic(str1, str2))
