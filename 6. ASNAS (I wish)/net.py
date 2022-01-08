from numpy.random.mtrand import rand
import torch
from torch import random
from torch._C import dtype
import torch.nn as nn
import numpy as np
import tests
from random import randrange

class net(nn.Module):
    def __init__(self, l):
        super().__init__()
        self.code_length = l

        self.i = nn.Linear(1, 128)
        self.l1 = nn.Linear(128, 128)
        self.l2 = nn.Linear(128, 4)

        self.criterion = nn.BCELoss()
        self.optimizer = torch.optim.Adam(self.parameters(), lr=1e-6)
    
    def forward(self, x):
        o0 = self.i(x)
        o1 = self.l1(o0)
        o2 = self.l2(o1)
        return o2

    def crossover(self, p1, p2):
        p1 = p1.numpy()
        p2 = p2.numpy()

        x = randrange(len(p1))
        tmp = p2[:x].copy()
        p2[:x], p1[:x]  = p1[:x], tmp

        p1 = torch.tensor(p1)
        p2 = torch.tensor(p2)

        return p1, p2

    def mutate(self, p):
        p = p.numpy()
        while(np.random.random() > 0.1):
            x = randrange(len(p))
            p[x] = np.random.random()

        p = torch.tensor(p)
        return p

    def turnover(self, p):
        if(np.random.random() > 0.5):
            p = p.numpy()
            p = np.flip(p)
            p = np.copy(p)
            p = torch.tensor(p)
        return p

    def run(self):
        tester = tests.rastrigin
        for tries in range(100):
            print("try: ", tries)
            # generate population
            pop = []
            best = -1e12
            for i in range(100):
                arr = np.random.rand(self.code_length) * 60 - 30
                fitness = tester(arr)
                if fitness > best:
                    best = fitness

                pop.append([torch.tensor(arr, dtype=torch.float32), fitness])
                # gene, current fitness, last fitness

            iter = 0
            # test and record fitness
            for epoch in range(1000):
                for i in range(100):
                    input = torch.tensor([iter], dtype=torch.float32)
                    # feed to network
                    output = self.forward(input)
                    # do the indicated operator
                    op = torch.argmax(output)
                    if op == 0:
                        max = sum([c[1] for c in pop])
                        selection_probs = [c[1]/max for c in pop]
                        r = np.random.choice(len(pop), p=selection_probs)

                        pop[i][0], pop[r][0] = self.crossover(pop[i][0], pop[r][0])
                    elif op == 1:
                        pop[i][0] = self.turnover(pop[i][0])
                    elif op == 2:
                        pop[i][0] = self.mutate(pop[i][0])
                    # calculate loss
                    gene = pop[i][0]
                    fitness = tester(gene.numpy())

                    if fitness > best:
                        best = fitness
                        print(epoch, best)

                    loss = fitness - pop[i][1]
                    target = torch.tensor(1, dtype=torch.float, requires_grad=True)
                    res = torch.tensor(1, dtype=torch.float, requires_grad=True)

                    if(loss <= 0):
                        res = torch.tensor(0, dtype=torch.float, requires_grad=True)

                    loss = self.criterion(res, target)
                    loss.backward()
                    self.optimizer.step()
                    pop[i][1] = fitness
                    
                    iter += 1

net_ = net(10)
net_.run()