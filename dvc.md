## Git DVC 연결

```

git init
git remote add origin <HTTP URL>

dvc init
dvc add <data file>

# <data file> : ./data/demo.txt

git add ./data/demo.txt.dvc
git add ./data/.gitignore
git commit -m <commit msg>

dvc remote add -d storage <remote storage URL>
dvc push

git add .dvc/config
git commit -m <commit msg>

```

## DVC pull

```
# test
rm -rf .data/demo.txt
dvc pull

# 파일이 수정된 경우 
echo "This is text" >> demo.txt
dvc add demo.txt
git add data.txt.dvc
git commit -m <commit msg>
git push origin <branch>
dvc push

```

## DVC checkout

```
git log --oneline
git checkout <commit hash> ./data/demo.txt.dvc
dvc checkout
cat ./data/demo.txt
```


