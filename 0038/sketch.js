var A,r1,r2,r3,r4,r5,r6
function setup(){
    createCanvas(800,800);
    background(76);
    r1 = 300;
    r2 = 100;
    A = 400;
    r = 300;
    r3 = 50;
    r4 = 75;
    r5 = 400;
    r6 = 250;
}
function draw(){
    clear();
    background(76);
    noStroke();
    fill(255,200,125);
    ellipse(400,400,30,30);//sun
    fill(7,94,181);
    ellipse(400+r1*cos(A),400+r2*sin(A),40,40);//earth
    fill(217,233,249);
    ellipse(400+r3*sin(A)+r1*cos(A),400+r4*cos(A)+r2*sin(A),10,10);//moon
    fill(178,46,32);
    ellipse(400+r5*cos(A),400+r6*sin(A),40,40);//mars
    fill(255,255,221);
    ellipse(400+r4*sin(A)+r5*cos(A),400+r3*cos(A)+r6*sin(A),10,10);//deimos
    fill(173,75,39);
    ellipse(400+r3*sin(A)+r5*cos(A),400+r4*cos(A)+r6*sin(A),20,20);//phobos
    A = A+25;
}
