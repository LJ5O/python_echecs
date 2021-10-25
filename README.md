# python_echecs 
Jeu d'échecs simple en python


# Version Console
**Pour la version Pygame, voir la branche Graphique**


# Comment jouer ?

Au lancement du jeu, le plateau est montré, ainsi qu'un input permettant à l'utilisateur de saisir les coordonnées du pion à déplacer
![Capture](https://user-images.githubusercontent.com/75009579/138706404-c5e599ed-c493-46cf-aa8d-988d4b0e08dc.PNG)

Pour séléctionner une pièce, il faut saisir les coordonnées X,Y, en se basant sur l'affichage du tableau. **La première valeur est x=0 !**

![Capture2](https://user-images.githubusercontent.com/75009579/138706995-9046466c-8d91-4102-abb8-45e5c3365f1c.PNG)

Une fois le pion séléctionné, le système demande les coordonnées de la case où le placer. Saisir ces coordonnées de la même manière. La validité de la nouvelle position est automatiquement vérifiée.
*Saisir 999 passera le tour*

![Capture3](https://user-images.githubusercontent.com/75009579/138707571-96229650-4daa-468a-82bf-b1a06d0e37f3.PNG)

Dès que le déplacement est validé, et que le pion est déplacé, le plateau est de nouveau affiché, et le joueur suivant peut jouer.
