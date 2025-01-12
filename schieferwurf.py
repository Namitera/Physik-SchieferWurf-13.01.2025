from manim import *

class Thumbnail(Scene):
    def construct(self):

        n = NumberPlane()
        ax = Axes(x_range=[0,16,1],x_length=13,y_range=[0,9,1],y_length=7)
        p1 = ax.plot(lambda x: -0.016*(x-8)**2+1).set_color(BLUE).set_opacity(1)
        p2 = ax.plot(lambda x: -0.031*(x-8)**2+2).set_color(BLUE).set_opacity(0.7)
        p3 = ax.plot(lambda x: -0.046*(x-8)**2+3).set_color(BLUE).set_opacity(0.5)
        p4 = ax.plot(lambda x: -0.062*(x-8)**2+4).set_color(BLUE).set_opacity(0.1)
        p5 = ax.plot(lambda x: -0.077*(x-8)**2+5).set_color(BLUE).set_opacity(0.1)
        p6 = ax.plot(lambda x: -0.092*(x-8)**2+6).set_color(BLUE).set_opacity(0.1)
        p7 = ax.plot(lambda x: -0.110*(x-8)**2+7).set_color(BLUE).set_opacity(0.1)
        p8 = ax.plot(lambda x: -0.124*(x-8)**2+8).set_color(BLUE).set_opacity(0.1)
        p9 = ax.plot(lambda x: -0.14*(x-8)**2+9).set_color(BLUE).set_opacity(0.1)
        p10 = ax.plot(lambda x: -0.15*(x-8)**2+9.6).set_color(BLUE).set_opacity(0.3)

        p21 = ax.plot(lambda x: -0.016*(x-8)**2+1).set_color(BLUE)
        p22 = ax.plot(lambda x: -0.031*(x-8)**2+2).set_color(BLUE)
        p23 = ax.plot(lambda x: -0.046*(x-8)**2+3).set_color(BLUE_D)
        p24 = ax.plot(lambda x: -0.062*(x-8)**2+4).set_color(BLUE_D)
        p25 = ax.plot(lambda x: -0.077*(x-8)**2+5).set_color(BLUE_C)
        p26 = ax.plot(lambda x: -0.092*(x-8)**2+6).set_color(BLUE_C)
        p27 = ax.plot(lambda x: -0.110*(x-8)**2+7).set_color(BLUE_D)
        p28 = ax.plot(lambda x: -0.124*(x-8)**2+8).set_color(BLUE_D)
        p29 = ax.plot(lambda x: -0.14*(x-8)**2+9).set_color(BLUE_D)
        p210 = ax.plot(lambda x: -0.15*(x-8)**2+9.6).set_color(BLUE_D)

        d1 = Dot(color=YELLOW,radius=0.1).move_to([-5.7,-3.35,0]).set_opacity(1)
        d2 = Dot(color=YELLOW,radius=0.1).move_to([-4.43,-2.65,0]).set_opacity(0.7)
        d3 = Dot(color=YELLOW,radius=0.1).move_to([-3.1,-1.7,0]).set_opacity(0.5)
        d4 = Dot(color=YELLOW,radius=0.1).move_to([-1.9,-0.65,0]).set_opacity(0.5)
        d5 = Dot(color=YELLOW,radius=0.1).move_to([-0.63,0.35,0]).set_opacity(0.7)
        d6 = Dot(color=YELLOW,radius=0.1).move_to([0.63,1.13,0]).set_opacity(0.7)
        d7 = Dot(color=YELLOW,radius=0.1).move_to([1.9,1.47,0]).set_opacity(0.5)
        d8 = Dot(color=YELLOW,radius=0.1).move_to([3.1,1.35,0]).set_opacity(0.5)
        d9 = Dot(color=YELLOW,radius=0.1).move_to([4.43,0.2,0]).set_opacity(0.7)
        d10 = Dot(color=YELLOW,radius=0.1).move_to([5.7,-1.8,0]).set_opacity(0.7)

        sw = Tex("Schiefer Wurf").to_edge(UP).scale(2.1).shift(DOWN*0.9)
        sw2 = Tex("Schiefer Wurf").to_edge(UP).scale(2.14).shift(DOWN*0.88).set_color(GRAY)

        a1 = Vector([1.3,0],color=YELLOW).move_to(d1).rotate(12*DEGREES).set_opacity(1)
        a2 = Vector([1.3,0],color=YELLOW).move_to(d2).rotate(17*DEGREES).set_opacity(0.7)
        a3 = Vector([1.3,0],color=YELLOW).move_to(d3).rotate(19*DEGREES).set_opacity(0.5)
        a4 = Vector([1.3,0],color=YELLOW).move_to(d4).rotate(16*DEGREES).set_opacity(0.5)
        a5 = Vector([1.3,0],color=YELLOW).move_to(d5).rotate(7*DEGREES).set_opacity(0.7)
        a6 = Vector([1.3,0],color=YELLOW).move_to(d6).rotate(-6*DEGREES).set_opacity(0.7)
        a7 = Vector([1.3,0],color=YELLOW).move_to(d7).rotate(-24*DEGREES).set_opacity(0.5)
        a8 = Vector([1.3,0],color=YELLOW).move_to(d8).rotate(-40*DEGREES).set_opacity(0.5)
        a9 = Vector([1.3,0],color=YELLOW).move_to(d9).rotate(-55*DEGREES).set_opacity(0.7)
        a10 = Vector([1.3,0],color=YELLOW).move_to(d10).rotate(-60*DEGREES).set_opacity(0.7)

        text = VGroup(sw2,sw)
        points = VGroup(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10)
        parabs = VGroup(p10,p2,p3,p4,p5,p6,p7,p8,p9,p1)
        parabs2 = VGroup(p210,p22,p23,p24,p25,p26,p27,p28,p29,p21)
        arrows = VGroup(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)

        self.add(parabs,parabs2,ax,text,points,arrows)





class QuoteOpening(Scene):
    def construct(self):
        n=NumberPlane()
        quote1 = Tex("„Alle Wahrheiten sind leicht zu ","verstehen",",").shift(2*UP)
        quote2 = Tex("sobald sie ","entdeckt"," sind;").shift(UP+LEFT*1.8)
        quote3 = Tex("der Punkt ist, sie zu ","entdecken",".“").shift(0*UP+1*LEFT)
        author = Tex("― Galileo").shift(2*DOWN)
        author.set_color(YELLOW)
        quote1[1].set_color(BLUE)
        quote2[1].set_color(BLUE)
        quote3[1].set_color(BLUE)
        
        self.wait()
        self.play(Write(quote1),run_time=3.5)
        self.play(Write(quote2),run_time=2.5)
        self.play(Write(quote3),run_time=3)
        self.wait(1)
        self.play(Write(author),run_time=2)
        self.wait(3)
        self.play(FadeOut(quote1,quote2,quote3,author))
        self.wait()





