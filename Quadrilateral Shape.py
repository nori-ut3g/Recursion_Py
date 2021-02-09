# ここから書いてください
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint


class QuadrilateralShape:
    def __init__(self, lineA, lineB, lineC, lineD):
        self.ax = lineA.startPoint.x; self.ay = lineA.startPoint.y
        self.bx = lineB.startPoint.x; self.by = lineB.startPoint.y
        self.cx = lineC.startPoint.x; self.cy = lineC.startPoint.y
        self.dx = lineD.startPoint.x; self.dy = lineD.startPoint.y

        #ABCDが四角形か判断
        if (lineA.endPoint.x == lineB.startPoint.x and lineA.endPoint.y == lineB.startPoint.y) and \
                (lineB.endPoint.x == lineC.startPoint.x and lineB.endPoint.y == lineC.startPoint.y) and \
                (lineC.endPoint.x == lineD.startPoint.x and lineC.endPoint.y == lineD.startPoint.y) and \
                (lineD.endPoint.x == lineA.startPoint.x and lineD.endPoint.y == lineA.startPoint.y):
            self.quadrangle = True

        #DCBAが四角形か判断
        elif (lineA.endPoint.x == lineD.startPoint.x and lineA.endPoint.y == lineD.startPoint.y) and \
                (lineD.endPoint.x == lineC.startPoint.x and lineD.endPoint.y == lineC.startPoint.y) and \
                (lineC.endPoint.x == lineB.startPoint.x and lineC.endPoint.y == lineB.startPoint.y) and \
                (lineB.endPoint.x == lineA.startPoint.x and lineB.endPoint.y == lineA.startPoint.y):
            self.quadrangle = True
        else:
            self.quadrangle = False

        #linelength
        self.lineAlength = ((self.ax-self.bx)**2+(self.ay-self.by)**2)**0.5
        self.lineBlength = ((self.bx-self.cx)**2+(self.by-self.cy)**2)**0.5
        self.lineClength = ((self.cx-self.dx)**2+(self.cy-self.dy)**2)**0.5
        self.lineDlength = ((self.dx-self.ax)**2+(self.dy-self.ay)**2)**0.5
        #angle
        self.angleA = self.angleCalc(self.bx, self.by, self.ax, self.ay, self.dx, self.dy)
        self.angleB = self.angleCalc(self.ax, self.ay, self.bx, self.by, self.cx, self.cy)
        self.angleC = self.angleCalc(self.bx, self.by, self.cx, self.cy, self.dx, self.dy)
        self.angleD = self.angleCalc(self.ax, self.ay, self.dx, self.dy, self.cx, self.cy)


    def angleCalc(self,a1,a2,b1,b2,c1,c2):
        a1 -= b1; a2 -= b2
        c1 -= b1; c2 -= b2
        cosine=(a1*c1+a2*c2)/(((a1**2+a2**2)**0.5)*((c1**2+c2**2)**0.5))
        return round((math.degrees(math.acos(cosine))),1)

    def getShapeType(self):
        if not self.quadrangle:
            return "四角形ではありません"

        #Square
        if self.lineAlength == self.lineBlength and self.lineAlength == self.lineClength and self.lineAlength == self.lineDlength:
            if self.angleA == 90:
                return('square（正方形）')
            else:
                return('rhombus（ひし形）')
        elif self.lineAlength == self.lineClength and self.lineBlength == self.lineDlength:
            if self.angleA == 90:
                return('rectangle（長方形）')
            else:
                return('parallelogram(平行四辺形)')
        elif self.lineAlength == self.lineClength or self.lineBlength == self.lineDlength:
            return('trapezoid(台形)')
        elif (self.lineAlength == self.lineBlength and self.lineClength == self.lineDlength)or(self.lineBlength == self.lineClength and self.lineDlength == self.lineAlength):
            return('kite(凧)')
        else:
            return('その他')

    def getPerimeter(self):
        if not self.quadrangle:
            return "四角形ではありません"

        return self.lineAlength + self.lineBlength + self.lineClength + self.lineDlength

    def getArea(self):
        if not self.quadrangle:
            return "四角形ではありません"

        lineaclength = ((self.ax-self.cx)**2+(self.ay-self.cy)**2)**0.5
        s1 = (self.lineAlength + self.lineBlength + lineaclength)/2
        halfarea1 = (s1*(s1-self.lineAlength)*(s1-self.lineBlength)*(s1-lineaclength))**0.5
        s2 = (self.lineClength + self.lineDlength + lineaclength)/2
        halfarea2 = (s2*(s2-self.lineClength)*(s2-self.lineDlength)*(s2-lineaclength))**0.5
        return round((halfarea1 + halfarea2), 1)

    def getAngle(self,angle):
        if not self.quadrangle:
            return "四角形ではありません"

        if(angle == 'BAD'):
            return self.angleA
        elif(angle == 'ABC'):
            return self.angleB
        elif(angle == 'ADC'):
            return self.angleD
        elif(angle == 'BCD'):
            return self.angleC
        else:
            return '未定義'

    def draw(self):
        if not self.quadrangle:
            return "四角形ではありません"
        #図形の大きさ
        xlist = [self.ax, self.bx, self.cx, self.dx]
        ylist = [self.ay, self.by, self.cy, self.dy]
        xMax = max(xlist); xMin = min(xlist)
        yMax = max(ylist); yMin = min(ylist)

        #第一象限にオフセット
        axOffset = self.ax - xMin; ayOffset = self.ay - yMin
        bxOffset = self.bx - xMin; byOffset = self.by - yMin
        cxOffset = self.cx - xMin; cyOffset = self.cy - yMin
        dxOffset = self.dx - xMin; dyOffset = self.dy - yMin
        xMax -= xMin; xMin -= xMin
        yMax -= yMin; yMin -= yMin

        #描写領域セット
        drawxy = [["　" for x in range(0,xMax+2)] for y in range(0,yMax+2)]

        #ループ計算開始点終了点計算関数
        #lineの向きによらず開始点と終了点を計算
        def pointcalc(p1,p2,direction):
            if direction == "x":
                Min = xMin
                Max = xMax
            else:
                Min = yMin
                Max = yMax

            if p1==p2:
                startP = Min
                endP = Max
            elif p1<p2:
                startP = p1
                endP = p2
            else:
                startP = p2
                endP = p1
            return startP, endP

        #描写ツール
        def drawtool(line,drawxy):
            if line == "lineA":
                px1, px2, px3 = axOffset, bxOffset, cxOffset
                py1, py2, py3 = ayOffset, byOffset, cyOffset
                xstart,xend = pointcalc(axOffset,bxOffset,"x")
                ystart,yend = pointcalc(ayOffset,byOffset,"y")
            elif line == "lineB":
                px1, px2, px3 = bxOffset, cxOffset, dxOffset
                py1, py2, py3 = byOffset, cyOffset, dyOffset
                xstart,xend = pointcalc(bxOffset,cxOffset,"x")
                ystart,yend = pointcalc(byOffset,cyOffset,"y")
            elif line == "lineC":
                px1, px2, px3 = cxOffset, dxOffset, axOffset
                py1, py2, py3 = cyOffset, dyOffset, ayOffset
                xstart,xend = pointcalc(cxOffset,dxOffset,"x")
                ystart,yend = pointcalc(cyOffset,dyOffset,"y")
            else:
                px1, px2, px3 = dxOffset, axOffset, bxOffset
                py1, py2, py3 = dyOffset, ayOffset, byOffset
                xstart,xend = pointcalc(dxOffset,axOffset,"x")
                ystart,yend = pointcalc(dyOffset,ayOffset,"y")

            #角度からsymbol決定
            #px1 >= px3で左側の辺か、右側の辺か判断
            #py1 >= py3で上側の辺か、下側の辺か判断
            #shiftRange,shiftPlot->プロットする点の調整
            #例：下記の1辺5の正方形
            #lineA = Line(Point(0,0), Point(5,0))
            #lineB = Line(Point(5,0), Point(5,5))
            #lineC = Line(Point(5,5), Point(0,5))
            #lineD = Line(Point(0,5), Point(0,0))
            #の時、描写する点は
            #lineA = Line(Point(1,0), Point(5,0))
            #lineB = Line(Point(5,1), Point(5,6))
            #lineC = Line(Point(5,5), Point(1,5))
            #lineD = Line(Point(0,6), Point(0,1))
            #になるため、shiftRange,shiftPlotで調整する
            if px2-px1 == 0:
                tilt = "infinity"
                xIntercept = px1
                yIntercept = 0
                symbol = '｜'
                if px1 >= px3:
                    xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 1, 1, 0
                else:
                    xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 1, 0, 0
            else:
                tilt = (py2 - py1)/(px2 - px1)
                xIntercept = 0
                yIntercept = py1 - tilt*px1
                if tilt == 1:
                    symbol = '／'
                    xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 1, 0, 0
                elif tilt == -1:
                    symbol = '＼'
                    xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 0, 0, 1
                #elif tilt>1:
                #    symbol = '/ '
                #    xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 1, 0, 0
                #elif tilt<-1:
                #    symbol = '\ '
                #    xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 0, 0, 1
                else:
                    if py1 >= py3:
                        symbol = '﹍'
                        xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 1, 0, 1
                    else:
                        symbol = '﹉'
                        xshiftRange, yshiftRange, xshiftPlot, yshiftPlot= 1, 0, 1, 0

            for y in range(yshiftRange + ystart, yshiftRange+yend):
                if tilt =="infinity":
                    drawxy[y][xIntercept+xshiftPlot] = symbol
                    continue
                for x in range(xshiftRange + xstart, xshiftRange+ xend):
                    if y == round(yIntercept + tilt*x):
                        drawxy[y+yshiftPlot][x] = symbol
            return drawxy

        #各線描写
        drawxy = drawtool("lineA",drawxy)
        drawxy = drawtool("lineB",drawxy)
        drawxy = drawtool("lineC",drawxy)
        drawxy = drawtool("lineD",drawxy)

        #現像
        for y in range(0,yMax+2):
            drawxy[y] = '　'.join(drawxy[y])
        drawxy.reverse()
        drawxy = '\n'.join(drawxy)
        return drawxy

