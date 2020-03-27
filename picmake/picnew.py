#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random
import math
import sqlite3
from PIL import Image, ImageDraw, ImageFont, ImageFilter

step = 15
#step = 1
W = 60*step
H = 30*step
h_h1 = 8*step
h_h2 = 3*step
h_h3 = 2*step
RGBbg = (220,220,220)
fontstr = "phetsarath_ot.ttf"
techbox = ["Algorithm","DataStructure","ComputerNetwork","AI","MachineLearning","Operation System","Statistics","Cyber Security","Data Mining","Big Data","Math","Compilation"," C ","C++","Java","Python","Scala",
"Matlab","C#"," R ","Javascript","Go","Ruby","Linux Shell","Perl","Multi-thread","Database","Mysql","Oracle","Nosql","Mongodb","Postgresql","Haskhell","Racket","Scheme","Prolog","X86",
"Mips","Arm","Assembly","Lc3","Php","Nodejs","Java Web","Flask","Django","ReactJS","Vue","Anjularjs","Asp","Ajax","D3.js","Ruby on rails","Tkinter","Pyqt","Unity3D","Java Swing","JavaFx",
"Pygame","Opencv","Opengl","Webgl","QT","ios","Android","Cuda","Mpi","Mathematica","Report"
]
techbox1 = ["Algorithm","DataStructure","ComputerNetwork","AI","MachineLearning","Operation System","Statistics","Cyber Security","Data Mining","Big Data","Math","Compilation"," C ","C++","Java","Python","Scala",
"Matlab","C#"," R ","Javascript","Go","Ruby","Linux Shell","Perl","Multi-thread","Database","Mysql","Oracle","Nosql","Mongodb","Postgresql","Haskhell","Racket","Scheme","Prolog","X86",
"Mips","Arm","Assembly","Lc3","Php","Nodejs","Java Web","Flask","Django","ReactJS","Vue","Anjularjs","Asp","Ajax","D3.js","Ruby on rails","Tkinter","Pyqt","Unity3D","Java Swing","JavaFx",
"Pygame","Opencv","Opengl","Webgl","QT","ios","Android","Cuda","Mpi","Mathematica","Report"
]
textbox  = techbox + techbox1
textbox2 = ["HW","Assignment","Project","Lab","Homework"]
transparent = 100
#techbox = ["Javascrip"]
class Rect:
 
   def __init__(self, x, y,width,height):
      self.x = x
      self.y = y
      self.width = width
      self.height = height
def printf(screen):
    for i in range(0,H):
        for j in range(0,W):
            print(screen[i][j],end="") # i =  h  j = w
        print()
    pass
def drawinit(rect,screen):
    for i in range(0,H):#y
        for j in range(0,W):#x
            if j >=rect.x and j< (rect.x + rect.width) and i >= rect.y and i< (rect.y + rect.height):
                #print("* ",end="")
                screen[i][j] = "* "
    return screen
def drawrect0(rect,screen):
    #formats = rect.H + math.sqrt(1-())
    #j = 30
    #print( math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)))
    for i in range(0,rect.width):#y
        for j in range(0,rect.width):#x
            if j >=rect.x and j< (rect.x + rect.width) and i >= rect.y and i< (rect.y + rect.height) and i <= (rect.height - math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)) ):
                #print("* ",end="")
                screen[i][j] = "* "
    return screen
def drawrect1(rect,screen):
    #formats = rect.H + math.sqrt(1-())
    #j = 30
    #print( math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)))
    for i in range(rect.y,rect.height + rect.y):#y
        for j in range(0,rect.width):#x
            #print(rect.width*rect.width-(j-rect.width)*(j-rect.width))
            if j >=rect.x and j< (rect.x + rect.width) and i >= rect.y and i< (rect.y + rect.height) :
                #print("* ",end="")
                
                if i >= (rect.y + math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)) ):
                    screen[i][j] = "* "
                    #print(math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)))
                    #print("y:" + str(i))
                    #print("x:" + str(j))
                    #print("####")
                    pass
                
    return screen
def drawrect2(rect,screen):
    #formats = rect.H + math.sqrt(1-())
    #j = 30
    #print( math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)))
    for i in range(0,rect.height):#y
        for j in range(rect.x,rect.x + rect.width):#x
            if j >=rect.x and j< (rect.x + rect.width) and i >= rect.y and i< (rect.y + rect.height) and i <= (rect.height - math.sqrt(rect.width*rect.width-(j-rect.x)*(j-rect.x)) ):
                #print("* ",end="")
                screen[i][j] = "* "
    return screen
