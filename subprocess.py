import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    # # basic
    # subprocess.run(["ls", "-ltr"])
    # subprocess.run(["python", "python_script101.py", "--x","8"])
    
    # # use output of subprocess
    # process1 = subprocess.Popen(["python", "python_script101.py", "--x","8"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, err = process1.communicate()
    # print(out.decode('utf-8'))


    #HW สั่งรัน python_script101.py 50 รอบ โดย x = 1,3,5,7,... 
    #แล้วให้เอา output ของ xt มารวมกัน แล้ว print ออกมา

    sum = 0 
    cou = 0
    for i in range(1,100,2):
            cou +=1
            process1 = subprocess.Popen(["python", "python_script101.py", "--x",f'{i}'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process1.communicate()
            print(f"({cou}) x= {i}")
            print(out.decode('utf-8'))
            sum += (i)
            
    print(f'   sum of x = {sum}')
    print(f'   sum of xt = {(sum)*2}')