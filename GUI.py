import pygame as py
from Astar import *
py.init()
class Button:
    def __init__(self,**kwargs):
        self.bg1=kwargs['bg1']
        self.fg1=kwargs['fg1']
        self.font=kwargs['font']
        self.text=kwargs['text']
        self.sizex=kwargs['sizex']
        self.sizey=kwargs['sizey']
        self.bg2=kwargs['bg2']
        self.fg2=kwargs['fg2']
    def show(self,surface,x,y):
        py.draw.rect(surface,self.bg1,(x,y,self.sizex,self.sizey))
        text=py.font.SysFont(self.font[0],self.font[1]).render(self.text,True,self.fg1)
        rectT=text.get_rect()
        rectT.center=(x+self.sizex//2,y+self.sizey//2)
        surface.blit(text,rectT)
        if py.mouse.get_pos()[0]>=x and py.mouse.get_pos()[1]<=y+self.sizey and py.mouse.get_pos()[0]<=x+self.sizex and py.mouse.get_pos()[1]>=y:
            py.draw.rect(surface,self.bg2,(x,y,self.sizex,self.sizey))
            text=py.font.SysFont(self.font[0],self.font[1]).render(self.text,True,self.fg2)
            rectT=text.get_rect()
            rectT.center=(x+self.sizex//2,y+self.sizey//2)
            surface.blit(text,rectT)
            if py.mouse.get_pressed()[0]:
                return True
            else:
                return False
        return False
class MainApp:
    def __init__(self,width=600,height=600):
        self.surface = py.display.set_mode((width, height))
        self.data= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
        self.sizex=50
        self.sizey=50
        self.positionChoice=[]
        self.distancex=50
        self.distancey=50
        self.btnSolve=Button(bg1=(128,128,128),fg1=(255,255,255),font=('Times',20),text='Giải',sizex=100,sizey=50,bg2=(0,128,128),fg2=(0,255,255))
    def run(self,FPS=30):
        clock=py.time.Clock()
        while True:
            clock.tick(FPS)
            self.display()
            for ev in py.event.get():
                if ev.type==py.QUIT:
                    return
                if ev.type==py.MOUSEBUTTONDOWN:
                    pos=py.mouse.get_pos()
                    x=int((pos[0]-self.distancex))//self.sizex
                    y=int((pos[1]-self.distancey))//self.sizey
                    if x>=0 and x<10 and y>=0 and y<10:
                        if ev.button==1 :
                                if len(self.positionChoice)>1:
                                    self.data[self.positionChoice[0][0]][self.positionChoice[0][1]]=0
                                    self.positionChoice.pop(0)
                                self.positionChoice.append((y,x))
                                try:
                                    self.data[self.positionChoice[0][0]][self.positionChoice[0][1]]=-1
                                    self.data[self.positionChoice[1][0]][self.positionChoice[1][1]]=-1 
                                except:
                                    pass   
                        if ev.button==3:
                            if self.data[y][x]==1:
                                self.data[y][x]=0
                            else:
                                self.data[y][x]=1         
            py.display.update()
    def convertData(self,path):
        for i in path[1:-1]:
            self.data[i[0]][i[1]]=2
    def refeshData(self):
        for i in range (len(self.data)):
            for j in range (len(self.data[0])):
                if self.data[i][j]==2:
                    self.data[i][j]=0
    def display(self):
        self.surface.fill((255,255,255))
        self.drawData()
        if self.btnSolve.show(self.surface,self.distancex+self.sizex*4,self.distancey+self.sizey*10):
            self.refeshData()
            path=astar(self.data,self.positionChoice[0],self.positionChoice[1])
            self.convertData(path)
    def drawData(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                py.draw.rect(self.surface,(0,0,0),(self.distancex+j*self.sizex,self.distancey+i*self.sizey,self.sizex,self.sizey),5)
                if self.data[i][j]==1:
                    color=(0,0,0)
                elif self.data[i][j]==0:
                    color=(255,255,255)
                elif self.data[i][j]==2:
                    color=(255,0,0)
                elif self.data[i][j]==-1:
                    color=(0,255,0)
                py.draw.rect(self.surface,color,(self.distancex+j*self.sizex,self.distancey+i*self.sizey,self.sizex,self.sizey))
if __name__ == '__main__':
    #ấn phải chuột để tạo/xóa ô cản
    #ẩn trái chuột để tạo ô bắt đầu, kết thúc, ấn nút giải để tìm đường đi
    MainApp().run()