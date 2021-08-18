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

* Postman (Back-end Testing)

### 구현해야 할 기능

#### 로그인
> · 유저로부터 아이디와 비밀번호 정보를 입력받아 로그인    
> · 아이디, 비밀번호는 필수 입력사항    
> · 로그인 유저에 대해 session으로 관리하기    
> · 비밀번호는 특정 조건에 맞춰 최소 8자리 이상의 길이    
> · 아이디는 이메일 형식으로만 입력받기

#### 회원가입
> · 유저로부터 아이디, 비밀번호, 이름 정보를 입력받아 로그인     
> · 비밀번호와 비밀번호 확인 값이 일치해야 함          
> · 아이디는 이메일 형식으로만 입력받기             
> · 이름은 한글, 영문으로만 입력받기            
> · 비밀번호는 특정 조건에 맞춰 입력받기             

#### 로그아웃
> · session에서 현재 로그인된 유저를 제거

#### 메인 페이지
> · 현재 db상 존재하는 모든 책 정보를 출력            
> · 현재 db상 존재하는 남은 책 수를 출력           
> · 책 이름 클릭 시 책 소개 페이지로 이동               
> · 책의 평점은 현재 db상 담긴 모든 평점의 평균임, 소수점 첫째 자리에서 반올림

#### 대여하기
> · 메인 페이지의 대여하기 버튼 클릭                      
> · 현재 db상 책이 없는 경우 대여가 안 됨                    
> · 현재 db상 책이 존재하는 경우 책을 대여 후 책 권수를 -1

#### 반납하기
> · 로그인 유저가 대여한 책을 모두 보여줌
> · 반납하기 버튼을 클릭하면 책을 반납, 책을 반납 후 책 권수를 +1

#### 책 소개
> · 메인 페이지의 책 이름을 클릭하여 접근함      
> · 책에 대한 소개 출력     
> · 가장 최신 리뷰부터 보이도록     
> · 댓글을 작성하면서 책 평점 기입            
> · 댓글, 평점은 모두 필수 입력사항

#### 대여 기록
> · 로그인한 유저가 대여 후 반납했던 책에 대한 모든 사항 출력하기