class RahmenBedingungen(Scene):
    def construct(self):

        n = NumberPlane()
        ax = Axes(x_range=[0,10,1],x_length=10,y_range=[0,7,1],y_length=7)
        v0 = ValueTracker(5)
        theta = ValueTracker(0)

        v0angle = Arc(start_angle=0)
        v0angle.add_updater(lambda mob: mob.become(Arc(color=WHITE,angle=theta.get_value(),radius=0.5*v0vector.get_length()).shift(5*LEFT+3.5*DOWN)))

        v0theta = MathTex(r"\theta").scale(2)
        v0theta.add_updater(
            lambda mob: mob.set_x(0.6*v0vector.get_length()*np.cos(0.5*theta.get_value())).set_y(0.6*v0vector.get_length()*np.sin(0.5*theta.get_value())).shift(5*LEFT+3.5*DOWN)
        )

        v0txt = MathTex(r"v_{0}").scale(2)
        v0txt.add_updater(
            lambda mob: mob.move_to(v0vector).shift(0.6*UP*np.sin(theta.get_value())*v0vector.get_length() +0.6*RIGHT*np.cos(theta.get_value())*v0vector.get_length())
        )

        examplethrow = ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2))
            ))
        examplethrow.add_updater(
            lambda mob: mob.become(ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2))
            ),color=WHITE))
        )

        v0vector = Vector([5,0],color=YELLOW).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        v0vector.add_updater(
            lambda mob: mob.set_angle((theta.get_value())).set_length(v0.get_value()).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        )
        obj = VGroup(ax,examplethrow,v0vector,v0angle,v0theta,v0txt)
        self.play(Create(obj))
        self.play(theta.animate.set_value(80*DEGREES),run_time=5)
        self.play(v0.animate.set_value(3),run_time=5)
        self.play(theta.animate.set_value(30*DEGREES),run_time=5)
        self.play(v0.animate.set_value(5),run_time=5)
        self.play(theta.animate.set_value(45*DEGREES),run_time=3)
        self.play(v0.animate.set_value(4),run_time=5)





class Teilgeschwindigkeiten(Scene):
    def construct(self):
        n = NumberPlane()
        theta = ValueTracker(15)
        v0vector = Vector([5,0],color=YELLOW).rotate(theta.get_value()*DEGREES).shift(1.5*UP+2.5*LEFT)
        v0txt = MathTex(r"v_{0}").scale(2)
        v0txt.add_updater(lambda mob: mob.next_to(v0vector,UP))
        vxvector = Vector(color=RED).shift(2*DOWN+3*LEFT)
        vyvector = Vector(color=GREEN).shift(2*DOWN+2*RIGHT)
        vxtxt = MathTex(r"v_{x}",color=RED).scale(2)
        vxtxt.next_to(vxvector,UP)
        vytxt = MathTex(r"v_{y}",color=GREEN).scale(2)
        vytxt.next_to(vyvector,UP)

        self.wait()
        self.add(v0vector,v0txt)
        self.play(Create(v0vector),Create(v0txt),run_time=2)
        self.wait(10)
        self.play(Create(vxvector),Create(vxtxt),run_time=2)
        self.wait()
        self.play(Create(vyvector),Create(vytxt),run_time=2)

        vxtxt.suspend_updating()
        self.play(vxvector.animate.shift(RIGHT*0.6 + UP*2.85),vxtxt.animate.shift(RIGHT*0.6 + UP*1.5),run_time=2)
        self.play(vxvector.animate.set_length(np.cos(theta.get_value()*DEGREES)*v0vector.get_length()).align_to(v0vector,LEFT),
                  vxtxt.animate.next_to(vxvector,DOWN),run_time=2)
        self.wait(2)  
        self.play(vyvector.animate.set_length(np.sin(theta.get_value()*DEGREES)*v0vector.get_length()).align_to(vxvector,UR).rotate(PI/2).shift(0.6*UR*vyvector.get_length()),vytxt.animate.shift(RIGHT*0.7 +2.5*UP),run_time=2) 
        self.wait()

        p1Vectors = VGroup(v0vector,vxvector,vyvector,vxtxt,vytxt)
        self.play(p1Vectors.animate.shift(DOWN*2),run_time=2)
        self.wait(4)

        v0vector.add_updater(lambda mob: mob.set_angle(theta.get_value()*DEGREES))
        v0txt.add_updater(lambda mob: mob.next_to(v0vector,UP*0.2))
        vxvector.add_updater(lambda mob: mob.set_length(np.cos(theta.get_value()*DEGREES)*v0vector.get_length()).align_to(v0vector,LEFT))
        vyvector.add_updater(lambda mob: mob.set_length(np.sin(theta.get_value()*DEGREES)*v0vector.get_length()).align_to(vxvector,UR).shift(0.97*UP*vyvector.get_length()))
        vytxt.add_updater(lambda mob: mob.next_to(vyvector,RIGHT))

        self.play(theta.animate.set_value(60),run_time=2)
        self.play(theta.animate.set_value(60),run_time=1)
        self.play(theta.animate.set_value(30),run_time=2)
        self.play(theta.animate.set_value(30),run_time=1)
        self.play(theta.animate.set_value(1),run_time=2)
        self.play(theta.animate.set_value(1),run_time=1)
        self.play(theta.animate.set_value(60),run_time=6)
        self.play(theta.animate.set_value(60),run_time=1)
        self.play(theta.animate.set_value(45),run_time=4)
        self.play(theta.animate.set_value(45),run_time=1)