#test1 正方形１
lineA = Line(Point(0,0), Point(5,0))
lineB = Line(Point(5,0), Point(5,5))
lineC = Line(Point(5,5), Point(0,5))
lineD = Line(Point(0,5), Point(0,0))
square1 = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(square1.getShapeType())
print(square1.draw())

#test2 正方形２
lineA = Line(Point(0,4), Point(4,8))
lineB = Line(Point(4,8), Point(8,4))
lineC = Line(Point(8,4), Point(4,0))
lineD = Line(Point(4,0), Point(0,4))
square2 = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(square2.getShapeType())
print(square2.draw())

#test2' 正方形２'
lineD = Line(Point(0+5,-4+5), Point(-4+5,-8+5))
lineC = Line(Point(-4+5,-8+5), Point(-8+5,-4+5))
lineB = Line(Point(-8+5,-4+5), Point(-4+5,0+5))
lineA = Line(Point(-4+5,0+5), Point(0+5,-4+5))
square3 = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(square3.getShapeType())
print(square3.draw())

#test3 長方形
lineA = Line(Point(0,0), Point(8,0))
lineB = Line(Point(8,0), Point(8,5))
lineC = Line(Point(8,5), Point(0,5))
lineD = Line(Point(0,5), Point(0,0))
rectangle = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(rectangle.getShapeType())
print(rectangle.draw())