def drawrect3(rect,screen):
    #formats = rect.H + math.sqrt(1-())
    #j = 30
    #print( math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)))
    for i in range(rect.y,rect.height + rect.y):#y
        for j in range(rect.x,W):#x
            #print(rect.width*rect.width-(j-rect.width)*(j-rect.width))
            if j >=rect.x and j< (rect.x + rect.width) and i >= rect.y and i< (rect.y + rect.height) :
                #print("* ",end="")
                
                if i >= (rect.y + math.sqrt(rect.width*rect.width-(j-rect.x)*(j-rect.x)) ):
                    screen[i][j] = "* "
                    #print(math.sqrt(rect.width*rect.width-(j-rect.width)*(j-rect.width)))
                    #print("y:" + str(i))
                    #print("x:" + str(j))
                    #print("####")
                    pass
                
    return screen
# 输入react  画出来  前置条件可遍历画布 按规格画
def drawother(rect,screen):
    if rect.y + rect.height > H or rect.x + rect.width >W:
        return [0,screen]
    else:
        for ii in range(rect.y,rect.y + rect.height):
            for jj in range(rect.x,rect.x + rect.width):
                #print(screen[ii][jj],end="")
                '''
                if rect.x >0 :
                    if(screen[ii][jj-1] == "* "):
                        return [0,screen]
                if rect.y >0 :
                    if(screen[ii-1][jj] == "* "):
                        return [0,screen]
                '''
                if(screen[ii][jj] == "* "):
                    return [0,screen]
            #print()
        screen = drawinit(rect,screen)
        return [1,screen]
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
def main(maintext):
    screen = []
    for i in range(0,H):
        screen.append([". "]*W)
    bgimg = Image.new('RGBA', (W,H), RGBbg)
    #bgimg.save('bg.jpg')
    #printf(screen)
    init_w = int(h_h1/2.6*len(maintext))

    init_rect = Rect(W-init_w - 8*step,13*step,init_w,h_h1)
    init_img = Image.new('RGBA', (init_rect.width,init_rect.height),color=transparent)  
    draw = ImageDraw.Draw(init_img)
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 1
    font = ImageFont.truetype(fontstr, fontsize)
    while font.getsize(maintext)[0] < img_fraction*init_rect.width:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(fontstr, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -=1
    font = ImageFont.truetype(fontstr, fontsize)
    draw.text((0 ,0), maintext, font=font, fill=rndColor2())
    outitem = {}
    outitem["box"] =  (init_rect.x, init_rect.y, init_rect.x + init_rect.width, init_rect.y+init_rect.height)
    init_img = init_img.resize((outitem["box"][2] - outitem["box"][0], outitem["box"][3] - outitem["box"][1]))
    #init_img.save(maintext+".png")
    r,g,b,a = init_img.split()
    bgimg.paste(init_img, outitem["box"],mask=a)
    '''
    for i in range(0,H):#y
        for j in range(0,W):#x
            print(".",end="")
        print()
    '''
    screen = drawinit(init_rect,screen)
    rect0 = Rect(0*step,0*step,10*step,10*step)
    rect1 = Rect(0*step,H-10*step,10*step,10*step)
    rect2 = Rect(W-10*step,0,10*step,10*step)
    rect3 = Rect(W-10*step,H-10*step,10*step,10*step)
    screen = drawinit(init_rect,screen)
    screen = drawrect0(rect0,screen)
    screen = drawrect1(rect1,screen)
    screen = drawrect2(rect2,screen)
    screen = drawrect3(rect3,screen)
    #screen = drawinit(rect2,screen)
    #screen = drawinit(rect3,screen)
    #printf(screen)
    #return 
    #screen = draw(rect_h2,screen)
    # 探索  生成宽（字体长度），高（h ... ）， --> 方向互换
    hbox = [h_h2,h_h3]
    textflag = 0
    outputs = []
    positionbox = [1,1,1,1,1,1,0,0]
    for i in range(0,1900000):
        text = techbox[textflag]
        pf = random.sample(positionbox, 1)[0]
        if pf == 1:
            rx = random.randint(W/6,5*W/6)
            ry = random.randint(int(H/3),int(2*H/3))
        else:
            rx = random.randint(0,W)
            ry = random.randint(0,H)
        
        rw = 0
        rh = random.sample(hbox, 1)[0]
        if rh == h_h2:
            rw = int(rh/2.65*len(text))
            if rw< rh:
                rw = int(rh)
                pass
        else:
            rw = int(rh/2.65*len(text))
            if rw< rh:
                rw = int(rh)
                pass
        flag = random.sample([0,1], 1)[0]
        #flag = 0
        tmp = Rect(rx,ry,rw,rh)# zoom + 
        if flag == 0:
            tmp = Rect(rx,ry,rw,rh)# zoom + 
        else:
            tmp = Rect(rx,ry,rh,rw)# zoom + 
        res = drawother(tmp,screen)
        screen = res[1]
        if(res[0] == 1):
            flagwidth = 0
            #picbox = (tmp.x, tmp.y, tmp.x + tmp.width, tmp.y+tmp.height)
            outitem = {}
            outitem["box"] =  (tmp.x, tmp.y, tmp.x + tmp.width, tmp.y+tmp.height)
            outitem["flag"] = flag
            outitem["name"] = text+".png"
            outputs.append(outitem)
            if flag == 0:
                cellimg = Image.new('RGBA', (tmp.width,tmp.height),color=transparent)  
                flagwidth = tmp.width  
            else:
                cellimg = Image.new('RGBA', (tmp.height,tmp.width),color=transparent)  
                flagwidth = tmp.height
            draw = ImageDraw.Draw(cellimg)
            fontsize = 1  # starting font size

            # portion of image width you want text width to be
            img_fraction = 1
            font = ImageFont.truetype(fontstr, fontsize)
            while font.getsize(text)[0] < img_fraction*flagwidth:
                # iterate until the text size is just larger than the criteria
                fontsize += 1
                font = ImageFont.truetype(fontstr, fontsize)

            # optionally de-increment to be sure it is less than criteria
            fontsize -=5
            font = ImageFont.truetype(fontstr, fontsize)
            draw.text((0 ,0), text, font=font, fill=rndColor2())
            #cellimg.save(text +'.png')  
            print(outitem["name"])
            if outitem["flag"] == 1 :
                cellimg = cellimg.rotate(90,expand=1)
            #cellimg.save(item["name"])
            #continue
        
            cellimg = cellimg.resize((outitem["box"][2] - outitem["box"][0], outitem["box"][3] - outitem["box"][1]))
            r,g,b,a = cellimg.split()
            bgimg.paste(cellimg, outitem["box"],mask=a)
            textflag = textflag + 1
            if textflag >=len(techbox):
                textflag = 0
            #cellimg = cellimg.resize((picbox[2] - picbox[0], picbox[3] - picbox[1]))
            #bgimg.paste(cellimg, picbox)
            

            #cellimg.save(str(rw)+'_'+str(rh)+'.png')  
        else:
            #print("wrong position")
            pass
    wbox = (0,0,W,H)
    wimg = Image.open("./bg/bg.png")#
    wimg = wimg.resize((W, H))
    r,g,b,a = wimg.split()
    bgimg.paste(wimg, wbox,mask=a)
    bgimg.save('./output/'+maintext+".png")        
    print(i)
    #printf(screen)
    return
    for item in outputs:
        #print(item)
        cellimg = Image.open(item["name"])#
        if item["flag"] == 1 :
            print(item["name"])
            cellimg = cellimg.rotate(90,expand=1)
            #cellimg.save(item["name"])
            #continue
        
        cellimg = cellimg.resize((item["box"][2] - item["box"][0], item["box"][3] - item["box"][1]))
        r,g,b,a = cellimg.split()
        bgimg.paste(cellimg, item["box"],mask=a)
    bgimg.save('output/out.png')   
    
#main(name)
prefix = "/wp-content/uploads/2019/08/"
conn = sqlite3.connect('../sendWP.db')
conn.text_factory = str
cursor = conn.cursor()
cursor.execute('select * from pdftags where imgurl is NULL')
values = cursor.fetchall()

for item in values:
    print("# Handle with " + item[1])
    cursor.execute("UPDATE pdftags SET imgurl=? WHERE id=?", (prefix +item[1] + ".png", item[0]))
    conn.commit()
    break
    #main(item[1])
conn.close()
'''
for name in textbox2:
    print("# Handle with " + name)
    main(name)
    break
'''