class sinuscosinusIntuition(Scene):
    def construct(self):

        n = NumberPlane().scale(3)
        n.set_opacity(0.7)
        ax = Axes(x_range=[-3,3,3],x_length=6,y_range=[-3,3,3],y_length=6,tips=False)
        ax.set_opacity(0.7)
        circ = Circle(radius=3,color=WHITE)
        b = ValueTracker(0)
    

        point = Dot(color=YELLOW)
        point.add_updater(lambda mob: mob.set_x(3*np.cos(b.get_value())))
        point.add_updater(lambda mob: mob.set_y(3*np.sin(b.get_value())))

        hyp = Line(start=[0,0,0],end=[3,0,0],color=YELLOW)
        hyp.add_updater(lambda mob: mob.set_angle(b.get_value()))

        adj = Line(start=[0,0,0],end=[3,0,0],color=RED)
        adj.add_updater(lambda mob: mob.set_x(1.5*np.cos(b.get_value())))
        adj.add_updater(lambda mob: mob.set_length(3*np.cos(b.get_value())))

        opp = Line(start=[0,0,0],end=[0,3,0],color=GREEN)
        opp.add_updater(lambda mob: mob.set_y(1.5*np.sin(b.get_value())))
        opp.add_updater(lambda mob: mob.set_length(3*np.sin(0.001+b.get_value())))
        opp.add_updater(lambda mob: mob.set_x(3*np.cos(b.get_value())))

        sin = MathTex(r"sin({\theta})",color=GREEN).scale(1)
        cos = MathTex( r"cos({\theta})",color=RED).scale(1)
        sin.add_updater(lambda mob: mob.next_to(opp,RIGHT,buff=0.1))
        cos.add_updater(lambda mob: mob.next_to(adj,DOWN,buff=0.1))

        theta = MathTex(r"\theta").scale(1)
        theta.add_updater(lambda mob: mob.set_x(0.5*np.cos(0.5*b.get_value())))
        theta.add_updater(lambda mob: mob.set_y(0.5*np.sin(0.5*b.get_value())))

        thetaarc = Arc(start_angle=1)
        thetaarc.add_updater(lambda mob: mob.become(Arc(angle=b.get_value(),radius=1)))

        self.add(n,circ,hyp,adj,opp,sin,cos,theta,thetaarc,point)
        self.play(b.animate.set_value(1*DEGREES),run_time=1)
        self.play(b.animate.set_value(45*DEGREES),run_time=4)
        self.play(b.animate.set_value(90*DEGREES),run_time=4)
        self.play(b.animate.set_value(45*DEGREES),run_time=4)
        self.wait(2)
        self.play(b.animate.set_value(PI/2),run_time=5)
        self.play(Indicate(sin))
        self.play(b.animate.set_value(0),run_time=5)
        self.wait(3)
        self.play(Indicate(cos))
        self.play(b.animate.set_value(PI/2),run_time=5)
        self.wait(2)
        self.play(b.animate.set_value(PI/4),run_time=3)
        self.wait(4)

        one = MathTex(r"1",color=YELLOW).move_to(hyp).shift(0.4*UP + 0.4*LEFT)
        self.add(one)
        self.play(Write(one))
        self.wait(2)

        one2 = MathTex(r"v_{0}",color=YELLOW).move_to(one)
        
        cos2 = MathTex(r"1\cdot ", r"cos(\theta)").move_to(cos)
        cos2[0].set_color(YELLOW)
        cos2[1].set_color(RED)
        cos2b = MathTex(r"v_{0}\cdot ", r"cos(\theta)").move_to(cos)
        cos2b[0].set_color(YELLOW)
        cos2b[1].set_color(RED)

        sin2 = MathTex(r"1\cdot ", r"sin(\theta)").move_to(sin)
        sin2[0].set_color(YELLOW)
        sin2[1].set_color(GREEN)
        sin2b = MathTex(r"v_{0}\cdot ", r"sin(\theta)",color=GREEN).move_to(sin).next_to(opp,RIGHT)
        sin2b[0].set_color(YELLOW)
        sin2b[1].set_color(GREEN)

        hyptip = Triangle(color=YELLOW,fill_opacity=1).move_to([2,2.32,0]).rotate(72*DEGREES).scale(0.2)
        adjtip = Triangle(color=RED,fill_opacity=1).move_to([1.8,0.2,0]).rotate(30*DEGREES).scale(0.1)
        opptip = Triangle(color=GREEN,fill_opacity=1).move_to([2.12,1.8,0]).rotate(0*DEGREES).scale(0.15)
        

        self.play(TransformMatchingShapes(cos,cos2))
        self.wait(3)
        self.play(TransformMatchingShapes(sin,sin2))
        self.wait()
        self.play(sin2.animate.next_to(opp,RIGHT))
        self.wait(2)
        self.play(TransformMatchingShapes(one,one2),TransformMatchingShapes(point,hyptip))
        self.wait(2)
        self.play(TransformMatchingShapes(cos2,cos2b),FadeIn(adjtip))
        self.wait(2)
        self.play(TransformMatchingShapes(sin2,sin2b),FadeIn(opptip))
        self.wait(2)
        self.play(sin2b.animate.next_to(opp,RIGHT))
        self.wait()
        self.play(FadeOut(ax,n,circ))
        self.wait(9)

        vxformula = MathTex(r"v_{0}\cdot ", r"cos(\theta)").move_to(cos2b)
        vxformula[0].set_color(WHITE)
        vxformula[1].set_color(RED)
        vyformula = MathTex(r"v_{0}\cdot ", r"sin(\theta)",color=GREEN).move_to(sin2b)
        vyformula[0].set_color(WHITE)
        vyformula[1].set_color(GREEN)
        vxformula2 = MathTex(r"v_{x}",r"=v_{0}\cdot cos(\theta)").shift(DOWN+3*LEFT)
        vyformula2 = MathTex(r"v_{y}",r"=v_{0}\cdot sin(\theta)").shift(UP+3*LEFT)
        vxformula2[0].set_color(RED)
        vyformula2[0].set_color(GREEN)


        self.add(vxformula,vyformula)
        self.play(ReplacementTransform(vxformula,vxformula2),run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(vyformula,vyformula2),run_time=2)
        self.wait(7)





class BahnkurveDreieck(Scene):
    def construct(self):

        n = NumberPlane()
        ax = Axes(x_range=[0,10,1],x_length=10,y_range=[0,7,1],y_length=7)
        v0 = ValueTracker(5)
        time = ValueTracker(0.1)
        theta = ValueTracker(1.1)
        point = Dot(radius=0.1,color=YELLOW)
        vxvector = Vector(color=RED)
        vyvector = Vector(color=GREEN)
        v0vector = Vector([3,0],color=YELLOW)

        examplethrow = ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(v0.get_value()**2 * np.cos(theta.get_value())**2))
            ))
        examplethrow.add_updater(
            lambda mob: mob.become(ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(v0.get_value()**2 * np.cos(theta.get_value())**2))
            ),color=WHITE))
        )

        point.add_updater(lambda mob: mob.set_x(time.get_value()))
        point.add_updater(
            lambda mob: mob.set_y(np.tan(theta.get_value())*point.get_x() - ((point.get_x()**2)/(v0.get_value()**2 * np.cos(theta.get_value())**2)))
            )
        point.add_updater(lambda mob: mob.shift(LEFT*5,DOWN*3.5))
        
        v0vector.add_updater(
            lambda mob: mob.set_angle(np.arctan(
                np.tan(theta.get_value()) - ((4.4*time.get_value())/(v0.get_value()**2 * np.cos(theta.get_value())))
                ) #?????????????????????????????????
            ).move_to(point).shift(UP*np.sin(v0vector.get_angle())*0.5*v0vector.get_length() +RIGHT*np.cos(v0vector.get_angle())*0.5*v0vector.get_length()).set_length(vxvector.get_length()/np.cos(v0vector.get_angle())))

        vxvector.add_updater(lambda mob: mob.set_length(3).next_to(point,RIGHT,buff=-0.1))
        vyvector.rotate(PI/2)
        vyvector.add_updater(lambda mob: mob.set_length(np.sin(np.abs(v0vector.get_angle())+0.01)*v0vector.get_length()).move_to(vxvector).shift(UP*0.5*vyvector.get_length()*np.sin(vyvector.get_angle()) +RIGHT*0.5*vxvector.get_length()))


        vxbrace = Brace(vxvector,direction=DOWN).scale(2)
        vxtex = MathTex(r"v_{x}", r"=konstant")
        vxtex[0].set_color(RED)
        vxbrace.add_updater(lambda mob: mob.next_to(vxvector,DOWN,buff=0.1))
        vxtex.add_updater(lambda mob: mob.next_to(vxbrace,DOWN,buff=0.5))

        vybrace = Brace(vyvector,direction=RIGHT).scale(vyvector.get_length())
        vytex = MathTex(r"v_{y}", r"=")
        vytex[0].set_color(GREEN)
        vydecimal = DecimalNumber(1,num_decimal_places=2)
        vydecimal.add_updater(lambda mob: mob.set_value(vyvector.get_length()).next_to(vytex,RIGHT,buff=0.3).shift(UP*0.1))
        vybrace.add_updater(lambda mob: mob.next_to(vxvector,RIGHT,buff=0.1).shift(UP*0.5*vyvector.get_length()).set_length(vyvector.get_length()))
        vytex.add_updater(lambda mob: mob.next_to(vybrace,RIGHT,buff=0.5))
        
        self.wait()
        self.play(Create(ax),Create(examplethrow),run_time=2)
        point.set_opacity(0)
        v0vector.set_opacity(0)
        vxvector.set_opacity(0)
        vyvector.set_opacity(0)
        self.add(point,v0vector,vxvector,vyvector)
        self.play(point.animate.set_opacity(1),v0vector.animate.set_opacity(1),vxvector.animate.set_opacity(1),vyvector.animate.set_opacity(1),run_time=2)
        self.play(time.animate.set_value(3),run_time=10)
        self.play(time.animate.set_value(3.01)) #-pql lässt vy seltsam springen nach rechts fürn frame kp
        self.play(Write(vxbrace),Write(vxtex),time.animate.set_value(3),run_time=3)
        self.play(time.animate.set_value(3))
        self.play(time.animate.set_value(5),run_time=4)
        vyvector.rotate(PI)
        self.play(time.animate.set_value(8),run_time=9)
        self.play(FadeOut(vxbrace),FadeOut(vxtex),FadeOut(point),FadeOut(v0vector),FadeOut(vxvector),FadeOut(vyvector),time.animate.set_value(8),run_time=0.5)        
        self.play(time.animate.set_value(1),vyvector.animate.rotate(-PI),rate_func=linear,run_time=0.01)
        self.play(Create(point),Create(v0vector),time.animate.set_value(1),run_time=0.001)
        self.play(Create(vxvector),Create(vyvector),time.animate.set_value(1),run_time=2)
        self.play(time.animate.set_value(1))
        self.play(Write(vybrace),Write(vytex),Write(vydecimal),time.animate.set_value(1),run_time=2)
        self.play(time.animate.set_value(5),run_time=9 )
        self.play(time.animate.set_value(0.5),run_time=6)
        self.play(time.animate.set_value(0.5),run_time=2)





