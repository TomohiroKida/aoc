tar Jcf YYYY.tar.xz YYYY/
gpg -r xx -ea YYYY.tar.xz
gpg -o YYYY.tar.xz -d YYYY.tar.xz.asc
tar xf YYYY.tar.xz
