# PATLITE_NH-FV_API
  
## 開発環境
- Python: 3.11.6  
  

## 実行方法
Pythonとgitの環境があることを前提にしています．  
localhostで動かす方法です．  
他の実行方法に関しては，よしなにしてください．  
  
1. 環境を作成  
このリポジトリをクローンする．  
```git clone git@github.com:mame7777/PATLITE_NH-FV_API.git```  
  
仮想環境を構築する．  
```python -m venv env```  
  
仮想環境を有効化する．(windows用のコマンド実行例)  
```.\env\Scripts\Activate.ps1```  
  
パッケージをインストールする．  
```pip install -r .\requirements.txt```  
  
  
2. webサーバを実行  
実行するだけなら`--reload`はなくてもよい．
```uvicorn main:app --reload```  
  
  
3. ブラウザからアクセス  
`http://localhost:8000/docs`にアクセスし，POSTの枠があり，`/api/lights_and_buzzer/[lights_and_buzzer]`と書かれた部分をクリックする．  
「Try it out」をクリックし，「lights_and_buzzer」の部分に数字を入力し「Execute」をクリックすると実行できる．  
数字は最初5文字がライト，次の1文字がブザーの制御であり，数字と動作の対応は製品説明書のPNSコマンドの部分と同様である． 
:::note info 
CLIで`curl`で既に動作確認できるので，その方法でもよい．
実行コマンド例：
```
curl -X 'POST' \
  'http://localhost:8000/api/lights_buzer/000000' \
  -H 'accept: application/json' \
  -d ''
```
:::