class VxyFormula(Scene):
    def construct(self):

        vst = MathTex(r"v=\frac{\Delta s}{\Delta t}")
        vst2 = MathTex(r"v=",r"\frac{\Delta s}{\Delta t}")
        vst3 = MathTex(r"v",r"\cdot t=s")
        vst4 = MathTex(r"s=",r"v",r"\cdot t")
        vst4a = MathTex(r"x=",r"v",r"\cdot t")
        vst5 = MathTex(r"x(t)=",r"v_{x}",r"\cdot t")
        ggb = Tex("gleichförmig geradlinige Bewegung").next_to(vst,UP)
        ggbf = VGroup(vst,ggb)
        vst[0][0:1].set_color(YELLOW)
        vst2[0][0:1].set_color(YELLOW)
        vst3[0].set_color(YELLOW)
        vst4[1].set_color(YELLOW)
        vst4a[1].set_color(YELLOW)
        vst5[1].set_color(RED)
        vxformula = MathTex(r"v_{x}",r"=v_{0}\cdot cos(\theta)")
        vxformula[0].set_color(RED)
        vst6 = MathTex(r"x(t)=",r"v_{0}\cdot cos(\theta)",r"\cdot t")
        vst6[1].set_opacity(0)
        vst6[1].set_color(RED)
        vxformula2 = MathTex(r"v_{x}",r"=v_{0}\cdot cos(\theta)")
        vxformula2[0].set_color(RED)


        self.play(Write(ggb),run_time=2)
        self.play(Write(vst))
        self.play(ggbf.animate.to_corner(UL))
        self.wait(2)
        vst2.move_to(vst)
        self.add(vst2)
        self.play(vst2.animate.move_to([0,0,0]),run_time=2)
        self.wait()
        self.play(Circumscribe(vst2[1]))
        self.wait()
        self.play(TransformMatchingShapes(vst2,vst3))
        self.wait()
        self.play(TransformMatchingShapes(vst3,vst4))
        self.wait(2)
        self.play(Circumscribe(vst4[0]))
        self.wait()
        self.play(TransformMatchingShapes(vst4,vst4a))
        self.wait(2)
        self.play(Circumscribe(vst4a[0]))
        self.play(Circumscribe(vst4a[1]))
        self.wait()
        self.play(TransformMatchingShapes(vst4a,vst5))
        self.wait(4)
        self.play(Indicate(vst5[0]))
        self.play(Indicate(vst5[1]))
        self.wait()
        vxformula.next_to(vst5,DOWN*4)
        self.play(Write(vxformula))
        self.wait(4)
        self.play(Circumscribe(vst5[1]))
        self.play(Indicate(vst5[1]))
        self.wait()
        self.play(Circumscribe(vxformula[0]))
        self.play(Indicate(vxformula[0]))
        self.wait()
        self.play(TransformMatchingShapes(vst5,vst6))
        self.wait()
        vxformula2.move_to(vxformula)
        self.play(TransformMatchingShapes(vxformula2[1],vst6[1]),vst6[1].animate.set_opacity(1),run_time=3)
        self.wait(3)
        self.play(Unwrite(vxformula),run_time=0.01)
        self.play(vst6.animate.to_corner(UR),vxformula2.animate.to_corner(UR).shift(DOWN),run_time=3)

        gbb = Tex("gleichmäßig beschleunigte Bewegung")
        sat = MathTex(r"s(t)=\frac{1}{2}at^{2}").next_to(gbb,DOWN)
        sat2 = MathTex(r"s(t)=\frac{1}{2}",r"a",r"t^{2}")
        sat3 = MathTex(r"s(t)=\frac{1}{2}",r"g",r"t^{2}")
        sat4 = MathTex(r"s(t)",r"=-\frac{1}{2}gt^{2}")
        sat5 = MathTex(r"y(t)",r"=-\frac{1}{2}gt^{2}")
        sat6 = MathTex(r"y(t)=-\frac{1}{2}gt^{2}+",r"v_{y}",r"t")
        sat6[1].set_color(GREEN)
        sat7 = MathTex(r"y(t)=",r"v_{y}",r"t-\frac{1}{2}gt^{2}")
        sat7[1].set_color(GREEN)
        ag = MathTex(r"a:=",r"g",r"=9.81\frac{m}{s^{2}}")
        ag2 = MathTex(r"a:=",r"g",r"=9.81\frac{m}{s^{2}}")
        vyformula = MathTex(r"v_{y}",r"=v_{0}\cdot sin(\theta)").shift(2*DOWN)
        vyformula[0].set_color(GREEN)
        vyformula2 = MathTex(r"v_{y}",r"=v_{0}\cdot sin(\theta)").shift(2*DOWN)
        vyformula2[0].set_color(GREEN)
        sat8 = MathTex(r"y(t)=",r"v_{0}\cdot sin(\theta)",r"t-\frac{1}{2}gt^{2}")
        sat8[1].set_opacity(0)
        sat8[1].set_color(GREEN)

        self.wait(3)
        self.play(Write(gbb),run_time=2)
        self.play(Write(sat))
        self.wait()
        self.play(Unwrite(ggb),run_time=0.5)
        self.play(gbb.animate.to_corner(UL),sat.animate.to_corner(UL).shift(DOWN),Unwrite(vst),run_time=2)
        self.wait()
        ag.next_to(sat,DOWN).shift(RIGHT*0.5)
        self.play(Write(ag),run_time=2)
        self.wait()
        sat2.move_to(sat)
        self.add(sat2)
        self.play(sat2.animate.move_to([0,0,0]))
        self.wait()
        self.add(ag2.move_to(ag))
        sat3[1].set_opacity(0)
        self.play(Circumscribe(sat2[1]))
        self.play(Indicate(sat2[1]))
        self.wait()
        self.play(Circumscribe(ag[1]))
        self.play(Indicate(ag[1]),Indicate(ag2[1]))
        self.wait()
        self.play(TransformMatchingShapes(sat2,sat3))
        self.play(TransformMatchingShapes(ag2[1],sat3[1]),sat3[1].animate.set_opacity(1),run_time=1)
        self.wait()
        self.play(Circumscribe(sat3[1]),run_time=1)
        self.wait()
        self.play(TransformMatchingShapes(sat3,sat4))
        self.wait(2)
        self.play(Circumscribe(sat4[0]))
        self.play(Indicate(sat4[0]))
        self.wait()
        self.play(TransformMatchingShapes(sat4,sat5))
        self.wait(3)
        self.play(Circumscribe(sat5[0]))
        self.wait(3)
        self.play(TransformMatchingShapes(sat5,sat6))
        self.wait(5)
        self.play(Circumscribe(sat6[1]))
        self.wait()
        self.play(TransformMatchingShapes(sat6,sat7))
        self.wait(2)
        self.play(Write(vyformula),run_time=2)
        self.wait(4)
        self.play(Circumscribe(sat7[1]))
        self.play(Indicate(sat7[1]))
        self.wait()
        self.play(Circumscribe(vyformula[0]))
        self.play(Indicate(vyformula[0]))
        self.wait()
        self.play(TransformMatchingShapes(sat7,sat8))
        self.add(vyformula2.move_to(vyformula))
        self.wait()
        self.play(TransformMatchingShapes(vyformula2[1],sat8[1]),sat8[1].animate.set_opacity(1),run_time=3)
        self.wait()
        self.play(Unwrite(vyformula),run_time=0.01)
        self.play(vyformula2.animate.to_corner(UR).shift(DOWN*3),sat8.animate.to_corner(UR).shift(DOWN*1.7),run_time=2)
        self.wait(3)





