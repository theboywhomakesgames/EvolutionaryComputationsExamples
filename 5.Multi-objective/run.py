import numpy as np
from nsga2.problem import Problem
from nsga2.evolution import Evolution
import testfunctions
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------- #
#                               Author MH.Samadi                               #
# ---------------------------------------------------------------------------- #
run_iter = 0

def run(tf1, tf2, rng = 10, var_range = (-5, 5)):
    global run_iter

    variables_range=[]
    for i in range(rng):
        variables_range.append(var_range)

    problem = Problem(
        num_of_variables=rng,
        objectives=[tf1, tf2],
        variables_range=variables_range,
        expand=False
    )
    evo = Evolution(problem)
    evol = evo.evolve()
    func = [i.objectives for i in evol]

    function1 = [i[0] for i in func]
    function2 = [i[1] for i in func]
    plt.clf()
    plt.xlabel('Function 1', fontsize=15)
    plt.ylabel('Function 2', fontsize=15)
    plt.scatter(function1, function2)
    plt.savefig("{iter}.png".format(iter=run_iter))
    run_iter += 1

print("kur")
run(testfunctions.kursawe1, testfunctions.kursawe2, 10, (-5, 5))
run(testfunctions.kursawe1, testfunctions.kursawe2, 30, (-5, 5))
run(testfunctions.kursawe1, testfunctions.kursawe2, 50, (-5, 5))

# kur - 10
# [-15126538058.211031, -38.757622701365825]

# kur - 30
# [-1991006584575.9895, -116.27286776416183]

# kur - 50
# [-36651585847.80749, -193.78811389367212]

print("schaffer")
run(testfunctions.schaffer1, testfunctions.schaffer2, 10, (-5, 5))
run(testfunctions.schaffer1, testfunctions.schaffer2, 30, (-5, 5))
run(testfunctions.schaffer1, testfunctions.schaffer2, 50, (-5, 5))

# 10
# [3.9998677604457193, 1.0929742991482094e-09]

# 30
# [3.9999998095504217, 2.266940170740813e-15]

# 50
# [3.999743637340084, 4.107744972557486e-09]

print("zdt1")
run(testfunctions.zdt1, testfunctions.zdt2, 10, (10, 100000))
run(testfunctions.zdt1, testfunctions.zdt2, 30, (10, 100000))
run(testfunctions.zdt1, testfunctions.zdt2, 50, (10, 100000))

# 10
# [100000, -24999.999367943394]

# 30
# [100000, -19290.892130232685]

# 50
# [78664.52971318027, -16534.8090694192]

print("zdt3")
run(testfunctions.zdt31, testfunctions.zdt32, 10, (10, 100000))
run(testfunctions.zdt31, testfunctions.zdt32, 30, (10, 100000))
run(testfunctions.zdt31, testfunctions.zdt32, 50, (10, 100000))

# 10
# [98197.25454916802, -121735.46485826676]

# 30
# [90078.4467717645, -107242.5866240902]

# 50
# [94940.04094535224, -106707.42783968532]

print("zdt4")
run(testfunctions.zdt41, testfunctions.zdt42, 10, (10, 100000))
run(testfunctions.zdt41, testfunctions.zdt42, 30, (10, 100000))
run(testfunctions.zdt41, testfunctions.zdt42, 50, (10, 100000))

# 10
# [57681.37613536717, -14035.311562164678]

# 30
# [862.826822509246, 164702117.33277163]

# 50
# [580.410070217539, 1315236181.1265128]

print("zdt6")
run(testfunctions.zdt61, testfunctions.zdt62, 10, (10, 100000))
run(testfunctions.zdt61, testfunctions.zdt62, 30, (10, 100000))
run(testfunctions.zdt61, testfunctions.zdt62, 50, (10, 100000))

# 10
# [1.0, 918.8828010808786]

# 30
# [1.0, 221101106.83682972]

# 50
# [1.0, 1186231866.4275157]