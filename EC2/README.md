# Amazon EC2
## 개요
- AWS 클라우드에서 가상의 컴퓨터 얻는다.
- 콘솔링크 : https://ap-northeast-2.console.aws.amazon.com/ec2/v2/home?region=ap-northeast-2
- 가이드시작: https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/concepts.html

## 인스턴스 생성 
- 콘솔 접속
- Linux - t2.micro 사용
- key pair 별도 저장

## 접속
- Windows > PuTTy 이용하여 접속
- 보안 그룹 생성(또는 변경) > 인바운드 > SSH-PORT22 허용
- 가이드 문서 : https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/putty.html

## Linux 명령어
- 필요할때마다 구글링! (ex. https://www.mireene.com/webimg/linux_tip1.htm )

## EC2에 프로그램 설치
### git
- sudo yum install git
- 정리 링크 : https://medium.com/sunhyoups-story/ec2-git-ac275a4e789c


### python3
- sudo yum install python36


### pip3
- curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
- python3 get-pip.py --user
- 이후 모듈 설치 : pip3 install modulename --user

### AWS CLI
- 관련 링크 : [aws guide] (https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-chap-tutorial.html)



### Google Chrome (+chromedriver) + selenium
- 한 방에 정리 링크! : https://medium.com/@praneeth.jm/running-chromedriver-and-selenium-in-python-on-an-aws-ec2-instance-2fb4ad633bb5


## 실행
- git clone [github link] / git pull origin master
- git checkout -b mybranch
- python3 myfile.py
- git add .
- git commit -m

