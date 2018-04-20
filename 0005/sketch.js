//setup for variables
var x1,x2,d1,d2;
//setup for canvas
function setup(){
    createCanvas(600,400);
    x1 = 100;
    x2 = 500;
    d1 = 0;
    d2 = 1;
}
//draw the balls
function draw (){
    clear();
    background(144);
    ellipse (x1,200,30,30);
    ellipse (x2,200,30,30);
//if at extremities satisfying following boundary conditions
if ((x1<0) && (x2>width))
    {
    d1 = 0; //direction swap to be effected
    d2 = 1;
    }
//
if ((d1==0) && (d2==1))
    {
    x1++; //and increment shall be as per this
    x2--;
    }
//if at extremities satisfying following boundary conditions
if ((x1>width) && (x2<0))
    {
    d1 = 1; //direction swap to be effected
    d2 = 0;
    }
if ((d1==1) && (d2==0))
    {
    x1--; //and increment shall be as per this
    x2++;
    }
}