#test4 ひし形
lineA = Line(Point(4,12), Point(0,6))
lineB = Line(Point(0,6), Point(4,0))
lineC = Line(Point(4,0), Point(8,6))
lineD = Line(Point(8,6), Point(4,12))
rhombus = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(rhombus.getShapeType())
print(rhombus.draw())

#test5 平行四辺形１
lineA = Line(Point(0,0), Point(2,2))
lineB = Line(Point(2,2), Point(2,6))
lineC = Line(Point(2,6), Point(0,4))
lineD = Line(Point(0,4), Point(0,0))
parallelogram1 = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(parallelogram1.getShapeType())
print(parallelogram1.draw())

#test6 平行四辺形２
lineA = Line(Point(0,0), Point(4,0))
lineB = Line(Point(4,0), Point(6,2))
lineC = Line(Point(6,2), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
parallelogram2 = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(parallelogram2.getShapeType())
print(parallelogram2.draw())

#test7 台形１
lineA = Line(Point(0,0), Point(6,0))
lineB = Line(Point(6,0), Point(4,2))
lineC = Line(Point(4,2), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
trapezoid1 = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(trapezoid1.getShapeType())
print(trapezoid1.draw())

#test8 台形２
lineA = Line(Point(0,0), Point(4,0))
lineB = Line(Point(4,0), Point(6,2))
lineC = Line(Point(6,2), Point(6,6))
lineD = Line(Point(6,6), Point(0,0))
trapezoid2 = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(trapezoid2.getShapeType())
print(trapezoid2.draw())

#test9 凧
lineC = Line(Point(0,4), Point(4,10))
lineD = Line(Point(4,10), Point(8,4))
lineA = Line(Point(8,4), Point(4,0))
lineB = Line(Point(4,0), Point(0,4))
kite = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(kite.getShapeType())
print(kite.draw())

#test9 凧
lineC = Line(Point(0,0), Point(3,0))
lineD = Line(Point(3,0), Point(6,3))
lineA = Line(Point(6,3), Point(4,0))
lineB = Line(Point(4,0), Point(0,4))
test = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(test.getShapeType())
print(test.draw())