class BahnkurveIntuition(Scene):
    def construct(self):

        bk = Tex("Bahnkurve").to_corner(UL)
        bkp2 =Tex ("- y in Abhängigkeit von x").to_corner(UL).shift(DOWN*1.1)
        bkp1 = Tex("- bringt x(t) und y(t) zusammen").to_corner(UL).shift(DOWN*0.5)
        xtboundary = Rectangle(color=BLACK,fill_opacity=1,width=5,height=4).shift(LEFT*4.5 + UP*2.5)
        self.play(Write(bk))
        self.wait(2)
        self.play(Write(bkp1))
        self.wait(4)
        self.play(Write(bkp2))
        self.wait(4)

        n = NumberPlane()
        ax1 = Axes(x_range=[0,5,1],x_length=4,y_range=(0,5,1),y_length=4).shift(LEFT*4.5 +DOWN*1.5)
        ax2 = Axes(x_range=[0,5,1],x_length=4,y_range=(0,5,1),y_length=4).shift(LEFT*0 +DOWN*1.5)
        ax3 = Axes(x_range=[0,5,1],x_length=4,y_range=(0,5,1),y_length=4).shift(RIGHT*4.5 +DOWN*1.5)
        axlabel1a = MathTex(r"x").align_to(ax1,UL).shift(UP*0.5)
        axlabel1b = MathTex(r"t").align_to(ax1,DR).shift(UP*0.5)
        axlabel2a = MathTex(r"y").align_to(ax2,UL).shift(UP*0.5)
        axlabel2b = MathTex(r"t").align_to(ax2,DR).shift(UP*0.5)
        axlabel3a = MathTex(r"y").align_to(ax3,UL).shift(RIGHT*0.5+DOWN*0.3)
        axlabel3b = MathTex(r"x").align_to(ax3,DR).shift(UP*0.5)

        v0 = ValueTracker(9)
        theta = ValueTracker(0)

        plotxt = ax1.plot(lambda x: v0.get_value()*np.cos(theta.get_value())*x)
        plotxt.add_updater(lambda mob:
                           mob.become(ax1.plot(lambda x: v0.get_value()*np.cos(theta.get_value())*x).set_color(YELLOW)))

        plotyt = ax2.plot(lambda x: v0.get_value()*np.sin(theta.get_value())*x- 0.5*9.81*x*x)
        plotyt.add_updater(lambda mob:
                           mob.become(ax2.plot(lambda x: v0.get_value()*np.sin(theta.get_value())*x - 0.5*9.81* x**2).set_color(YELLOW)))

        plotyx = ax3.plot(lambda x: np.tan(theta.get_value())*x - ((9.81* x**2)/(2*v0.get_value()**2 * np.cos(theta.get_value())**2)))
        plotyx.add_updater(lambda mob:
                           mob.become(ax3.plot(lambda x: np.tan(theta.get_value())*x - ((9.81* x**2)/(2*v0.get_value()**2 * np.cos(theta.get_value())**2))).set_color(YELLOW)))
        
        numberv0 = DecimalNumber(0.00,num_decimal_places=2).to_corner(UR)
        numberv0.add_updater(lambda mob: mob.set_value(v0.get_value()))
        numbertheta = DecimalNumber(0.00,num_decimal_places=2).to_corner(UR).shift(DOWN)
        numbertheta.add_updater(lambda mob: mob.set_value((360*theta.get_value())/(2*PI)))
        v0tex = MathTex(r"v_{0}=").next_to(numberv0,LEFT).set_color(YELLOW)
        thetatex = MathTex(r"\theta=").next_to(numbertheta,LEFT).set_color(YELLOW)

        plotxt.set_z_index(-2)
        self.add(xtboundary.set_z_index(-1))

        xtformula = MathTex(r"x",r"(t)=",r"v_{0}cos(\theta)",r"t").next_to(axlabel1a,RIGHT).shift(RIGHT*0.2)
        xtformula[0].set_color(RED)
        xtformula[2].set_color(RED)

        ytformula = MathTex(r"y",r"(t)=",r"v_{0}sin(\theta)",r"t-\frac{1}{2}gx^{2}").next_to(axlabel2a,RIGHT).shift(RIGHT*0.2+UP*0.1)
        ytformula[0].set_color(GREEN)
        ytformula[2].set_color(GREEN)

        yxformula = MathTex(r"y",r"(x)").next_to(axlabel3a,RIGHT).shift(RIGHT*-0.5+DOWN*1)

        self.play(Create(ax1))
        self.add(plotxt)
        self.play(Write(axlabel1a),Write(axlabel1b),Write(xtformula))
        self.wait()
        self.play(Write(numbertheta),Write(numberv0),Create(v0tex),Create(thetatex))
        self.wait()
        self.play(theta.animate.set_value(1.57),run_time=5)
        self.play(theta.animate.set_value(0.3),run_time=5)
        self.play(theta.animate.set_value(1),run_time=2)
        self.wait()
        self.play(v0.animate.set_value(4),run_time=4)
        self.play(v0.animate.set_value(10),run_time=4)
        self.play(v0.animate.set_value(9),run_time=2)
        self.wait()

        self.play(Create(ax2))
        self.add(plotyt)
        self.play(Write(axlabel2a),Write(axlabel2b),Write(ytformula))
        self.wait()
        self.play(theta.animate.set_value(1.57),run_time=5)
        self.play(theta.animate.set_value(0.3),run_time=5)
        self.play(theta.animate.set_value(1),run_time=2)
        self.wait()
        self.play(v0.animate.set_value(4),run_time=4)
        self.play(v0.animate.set_value(10),run_time=4)
        self.play(v0.animate.set_value(9),run_time=2)
        self.wait()

        self.play(Create(ax3))
        self.add(plotyx)
        self.play(Write(axlabel3a),Write(axlabel3b),Write(yxformula))
        self.wait()
        self.play(theta.animate.set_value(1.57),run_time=5)
        self.play(theta.animate.set_value(0.3),run_time=5)
        self.play(theta.animate.set_value(1),run_time=2)
        self.wait()
        self.play(v0.animate.set_value(4),run_time=4)
        self.play(v0.animate.set_value(10),run_time=4)
        self.play(v0.animate.set_value(9),run_time=2)
        self.wait()





