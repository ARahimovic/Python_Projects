'''
   Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

   Mat size must be X. ( is an odd natural number, and  is  times .)
   The design should have 'WELCOME' written in the center.
   The design pattern should only use |, . and - characters.
   '''

# Enter your code here. Read input from STDIN. Print output to STDOUT


def returnDesign(N, M):
    for i in range(N):
        if (i == N // 2):
            print("WELCOME".center(M, "-"))
        elif (i < N // 2):
            print((".|."*(2*i+1)).center(M, "-"))
        else:
            coeff = 2*(N % i)-1
            print((".|."*coeff).center(M, "-"))


if __name__ == "__main__":
    N, M = map(int, input().split())
    returnDesign(N, M)
