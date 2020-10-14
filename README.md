# G1
## System operating procedure(システム開始手順)
1. Run program "sockect_host.py" on the server.
```
[ec2-user@ip-172-31-39-61 ~]$ python3 socket_host.py 
```
2. Run program "human-sensor.py" on the Raspberry pi.

## About folders and files in here
### ・[DA] folder
　デモ用のwebサイトに関するファイル   
  Files about web dite about demonstration.
### ・[counter/keras-yolo3] folder  
　人の検知・人数のカウントに関するファイル(最終版には不使用)  
  Files about detection and counting of people (It was not used to new version). 
### ・[mask] folder  
　マスク検出に関するファイル  
  Files about detection masks on face.
### ・people-distance.py
  人の距離の計算をするプログラム   
  This program calculate distance.
### ・how2connec.txt  
　次の2つのファイルの説明文  
 Descriptions of the following 2 files the following.
  ```
  showStat.py
  socket_host.py
  ```
### ・takeSendPic.sh
　カメラと"showstat.py"の実行   
  Running the camera and "showstat.py".
### ・LEDproc.py
　LEDの動作  
　Operate LED rights.
### ・human-sensor.py
　人感知センサの動作  
 Operate human-detection-sensor.
   
   
以下、テスト用プログラム
#### ・G1_test.py
#### ・G1_test2.py
#### ・LED_test.py
#### ・LEDkill.py
#### ・test_camera.py