class BahnkurveFormula(Scene):
    def construct(self):

        hb = Tex("horizontale Bewegung:").to_corner(UL)
        vb = Tex("vertikale Bewegung:").to_corner(UL).shift(RIGHT*6)
        xttex = MathTex(r"x",r"(t)=",r"v_{0}cos(\theta)",r"\cdot t").to_corner(UL).shift(DOWN*0.8)
        yttex = MathTex(r"y",r"(t)=",r"v_{0}sin(\theta )", r"t", r"-\frac{1}{2}g", r"t^{2}").to_corner(UL).shift(DOWN*0.5 + RIGHT*6)
        xttex[0].set_color(RED)
        xttex[2].set_color(RED)
        yttex[0].set_color(GREEN)
        yttex[2].set_color(GREEN)


        self.play(Write(hb))
        self.play(Write(xttex))
        self.wait()
        self.play(Write(vb))
        self.play(Write(yttex))
        self.wait()

        xt1=MathTex(r"x(t)=",r"v_{0}cos(\theta)",r"\cdot t")
        xt2=MathTex(r"x=",r"v_{0}cos(\theta)",r"\cdot t")
        xt=MathTex(r"\frac{x}{v_{0}cos(\theta )}",r"=",r" t")
        xtcopy=MathTex(r"\frac{x}{v_{0}cos(\theta )}",r"=",r"t")
        yt=MathTex(r"y(t)=v_{0}sin(\theta )", r"t", r"-\frac{1}{2}g", r"t^{2}").shift(DOWN*2)

        self.play(Write(yt))
        self.play(Write(xt1))
        self.wait(3)
        self.play(Indicate(xt1[0]),run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(xt1,xt2))
        self.wait()
        self.play(Circumscribe(xt2[1]))
        self.play(Indicate(xt2[1]))
        self.wait()
        self.play(TransformMatchingShapes(xt2,xt),run_time=2)
        self.add(xtcopy)
        self.wait()

        insert1 = MathTex(r"y(x)=",r"v_{0}sin(\theta )", r"\frac{x}{v_{0}cos(\theta )}", r"-\frac{1}{2}g", r"t^{2}").shift(DOWN*2)
        insert1a = MathTex(r"y(x)=", r"\frac{v_{0}sin(\theta )\cdot x}{v_{0}cos(\theta )}", r"-\frac{1}{2}g", r"t^{2}").shift(DOWN*2)
        insert1aa = MathTex(r"y(x)=", r"\frac{v_{0}\cdot sin(\theta )\cdot x}{v_{0}\cdot cos(\theta )}", r"-\frac{1}{2}g", r"t^{2}").shift(DOWN*2)
        insert1b = MathTex(r"y(x)=", r"\frac{sin(\theta )}{cos(\theta )}", r"\cdot x-\frac{1}{2}g", r"t^{2}").shift(DOWN*2)
        insert1c = MathTex(r"y(x)=", r"tan(\theta )", r"\cdot x-\frac{1}{2}g", r"t^{2}").shift(DOWN*2)

        insert2 = MathTex(r"y(x)=", r"tan(\theta )", r"\cdot x-\frac{1}{2}g", r"(\frac{x}{v_{0}cos(\theta )})^{2}").shift(DOWN*2)
        insert2a = MathTex(r"y(x)=", r"tan(\theta )", r"\cdot x-\frac{1}{2}g", r"\frac{x^{2}}{(v_{0}cos(\theta ))^{2}}").shift(DOWN*2)
        insert2b = MathTex(r"y(x)=", r"tan(\theta )", r"\cdot x-\frac{1}{2}g", r"\frac{x^{2}}{v_{0}^{2}cos^{2}(\theta )}").shift(DOWN*2)
        insert2c = MathTex(r"y(x)=", r"tan(\theta )\cdot x", r"-\frac{gx^{2}}{2v_{0}^{2}cos^{2}(\theta )}").shift(DOWN*2)

        xt.save_state()
        self.play(Circumscribe(yt[1]))
        self.play(Indicate(yt[1]),run_time=2)
        self.play(Circumscribe(xt[2]),Circumscribe(xtcopy[2]))
        self.play(Indicate(xt[2]),Indicate(xtcopy[2]),run_time=2)
        insert1[2].set_opacity(0)
        self.wait()
        self.play(TransformMatchingShapes(yt,insert1))
        self.wait()
        self.play(Circumscribe(xt[0]),run_time=1)
        self.play(AnimationGroup(
            TransformMatchingShapes(xt[0],insert1[2]),insert1[2].animate.set_opacity(1),lag_ratio=0.3
            ),run_time=3)
        self.wait()
        self.play(Indicate(insert1[1]))
        self.play(Indicate(insert1[2]))
        self.wait()
        self.play(TransformMatchingShapes(insert1,insert1a),run_time=2)
        self.wait()
        self.play(Circumscribe(insert1a[1]),run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(insert1a,insert1aa))
        self.wait()
        self.play(TransformMatchingShapes(insert1aa,insert1b))
        self.wait()
        self.play(Indicate(insert1b[1]),run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(insert1b,insert1c))
        self.wait()

        self.play(Restore(xt))
        self.play(Circumscribe(insert1c[3]))
        self.play(Indicate(insert1c[3]))
        self.wait()
        insert2[3].set_opacity(0)
        self.play(Circumscribe(xt[2]))
        self.play(Indicate(xt[2]),Indicate(xtcopy[2]))
        self.wait()
        self.play(TransformMatchingShapes(insert1c,insert2))
        self.play(AnimationGroup(
            TransformMatchingShapes(xt[0],insert2[3]),insert2[3].animate.set_opacity(1),lag_ratio=0.2
            ),run_time=3)
        xt.set_opacity(0)
        self.wait()
        self.play(Circumscribe(insert2[3]))
        self.wait()
        self.play(TransformMatchingShapes(insert2,insert2a))
        self.wait()
        self.play(Circumscribe(insert2a[3]))
        self.wait()
        self.play(TransformMatchingShapes(insert2a,insert2b))
        self.wait()
        self.play(Indicate(insert2b[2]))
        self.wait()
        self.play(Indicate(insert2b[3]))
        self.wait()
        self.play(TransformMatchingShapes(insert2b,insert2c))
        self.wait()
        self.play(Unwrite(xt),Unwrite(xtcopy),insert2c.animate.move_to([0,0,0]))
        self.wait(10)





