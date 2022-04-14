def CheSs(N,M):
    for i in range(int(N)):
        for j in range(int(M)):
            if (i + j) % 2 == 0:
                print("🟨",end="")
            elif (i + j) % 2 != 0:
                print("🟩",end="")
        print("\n",end="")
N = (input("Enter N :"))
M = (input("Enter M :"))
CheSs(int(N),int(M))