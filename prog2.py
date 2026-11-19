Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\kavya> cd C:\Users\Public
PS C:\Users\Public> mkdir 1GD25CI041
mkdir : An item with the specified name C:\Users\Public\1GD25CI041 already exists.
At line:1 char:1
+ mkdir 1GD25CI041
+ ~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceExists: (C:\Users\Public\1GD25CI041:String) [New-Item], IOException
    + FullyQualifiedErrorId : DirectoryExist,Microsoft.PowerShell.Commands.NewItemCommand

PS C:\Users\Public> Mkdir 1GD25CI041
Mkdir : An item with the specified name C:\Users\Public\1GD25CI041 already exists.
At line:1 char:1
+ Mkdir 1GD25CI041
+ ~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceExists: (C:\Users\Public\1GD25CI041:String) [New-Item], IOException
    + FullyQualifiedErrorId : DirectoryExist,Microsoft.PowerShell.Commands.NewItemCommand

PS C:\Users\Public> cd C:\Users\Public\1GD25CI041
PS C:\Users\Public\1GD25CI041> git config user.name "harshitamajjagi5353"
PS C:\Users\Public\1GD25CI041> git config user.email "harshitamajjagi53@gmail.com"
PS C:\Users\Public\1GD25CI041> git branch
* main
PS C:\Users\Public\1GD25CI041> git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\Public\1GD25CI041> git checkout -b new-branch
Switched to a new branch 'new-branch'
PS C:\Users\Public\1GD25CI041> git branch main
fatal: a branch named 'main' already exists
PS C:\Users\Public\1GD25CI041> git checkout -b feature-branch
Switched to a new branch 'feature-branch'
PS C:\Users\Public\1GD25CI041> git branch
* feature-branch
  main
  new-branch
PS C:\Users\Public\1GD25CI041> ni new -feature.txt
New-Item : A parameter cannot be found that matches parameter name 'feature'.
At line:1 char:8
+ ni new -feature.txt
+        ~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [New-Item], ParameterBindingException
    + FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.PowerShell.Commands.NewItemCommand

PS C:\Users\Public\1GD25CI041> ni new-feature.txt


    Directory: C:\Users\Public\1GD25CI041


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        19-11-2026     20:51              0 new-feature.txt


PS C:\Users\Public\1GD25CI041> Add content-feature the git branching
Add : The term 'Add' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ Add content-feature the git branching
+ ~~~
    + CategoryInfo          : ObjectNotFound: (Add:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\Public\1GD25CI041> Add-content feature the git branching
Add-Content : A positional parameter cannot be found that accepts argument 'git'.
At line:1 char:1
+ Add-content feature the git branching
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Add-Content], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.AddContentCommand

PS C:\Users\Public\1GD25CI041> Add-content -feature the git branching
Add-Content : A parameter cannot be found that matches parameter name 'feature'.
At line:1 char:13
+ Add-content -feature the git branching
+             ~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Add-Content], ParameterBindingException
    + FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.PowerShell.Commands.AddContentCommand

PS C:\Users\Public\1GD25CI041> add-content feature the git branching
Add-Content : A positional parameter cannot be found that accepts argument 'git'.
At line:1 char:1
+ add-content feature the git branching
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Add-Content], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.AddContentCommand

PS C:\Users\Public\1GD25CI041> add content-feature the git branching
add : The term 'add' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ add content-feature the git branching
+ ~~~
    + CategoryInfo          : ObjectNotFound: (add:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\Public\1GD25CI041> add-content feature the git branching
Add-Content : A positional parameter cannot be found that accepts argument 'git'.
At line:1 char:1
+ add-content feature the git branching
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Add-Content], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.AddContentCommand

PS C:\Users\Public\1GD25CI041> add-content new-feature.txt "feature the git branching"
PS C:\Users\Public\1GD25CI041> cat new -feature git branching
Get-Content : A parameter cannot be found that matches parameter name 'feature'.
At line:1 char:9
+ cat new -feature git branching
+         ~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Get-Content], ParameterBindingException
    + FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.PowerShell.Commands.GetContentCommand

PS C:\Users\Public\1GD25CI041> cat new-feature git branching
Get-Content : A positional parameter cannot be found that accepts argument 'git'.
At line:1 char:1
+ cat new-feature git branching
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Get-Content], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.GetContentCommand

PS C:\Users\Public\1GD25CI041> cat new-feature.txt
feature the git branching
PS C:\Users\Public\1GD25CI041> git add new-feature.txt
PS C:\Users\Public\1GD25CI041> git status
On branch feature-branch
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   new-feature.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ed
        prog2.py

PS C:\Users\Public\1GD25CI041> git commit -m "add new-feature.txt in new branch"
[feature-branch dbaa74b] add new-feature.txt in new branch
 1 file changed, 1 insertion(+)
 create mode 100644 new-feature.txt
PS C:\Users\Public\1GD25CI041> git push -u origin feature-branch
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 324 bytes | 162.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'feature-branch' on GitHub by visiting:
remote:      https://github.com/harshitamajjagi5353/1GD25CI041/pull/new/feature-branch
remote:
To https://github.com/harshitamajjagi5353/1GD25CI041.git
 * [new branch]      feature-branch -> feature-branch
branch 'feature-branch' set up to track 'origin/feature-branch'.
PS C:\Users\Public\1GD25CI041> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\Public\1GD25CI041> git merge feature-branch
Updating 20841af..dbaa74b
Fast-forward
 new-feature.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 new-feature.txt
PS C:\Users\Public\1GD25CI041> dir


    Directory: C:\Users\Public\1GD25CI041


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        19-11-2026     11:05              0 ed
-a----        19-11-2026     10:41             26 myfile.txt
-a----        19-11-2026     21:05             27 new-feature.txt
-a----        19-11-2026     12:31              0 prog2.py


PS C:\Users\Public\1GD25CI041> git log --oneline
dbaa74b (HEAD -> main, origin/feature-branch, feature-branch) add new-feature.txt in new branch
20841af (origin/main, new-branch) myfirst commit
PS C:\Users\Public\1GD25CI041> git push
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/harshitamajjagi5353/1GD25CI041.git
   20841af..dbaa74b  main -> main
PS C:\Users\Public\1GD25CI041> git push -u origin feature-branch
branch 'feature-branch' set up to track 'origin/feature-branch'.
Everything up-to-date
PS C:\Users\Public\1GD25CI041> notepad prog2.py
PS C:\Users\Public\1GD25CI041>