class BahnkurveGraph(Scene):
    def construct(self):

        n = NumberPlane()
        ax = Axes(x_range=[0,10,1],x_length=10,y_range=[0,7,1],y_length=7)
        v0 = ValueTracker(5)
        theta = ValueTracker(0)

        v0angle = Arc(start_angle=0)
        v0angle.add_updater(lambda mob: mob.become(Arc(color=WHITE,angle=theta.get_value(),radius=0.5*v0vector.get_length()).shift(5*LEFT+3.5*DOWN)))

        v0theta = MathTex(r"\theta").scale(2)
        v0theta.add_updater(
            lambda mob: mob.set_x(0.6*v0vector.get_length()*np.cos(0.5*theta.get_value())).set_y(0.6*v0vector.get_length()*np.sin(0.5*theta.get_value())).shift(5*LEFT+3.5*DOWN)
        )

        v0txt = MathTex(r"v_{0}").scale(2)
        v0txt.add_updater(
            lambda mob: mob.move_to(v0vector).shift(0.6*UP*np.sin(theta.get_value())*v0vector.get_length() +0.6*RIGHT*np.cos(theta.get_value())*v0vector.get_length())
        )

        examplethrow = ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2))
            ))
        examplethrow.add_updater(
            lambda mob: mob.become(ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2))
            ),color=WHITE))
        )

        v0vector = Vector([5,0],color=YELLOW).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        v0vector.add_updater(
            lambda mob: mob.set_angle((theta.get_value())).set_length(v0.get_value()).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        )

        bkformula = MathTex(r"y(x)=xtan(\theta )-\frac{gx^{2}}{2v_{0}^{2}cos^{2}(\theta )}").shift(UP*3)
        axlabel1 = MathTex(r"y").align_to(ax,UL).shift(RIGHT*0.5)
        axlabel2 = MathTex(r"x").align_to(ax,DR).shift(RIGHT*0.5)

        obj = VGroup(ax,examplethrow,v0vector,v0angle,v0theta,v0txt)
        self.play(Create(obj),Write(bkformula),Write(axlabel1),Write(axlabel2))
        self.play(theta.animate.set_value(80*DEGREES),run_time=4)
        self.play(v0.animate.set_value(3),run_time=3)
        self.play(theta.animate.set_value(30*DEGREES),run_time=4)
        self.play(v0.animate.set_value(5),run_time=5)
        self.play(theta.animate.set_value(45*DEGREES),run_time=3)
        self.play(v0.animate.set_value(4),run_time=4)





class Eigenschaften1(Scene):
    def construct(self):

        #winkelgruppe
        n = NumberPlane()
        ax = Axes(x_range=[0,10,1],x_length=10,y_range=[0,7,1],y_length=7)
        v0 = ValueTracker(8)
        Range = ValueTracker(0.01)
        rpoint = Dot(radius=0.2,color=YELLOW).set_y(-3.5)
        rpoint.add_updater(lambda mob: mob.set_x(
            -5+ v0.get_value()**2/9.81 *np.sin(2*(0.5*np.arcsin(9.81*Range.get_value()/v0.get_value()**2)))
        ))
        rptex = MathTex(r"R").scale(2)
        rptex.add_updater(lambda mob: mob.next_to(rpoint,UR))
        owg = Tex("obere Winkelgruppe")
        uwg = Tex("untere Winkelgruppe")
        owg.add_updater(lambda mob: mob.next_to(f2,UP))
        uwg.add_updater(lambda mob: mob.next_to(f1,UP))

        f1 = ax.plot(lambda x: 0)
        f1.add_updater(
            lambda mob: mob.become(ax.plot(
            lambda x: (np.tan((0.5*np.arcsin(9.81*Range.get_value()/v0.get_value()**2)))*x - ((9.81*x**2)/(2*v0.get_value()**2 * np.cos((0.5*np.arcsin(9.81*Range.get_value()/v0.get_value()**2)))**2))),color=RED)))
        
        f2 = ax.plot(lambda x: 0)
        f2.add_updater(
            lambda mob: mob.become(ax.plot(
            lambda x: (np.tan((0.5*(PI-np.arcsin(9.81*Range.get_value()/v0.get_value()**2))))*x - ((9.81*x**2)/(2*v0.get_value()**2 * np.cos((0.5*(PI-np.arcsin(9.81*Range.get_value()/v0.get_value()**2))))**2))),color=GREEN)))
        
        v0vector = Vector([5,0],color=YELLOW).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        v0vector.add_updater(
            lambda mob: mob.set_angle((0.5*np.arcsin(9.81*Range.get_value()/v0.get_value()**2))).set_length(0.2*v0.get_value()).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2))
        
        v0vector2 = Vector([5,0],color=YELLOW).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        v0vector2.add_updater(
            lambda mob: mob.set_angle((0.5*(PI-np.arcsin(9.81*Range.get_value()/v0.get_value()**2)))).set_length(0.2*v0.get_value()).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2))

        obj = VGroup(ax,f1,f2,v0vector,v0vector2,rpoint,rptex)
        self.play(Create(obj),run_time=2)
        self.play(Range.animate.set_value(5),run_time=6)
        self.play(Range.animate.set_value(9),v0.animate.set_value(10),run_time=5)
        self.play(Range.animate.set_value(10),run_time=4)
        self.play(v0.animate.set_value(11.7),run_time=4)
        self.play(Write(owg))
        self.play(Write(uwg))
        self.wait(4)





class Eigenschaften2(Scene):
    def construct(self):

        #h0
        n = NumberPlane()
        ax = Axes(x_range=[0,10,1],x_length=10,y_range=[0,7,1],y_length=7)
        v0 = ValueTracker(5)
        theta = ValueTracker(0)
        h0 = ValueTracker(0.01)

        v0angle = Arc(start_angle=0)
        v0angle.add_updater(lambda mob: mob.become(Arc(color=WHITE,angle=theta.get_value(),radius=0.5*v0vector.get_length()).shift(5*LEFT+3.5*DOWN + UP*h0.get_value())))

        v0theta = MathTex(r"\theta").scale(2)
        v0theta.add_updater(
            lambda mob: mob.set_x(0.6*v0vector.get_length()*np.cos(0.5*theta.get_value())).set_y(0.6*v0vector.get_length()*np.sin(0.5*theta.get_value())).shift(5*LEFT+3.5*DOWN + UP*h0.get_value())
        )

        h0txt = MathTex(r"h_{0}").scale(2)
        h0txt.add_updater(
            lambda mob: mob.next_to(h0vector,LEFT)
        )

        h0vector = Rectangle(color=GREEN,fill_color=GREEN,fill_opacity=1,width=0.2).shift(LEFT*5)
        h0vector.add_updater(
            lambda mob: mob.set_y(0.5*h0.get_value()-3.5).set_height(h0.get_value())
        )

        examplethrow = ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2)) +h0.get_value()
            ))
        examplethrow.add_updater(
            lambda mob: mob.become(ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2)) +h0.get_value()
            ),color=WHITE))
        )

        v0vector = Vector([5,0],color=YELLOW).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        v0vector.add_updater(
            lambda mob: mob.set_angle((theta.get_value())).set_length(v0.get_value()).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2 + UP*h0.get_value())
        )

        bkformula = MathTex(r"y(x)=xtan(\theta )-\frac{gx^{2}}{2v_{0}^{2}cos^{2}(\theta )}+h_{0}").shift(UP*3)
        axlabel1 = MathTex(r"y").align_to(ax,UL).shift(RIGHT*0.5)
        axlabel2 = MathTex(r"x").align_to(ax,DR).shift(RIGHT*0.5)

        obj = VGroup(ax,h0txt,h0vector,examplethrow,v0vector,v0angle,v0theta)
        self.play(Create(obj),Write(bkformula),Write(axlabel1),Write(axlabel2))
        self.play(theta.animate.set_value(30*DEGREES),run_time=3)
        self.play(v0.animate.set_value(3),run_time=3)
        self.play(h0.animate.set_value(3),run_time=3)
        self.play(theta.animate.set_value(60*DEGREES),run_time=3)
        self.play(h0.animate.set_value(5),run_time=3)
        self.play(theta.animate.set_value(10*DEGREES),run_time=5)
        self.play(h0.animate.set_value(0.01),run_time=2)
        self.play(theta.animate.set_value(30*DEGREES),v0.animate.set_value(5),run_time=1)





