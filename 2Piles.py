import random
import math
class GeneticAlgorithm:
    POP = 30
    LEN = 10
    MUT = 0.1
    REC = 0.5
    END = 2000
    SUMTARG = 36
    PRODTARG = 360
    gene = []
    for i in range(0, 31):
        gene.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    rnd = random.random()
    def run(self):
        self.init_pop()
        for tournamentNo in range(0, self.END):
            random.seed()
            a = math.trunc(round(self.POP * random.random(), 0))
            random.seed()
            b = math.trunc(round(self.POP * random.random(), 0))
            if self.evaluate(a) < self.evaluate(b):
                winner = a
                loser = b
            else:
                winner = b;
                loser = a;
            for i in range(0, self.LEN):
                if random.random() < self.REC:
                    self.gene[loser][i] = self.gene[winner][i]
                if random.random() < self.MUT:
                    self.gene[loser][i] = 1 - self.gene[loser][i]
                if self.evaluate(loser) == 0.0:
                    self.display(tournamentNo, loser)
    def display(self, tournaments, n):
        print("\r\n==============================\r\n")
        print("After {} tournaments, Solution sum pile (should be 36) cards are : ".format(tournaments))
        countsum = 0
        countprod = 1
        for i in range(0, self.LEN):
            if self.gene[n][i] == 0:
                print(i + 1)
                countsum += i+1
        print("\r\nWhich sum to: {}\r\n".format(countsum))
        print("\r\n==============================\r\n")
        print("\r\nAnd Product pile (should be 360)  cards are : ")
        for i in range(0, self.LEN):
            if self.gene[n][i] == 1:
                print(i + 1)

                countprod = countprod*(i+1)
        print("\r\nWhich product is: {}\r\n".format(countprod))
        print("\r\n==============================\r\n")
    def evaluate(self, n):
        ssum = 0
        prod = 1
        for i in range(0, self.LEN):
            if self.gene[n][i] == 0:
                ssum += (1 + i)
            else:
                prod *= 1 + i
        scaled_sum_error = (ssum - self.SUMTARG) / self.SUMTARG
        scaled_prod_error = (prod - self.PRODTARG) / self.PRODTARG
        combined_error = math.fabs(scaled_sum_error) + math.fabs(scaled_prod_error)
        return combined_error
    def init_pop(self):
        for i in range(0, self.POP):
            for j in range(0, self.LEN):
                self.rnd = random.random()
                if self.rnd < 0.5:
                    self.gene[i][j] = 0
                else:
                    self.gene[i][j] = 1