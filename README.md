# E365-dynamic-IP_by_service

 English:
 
 this script is a customization of the microsoft script, it allows to extract the IP of some services of microsoft to integrate them in a file txt for feeds / dynamic ip list. it can be started by a task scheduled to be up to date.   example : for extract all IP of  *.mail.protection.outlook.com      ... 
 
 purpose: update dynamic lists on routers, to allow it and route the communication with exchange online services.
 for my case, hybrid exchange so * .mail.protection.outlook.com.
 
 
 Francais:
 ce script est une personnalisation du script de microsoft , il permet extraire les  adresses IP  de certains services de microsoft  pour les integrer dans un fichier txt  pour des creer  feeds / dynamic ip list  automatiquement . 
 il peut etre lancé par une tache planifié  pour etre a jour regulierement .
 
 but : mettre a jour des listes dynamiques sur des routeurs , pour la permettre et router  les communication avec des services exchange online . 
 pour mon cas , exchange hybride  donc *.mail.protection.outlook.com . 
 
configuration  possible :
   -champs de recherche  (ndd_extract)
   -emplacement du fichier   ( datapath )
   -affiche un retour dans la console  ( show )

 
 
 
 source du script : https://docs.microsoft.com/fr-fr/office365/enterprise/office-365-ip-web-service
 info sur les ip microsoft : https://docs.microsoft.com/fr-fr/office365/enterprise/urls-and-ip-address-ranges?redirectSourcePath=%252farticle%252f8548a211-3fe7-47cb-abb1-355ea5aa88a2
