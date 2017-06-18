#! /usr/bin/env python
import sys

def LCS(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    cell = [[0 for j in range(len2)] for i in range(len1)]


    for i in range(len1):
        for j in range(len2):
            if s1[i] == s2[j]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])

    return cell[len1-1][len2-1]


def main():
    args = sys.argv
    s1, s2 = args[1], args[2]
    print s1, s2
    print LCS(s1, s2)


if __name__ == '__main__':
    main()

