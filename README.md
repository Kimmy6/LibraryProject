도서관 대출 서비스 (2기 김민성)
============================

## 프로젝트에 사용할 프로그램 및 패키지

### 개발 환경: Visual Studio Code

* Python (Back-end)
  + Flask
  + SQLAlchemy
  + PyMySQL
  + ajax
  + ...

* HTML (Front-end)
  + Vanilla HTML
  + Jinja2
  + JavaScript
  + ...

* Postman

## 구현해야 할 기능

* 로그인
  + User에서 ID(email), PW를 받아 로그인, session으로 관리

* 회원가입
  + User에서 ID, PW, 이름을 받아 회원가입
  + ID는 무조건 email형식, 이름은 무조건 한글/영어
  + PW는 특정 조건에 따라 작성

* 로그아웃
  + session에서 현재 로그인된 유저를 제거

* 메인 페이지
  + 현재 DB상에 존재하는 모든 책 정보와 남은 책 수를 표시
  + 책 이름 클릭 시 소개 페이지로 이동
  + 책 평점은 소수점 첫째자리에서 반올림

* 대여
  + 메인 페이지의 대여하기 버튼을 눌러 실행
  + DB상에 책이 존재하지 않는 경우 대여하지 못함, 대여 불가능 메시지 출력
  + 책을 대여하는 경우 남은 권 수에서 -1을 함
  + 같은 책을 대여할 경우 이미 대여했다는 메시지 출력

* 반납
  + 로그인 유저가 대여한 모든 책 표시 및 책에 대한 소개 출력

* 책 소개
  + 메인페이지의 책 이름을 클릭하여 접근, 책 소개 페이지로 이동
  + 댓글(이름, 평점, 내용) 표시

