var x,y,r1,r2,A
function setup(){
createCanvas (500,500);
background (67);
r1 = 240;
r2 = 50;
A = 20;
//let central location be 250,250, so x = 250, y = 250;
}
function draw (){
    clear ();
    background (67);
    ellipse(250,250,20,20);//centre
    //x = r cos a and y = r sin a  as per trigonometry
    A = A+25;
    ellipse((250+ r1*cos(A)),(250+r2*sin(A)),25,25);
}
