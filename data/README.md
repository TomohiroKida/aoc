# comp
- tar Jcf YYYY.tar.xz YYYY/
- gpg -r xx -ea YYYY.tar.xz
# decomp
- gpg -o YYYY.tar.xz -d YYYY.tar.xz.asc
- tar xf YYYY.tar.xz

# data directory tree
- ./data/
-- YYYY/
--- DD_input_test_N.txt
--- DD_input.txt