class PauseAndPonder(Scene):
    def construct(self):
        
        bkformula = MathTex(r"y(x)=", r"tan(\theta )x", r"-\frac{gx^{2}}{2v_{0}^{2}cos^{2}(\theta )}").to_edge(UP).shift(RIGHT*3)
        ansatz = MathTex(r"y(x)=0").shift(UP+RIGHT*4).scale(1.5)
        lösung = MathTex(r"R=\frac{v_{0}^{2}}{g}sin(2\theta)")
        r = Tex("Reichweite").shift(UP).scale(1.5)
        n = NumberPlane()
        ax = Axes(x_range=[0,10,1],x_length=10,y_range=[0,7,1],y_length=7)
        rbracket = Brace(mobject=r).rotate(PI).scale(2.6).align_to(ax,LEFT).shift(RIGHT*0.2+DOWN*0.4)
        r.shift(LEFT*0.6)
        v0 = ValueTracker(5)
        theta = ValueTracker(0)

        examplethrow = ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2))
            ))
        examplethrow.add_updater(
            lambda mob: mob.become(ax.plot(
            lambda x: (np.tan(theta.get_value())*x - ((x**2)/(1.5*v0.get_value()**2 * np.cos(theta.get_value())**2))
            ),color=WHITE))
        )

        v0vector = Vector([5,0],color=YELLOW).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        v0vector.add_updater(
            lambda mob: mob.set_angle((theta.get_value())).set_length(0.5*v0.get_value()).align_to(ax,DL).shift(UP*0.2+RIGHT*0.2)
        )

        axlabel1 = MathTex(r"y").align_to(ax,UL).shift(RIGHT*0.5)
        axlabel2 = MathTex(r"x").align_to(ax,DR).shift(RIGHT*0.5)

        obj = VGroup(ax,examplethrow,v0vector)
        self.play(Create(obj),Write(bkformula),Write(axlabel1),Write(axlabel2))
        self.play(theta.animate.set_value(55*DEGREES),run_time=3)
        self.play(v0.animate.set_value(3.6),run_time=5)
        self.play(Write(r),DrawBorderThenFill(rbracket),run_time=3)
        self.wait(2)
        self.play(Write(ansatz))
        self.wait(5)





class Ending(Scene):
    def construct(self):
        n = NumberPlane()
        manimlogo = ManimBanner().scale(0.5)
        musicimg = ImageMobject("3b1bmusiclogo").scale(0.4)
        mltxt = Tex("https://docs.manim.community/en/stable/index.html")
        mimgtxt = Tex("https://vincerubinetti.bandcamp.com/album/the-music-of-3blue1brown").scale(0.9)
        desmostxt = Tex("https://www.desmos.com/?lang=en").scale(0.9)
        lp1 = Tex("https://www.leifiphysik.de/mechanik/waagerechter-und-schraeger-wurf/grundwissen/schraeger-wurf-nach-oben-mit-anfangshoehe").scale(0.9)
        lp2 = Tex("https://www.leifiphysik.de/mechanik/waagerechter-und-schraeger-wurf/grundwissen/waagerechter-wurf").scale(0.9)
        lp3 = Tex("https://www.leifiphysik.de/mechanik/freier-fall-senkrechter-wurf").scale(0.9)
        lp4 = Tex("https://www.leifiphysik.de/mechanik/beschleunigte-bewegung").scale(0.9)
        lp5 = Tex("https://www.leifiphysik.de/mechanik/gleichfoermige-bewegung").scale(0.9)
        download = Tex("Download zum Vortrag, Skript, Code:")
        downloadlink = Tex("")

        objs = VGroup(manimlogo,mltxt,mimgtxt,desmostxt,lp1,lp2,lp3,lp4,lp5,download,downloadlink)
        objs.set_opacity(0)

        #self.add(n)
        self.wait(2)
        self.play(manimlogo.animate.set_opacity(1))
        self.play(manimlogo.animate.shift(5.5*LEFT + 2.8*UP))

        self.play(mltxt.animate.set_opacity(1))
        self.play(mltxt.animate.shift(1*LEFT + 1.3*UP))

        self.play(FadeIn(musicimg))
        self.play(musicimg.animate.shift(5.5*LEFT + -1.3*UP))

        self.play(mimgtxt.animate.set_opacity(1))
        self.play(mimgtxt.animate.shift(-0.1*LEFT + -3.5*UP))

        self.wait(6)
        self.play(FadeOut(objs,musicimg),run_time=2)
        self.wait()

        self.play(lp1.animate.set_opacity(1))
        self.play(lp1.animate.shift(0*LEFT + 3*UP))

        self.play(lp2.animate.set_opacity(1))
        self.play(lp2.animate.shift(0*LEFT + 1.8*UP))

        self.play(lp3.animate.set_opacity(1))
        self.play(lp3.animate.shift(0.15*LEFT + 0.8*UP))

        self.play(lp4.animate.set_opacity(1))
        self.play(lp4.animate.shift(0.4*LEFT + 0.1*UP))

        self.play(lp5.animate.set_opacity(1))
        self.play(lp5.animate.shift(0.3*LEFT + -0.4*UP))

        self.play(desmostxt.animate.set_opacity(1))
        self.play(desmostxt.animate.shift(2.95*LEFT + -1*UP))

        self.play(download.animate.set_opacity(1))
        self.play(download.animate.shift(2.35*LEFT + -2*UP))

        self.wait(6)
        self.play(FadeOut(lp1,lp2,lp3,lp4,lp5,desmostxt,download,downloadlink),run_time=2)
        self.wait()





class Zusammenfassung(Scene):
    def construct(self):

        n = NumberPlane()
        zf = Tex("Zusammenfassung:")
        teilv = Tex("Teilgeschwindigkeiten:").to_corner(UL).shift(DOWN)
        vxformula = MathTex(r"v_{x}",r"=v_{0}\cdot cos(\theta)").shift(UP*0.8+5*LEFT)
        vyformula = MathTex(r"v_{y}",r"=v_{0}\cdot sin(\theta)").shift(1.5*UP+5*LEFT)
        vxformula[0].set_color(RED)
        vyformula[0].set_color(GREEN)
        horib = Tex("horizontale Bewegung:").to_corner(UL).shift(4*DOWN)
        vst6 = MathTex(r"x(t)=",r"v_{0}\cdot cos(\theta)",r"\cdot t").to_corner(UL).shift(4.7*DOWN)
        vst6[1].set_color(RED)
        vertb = Tex("vertikale Bewegung:").to_corner(UL).shift(4*DOWN).to_corner(UL).shift(5.9*DOWN)
        sat8 = MathTex(r"y(t)=",r"v_{0}\cdot sin(\theta)",r"t-\frac{1}{2}gt^{2}").to_corner(UL).shift(6.4*DOWN)
        sat8[1].set_color(GREEN)
        bk = Tex("Bahnkurve:").to_edge(UP).shift(RIGHT*1.2+DOWN)
        bkformula = MathTex(r"y(x)=", r"tan(\theta )\cdot x", r"-\frac{gx^{2}}{2v_{0}^{2}cos^{2}(\theta )}").to_edge(UP).shift(RIGHT*3.3+1.3*DOWN)

        #self.add(n)
        self.add(zf.to_corner(UL))
        self.add(teilv,vxformula,vyformula)
        self.add(horib,vst6)
        self.add(vertb,sat8)
        self.add(bk,bkformula)