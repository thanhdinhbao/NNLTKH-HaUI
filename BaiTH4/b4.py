import os
import shutil as st

os.mkdir("D:/BAI4")
st.copy('D:/iris.txt', 'D:/BAI4')
os.rename('D:/BAI4/iris.txt', 'D:/BAI4/iris.dat')
#chuyển tới thư mục BAI4
os.chdir('D:/BAI4')
#show nội dung thư mục
files = os.listdir()
for file in files:
    print(file)
#xóa file
os.remove('iris.dat')
#xóa thư mục rỗng
os.chdir('D:/')
st.rmtree('BAI4')
