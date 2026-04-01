1 Etude du problème d’optimisation

1. Interpréter le coût (2) et en particulier le terme min {q, d}.
Le profit de la boulangerie se définit comme les revenus moins les coûts d'où la définition de la fonction. min{q,d} signifie que pour chaque produit j, si on a une quantité supérieure à la demande, on peut fournir tous les clients et sinon, on écoule tout le produit. Ainsi, vTmin représente les revenus totaux obtenus par les ventes et cTr représente le total des coûts d'achat de matière première.

2. Quelle difficulté présente ce dernier terme dans le cadre d’un algorithme d’optimisation ?
La fonction min que l'on peut définir par min(a,b)=(-|a-b|+a+b)/2 n'est pas défférentiable sur R^2 à cause de la valeur absolue, ce qui pose un problème de convergence des simulations (comme vues en cours par la méthode de descente de gradient par exemple). 

