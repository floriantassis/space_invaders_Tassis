# space_invaders_Tassis

Florian TASSIS
---------------------------------------------------------------

OBJECTIF :

Le but de ce projet est de réalisé, en python, le jeu space invaders à notre manière
Ce jeu consiste à détruire des robots ennemis qui nous tire dessus. Pour cela, utiliser le bouton poussoir présent sur la carte afin de pouvoir détruire les ennemis. Nous allons ausi utiliser l'accéléromètre présent sur la carte afin de déplacer le robot. Sortirons nous vainqueur de cette guerre où la pitié n'a pas sa place? Bah on verra déjà si on arrive à le coder.
    
---------------------------------------------------------------

LANCER LE JEU :

Afin de jouer au jeu il faudra tout d'abord mettre python sur la carte, car ce n'est pas un langage prévu de base par la carte.
Il faudra alors suivre les étapes suivantes :

    Téléchargez le programme de flashage : https://github.com/micropython/micropython/blob/master/tools/pydfu.py
        Par exemple : https://github.com/micropython/micropython/blob/cdaec0dcaffbfcb58e190738cf6e9d34541464f0/tools/pydfu.py

    Créez un environnement virtuel, avec un shell
        cd  le_dossier_qui_va_bien
        python3.8 -m venv    venv
    Activez l'environnement virtuel
        source venv/bin/activate 
    (venv) est ajouté au début du promptpip  
        install pyusb==1.1.1
        
    Sur STM32F4 Discovery
        https://www.micropython.org/download#other  -> Prenez la dernière version stable
    
    Débranchez la STM32F4 Discovery et mettez un jumper entre VDD et BOOT0
    
    Branchez un câble mini-USB en haut de la STM32F4-Discovery
    Branchez un câble micro-USB en bas de la STM32F4-Discovery
    
    Rentrez les commandes suivantes :
       " python pydfu.py --list "
       " python pydfu.py --upload STM32F4DISC-20210222-v1.14.dfu "
    
    Ejectez la clé USB
    Retirez le Jumper
    Appuyez sur le bouton poussoir noir (Reset)
    
    Remplacez le contenu de " main.py " par le contenu de " space_invaders.py " 
    
    Enregistrer le programme
    Ejectez la clé USB
    Appuyez sur le bouton poussoir noir (Reset)
    
    Enfin démarrez un terminal MicroPython avec la commande suivante :
       " sudo screen /dev/ttyUSB0 115200 "
    
    Vous pouvez a présent profiter du jeu, il ne vous reste qu'à profiter ! 

---------------------------------------------------------------

DIFFICULTES RENCONTRÉES :

Ce projet m'a permis de développer certaines compétences et d'appliquer ce que nous avons appris en cours. Il me manquer cependant l'utilisation des classes qui m'aurait bien aidé. J'ai en effet essayer de les utiliser mais je pense que je faisait des erreurs qui m'ont empéché de pouvoir plus avancer ce projet. Ces problèmes m'ont fait perdre beaucoup de temps et je n'ai donc pas pu finir ce projet dans les temps. De plus, je n'ai pas forcément l'habitude de coder en python et je garde certains automatismes du C qui ne sont pas compatible avec python ce qui me fait également perdre du temps. 

J'ai aussi rencontré des difficultés dans le fait d'afficher tous les robots ennemis et de les faire bouger en même temps.

 ---------------------------------------------------------------

RETOUR SUR LE PROJET :
Je trouve l'idée de réaliser ce projet très bonne. En effet, elle nous permet d'utiliser les compétences acquises en théories dans un projet ludique qui nous donne envie d'aller au bout. Je trouve que nous sommes bien accompagné durant tout le long du projet. Je n'ai cependant pas eu le temps  de finir ce projet car j'ai eu certains problèmes personnels ces derniers temps. Je vais esayer de le finir pendant mon temps libre afin d'améliorer mes compétences en python. En bref, j'ai trouvé très intéressant ce projet et la façon dont il a été mené.
