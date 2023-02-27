## Git DVC 연결

```

git init
git remote add origin <HTTP URL>

dvc init
dvc add <data file>

# <data file> : ./data/demo.txt

git add ./data/demo.txt.dvc
git add ./data/.gitignore
git commit -m <commit message>

dvc remote add -d storage <remote storage URL>
dvc push

git add .dvc/config
git commit -m <commit message>

```

## DVC pull

```
# test
rm -rf .data/demo.txt
dvc pull

# 파일이 수정된 경우 
echo "This is text" >> demo.txt




```