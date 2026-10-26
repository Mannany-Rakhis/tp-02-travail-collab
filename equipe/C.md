# Équipe C

Pour travailler efficacement en équipe sur **GitHub**, il est essentiel d'isoler chaque tâche dans une **branche dédiée** (ex: `feature/nom-tache`) plutôt que de modifier directement la branche principale (`main`), qui doit toujours rester stable et prête pour le déploiement. Chaque développeur clone le dépôt, travaille sur sa branche locale, et pousse ses modifications via des **commits atomiques** accompagnés de messages descriptifs.

L'intégration du code se fait obligatoirement via des **Pull Requests (PR)**, qui servent de filtre qualité. Cette étape permet aux pairs de **réviser le code**, de discuter des changements et de lancer des **tests automatisés** (CI/CD). Une fois la PR approuvée et les conflits résolus, le code est fusionné dans `main`, assurant ainsi une collaboration structurée, sécurisée et traçable.
