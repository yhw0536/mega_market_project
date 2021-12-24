# 명령어

- https://github.com/coreybutler/nvm-windows/releases 접속
- nvm-setup.zip 다운로드 후 설치
- cmd 접속
- nvm install v16.13.1
- nvm use v16.13.1
- /base/static/common.base.css 파일 생성
- common.base.css 파일내용

```
@tailwind utilities;
@font-face {
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
html > body {
    font-family: "GmarketSansMedium";
    text-underline-position: under;
}
```

- npx tailwindcss -i ./base/static/common.base.css -o ./base/static/common.css --watch
- 앞으로 개발할 때 마다 켜주세요.
- .gitignore 파일에 node_modules/ 추가
- 새로운 환경에서 시작할 때
- npm install
- npm run css
- python manage.py runserver