# Оригинальная лр - https://github.com/grishutenko/upp-git

### Шпаргалка по командам git

 - git config --global user.name "Your Name" - имя автора commit'а
 - git config --global user.email "_@_._" - почта автора commit'а
 - git commit -a -m "Name of commit" - индексация отслеживаемых файлов и добавление в commit
 - git commit --amend -m "Название" - перекоммитить текущий коммит
 - git checkout 424323532 index.html - востановление файла из коммита с хешем 424323532
 - git rm text.txt - удалить из репозитория файл и проиндексировать изменение, ключ -r для деректории
 - git log master - показать commit'ы в ветке master 
 - git branch -v - казать список веток и последний commit в каждой
 - git fetch origin - скачать все файлы со всех веток из удаленного репозитория
 - git pull origin - скачать только измененные фвйлы со всех веток их удаленного репозитория
 - git merge other-branch - влить в активную ветку изменения из ветки other-branch
 - git checkout master - перключение в ветку master из другой ветки
 - git diff HEAD - сравнить рабочую директорию и commit, на который указывает HEAD (HEAD — указатель на текущий коммит или на текущую ветку)
 - git clone https://github.com/grishutenko/upp-git folder - клонирование файлов в folder
 - git blame README.md - показать строки, даты их изменения и имя автора коммита для файла README.md
 
